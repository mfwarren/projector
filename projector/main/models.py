from django.db import models
from django.conf import settings
from autoslug import AutoSlugField


class Project(models.Model):
    """
    A Project can have many tasks, it also is visible/editable/estimateable by
    different sets of users.  The owner is expected to produce the project and
    list the tasks for it.  They would then invite people to submit estimates.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=255)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hide_estimates = models.BooleanField(default=True)
    slug = AutoSlugField(populate_from='name')  # for nice urls for logged in users
    public_token = models.CharField(max_length=64, null=True)  # for unique public urls

    def tasks(self):
        return Task.objects.filter(project=self)

    def smart_blurb(self):
        return "put something here about last updated or total duration"

    class Meta:
        permissions = (
            ('estimate_project', 'Estimate Project'),  # permission to submit estimate
            ('view_project', 'View Project'),  # private view permission
            ('owns_project', 'Owns Project'),  # owner - can add tasks to project
        )

    def __unicode__(self):
        return self.name


class Task(models.Model):
    """
    A project contains many tasks. From a project manager perspective they
    may want to approve/disapprove tasks that are later deemed out of scope,
    group tasks and assign them to teams or people.
    """
    description = models.CharField(max_length=255)
    assignee = models.CharField(max_length=255, null=True, blank=True)
    project = models.ForeignKey(Project)
    is_enabled = models.BooleanField(default=True)
    group = models.CharField(max_length=64, null=True, blank=True)
    actual_duration = models.FloatField(null=True, blank=True)  # used for reference class forecasting
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def estimates(self):
        return TaskEstimate.objects.filter(task=self)

    def __unicode__(self):
        return self.description


class TaskEstimate(models.Model):
    """
    Users can submit an estimate for a task.  The estimate consists of minimum,
    likely and maximum estimate in hours and a risk curve for how confident they
    are around the likely estimate.
    Users can leave comments with their estimate.
    if a particular task is outside the scope of a user to estimate on they can
    flag as is_na.  If a new task is added to an already estimated project they can
    be notified in the UI of unestimated tasks.
    """
    CURVES = (('no_idea', 'No Idea'),
              ('certain', 'Certain'),
              ('less_sure', 'Less Sure'),
              ('very_unsure', 'Very Unsure'))
    task = models.ForeignKey(Task)
    likely = models.FloatField()
    minimum = models.FloatField()
    maximum = models.FloatField()
    curve = models.CharField(max_length=32, choices=CURVES)
    comments = models.TextField(null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    is_na = models.BooleanField(default=False)  # user able to flag task as NA for them to estimate
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%f hours for %s" % (self.likely, self.task.description)


class Invitation(models.Model):
    """
    Owners of the project can send invites to gather estimates, or provide private
    view only access to the final project estimate.
    """
    to_email = models.EmailField()
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL)
    project = models.ForeignKey(Project)
    permission = models.CharField(max_length=32)  # estimate/view/own
    token = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "from %s to %s for %s to %s" % (self.from_user.username, self.to_email,
                                               self.permission, self.project)
