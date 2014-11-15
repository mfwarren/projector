(function () {
  'use strict';

  angular
    .module('projector', [
      'projector.routes',
      'projector.authentication'
    ]);

  angular
    .module('projector.routes', ['ngRoute']);
})();
