(function () {
  'use strict';

  angular
    .module('projector.authentication', [
      'projector.authentication.controllers',
      'projector.authentication.services'
    ]);

  angular
    .module('projector.authentication.controllers', []);

  angular
    .module('projector.authentication.services', ['ngCookies']);
})();
