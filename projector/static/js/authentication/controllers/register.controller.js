/**
 * Register controller
 * @namespace projector.authentication.controllers
 */
(function () {
  'use strict';

  angular
    .module('projector.authentication.controllers')
    .controller('RegisterController', RegisterController);

  RegisterController.$inject = ['$location', '$scope', 'Authentication'];

  /**
   * @namespace RegisterController
   */
  function RegisterController($location, $scope, Authentication) {
    var vm = this;

    vm.register = register;

    activate();

    /**
     * @name activate
     * @desc Actions to be performed when this controller is instantiated
     * @memberOf projector.authentication.controllers.RegisterController
     */
    function activate() {
      // If the user is authenticated, they should not be here.
      if (Authentication.isAuthenticated()) {
        $location.url('/');
      }
    }

    /**
     * @name register
     * @desc Register a new user
     * @memberOf projector.authentication.controllers.RegisterController
     */
    function register() {
      Authentication.register(vm.email, vm.password, vm.username);
    }
  }
})();
