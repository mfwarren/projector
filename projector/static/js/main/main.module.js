(function () {
  'use strict';

  angular
    .module('projector.tasks', [
      'projector.tasks.controllers',
      'projector.tasks.directives',
      'projector.tasks.services'
    ]);

  angular
    .module('projector.tasks.controllers', []);

  angular
    .module('projector.tasks.directives', ['ngDialog']);

  angular
    .module('projector.tasks.services', []);
})();
