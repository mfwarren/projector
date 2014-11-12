from django.contrib import admin
from main.models import Project, Task, TaskEstimate, Invitation
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    pass
admin.site.register(Project, ProjectAdmin)


class TaskAdmin(admin.ModelAdmin):
    pass
admin.site.register(Task, TaskAdmin)


class TaskEstimateAdmin(admin.ModelAdmin):
    pass
admin.site.register(TaskEstimate, TaskEstimateAdmin)


class InvitationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Invitation, InvitationAdmin)
