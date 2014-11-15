/* Project specific Javascript goes here. */

var app = angular.module('project', []);

app.controller('TaskController', [ '$http', function($http){
  var project = this;
  project.tasks = [];

  this.tasks = $http.get('tasks/').success(function(data){
    project.tasks = data;
    console.log(data);
  });
}]);
