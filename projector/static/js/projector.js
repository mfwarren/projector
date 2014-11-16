(function () {
  'use strict';

  angular
    .module('projector', [
      'projector.config',
      'projector.routes',
      'projector.authentication'
    ]);

  angular
    .module('projector.routes', ['ngRoute']);
  angular
    .module('projector.config', []);
})();
