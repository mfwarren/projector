/**
 * AccountSettingsController
 * @namespace projector.accounts.controllers
 */
(function () {
  'use strict';

  angular
    .module('projector.accounts.controllers')
    .controller('AccountSettingsController', AccountSettingsController);

  AccountSettingsController.$inject = [
    '$location', '$routeParams', 'Authentication', 'Account'
  ];

  /**
   * @namespace AccountSettingsController
   */
  function AccountSettingsController($location, $routeParams, Authentication, Account) {
    var vm = this;

    vm.destroy = destroy;
    vm.update = update;

    activate();


    /**
     * @name activate
     * @desc Actions to be performed when this controller is instantiated.
     * @memberOf projector.accounts.controllers.AccountSettingsController
     */
    function activate() {
      var authenticatedAccount = Authentication.getAuthenticatedAccount();
      var username = $routeParams.username.substr(1);

      // Redirect if not logged in
      if (!authenticatedAccount) {
        $location.url('/');
      } else {
        // Redirect if logged in, but not the owner of this account.
        if (authenticatedAccount.username !== username) {
          debugger;
          $location.url('/');
        }
      }

      Account.get(username).then(accountSuccessFn, accountErrorFn);

      /**
       * @name accountSuccessFn
       * @desc Update `account` for view
       */
      function accountSuccessFn(data, status, headers, config) {
        vm.account = data.data;
      }

      /**
       * @name accountErrorFn
       * @desc Redirect to index
       */
      function accountErrorFn(data, status, headers, config) {
        $location.url('/');
      }
    }


    /**
     * @name destroy
     * @desc Destroy this account
     * @memberOf projector.accounts.controllers.AccountSettingsController
     */
    function destroy() {
      Account.destroy(vm.account.username).then(accountSuccessFn, accountErrorFn);

      /**
       * @name accountSuccessFn
       * @desc Redirect to index
       */
      function accountSuccessFn(data, status, headers, config) {
        Authentication.unauthenticate();
        window.location = '/';

      }
    }


    /**
     * @name update
     * @desc Update this account
     * @memberOf projector.accounts.controllers.AccountSettingsController
     */
    function update() {
      var username = $routeParams.username.substr(1);

      Account.update(username, vm.account).then(accountSuccessFn, accountErrorFn);

      /**
       * @name accountSuccessFn
       * @desc
       */
      function accountSuccessFn(data, status, headers, config) {
      }


      /**
       * @name accountErrorFn
       * @desc
       */
      function accountErrorFn(data, status, headers, config) {
      }
    }
  }
})();
