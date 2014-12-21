(function () {
  'use strict';

  angular
    .module('projector', [
      'projector.config',
      'projector.routes',
      'projector.accounts',
      'projector.authentication',
      'projector.layout',
      'projector.utils'
    ]);

  angular
    .module('projector.routes', ['ngRoute']);
  angular
    .module('projector.config', []);

  angular
    .module('projector')
    .run(run);

  run.$inject = ['$http'];
  function run($http) {
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
  }
})();
