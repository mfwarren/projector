/**
* AccountController
* @namespace projector.accounts.controllers
*/
(function () {
  'use strict';

  angular
    .module('projector.accounts.controllers')
    .controller('AccountController', AccountController);

  AccountController.$inject = ['$location', '$routeParams', 'Posts', 'Account'];

  /**
  * @namespace AccountController
  */
  function AccountController($location, $routeParams, Posts, Account) {
    var vm = this;

    vm.account = undefined;
    vm.posts = [];

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf projector.accounts.controllers.AccountController
    */
    function activate() {
      var username = $routeParams.username.substr(1);

      Account.get(username).then(accountSuccessFn, accountErrorFn);
      Posts.get(username).then(postsSuccessFn, postsErrorFn);

      /**
      * @name accountSuccessAccount
      * @desc Update `account` on viewmodel
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


      /**
        * @name postsSucessFn
        * @desc Update `posts` on viewmodel
        */
      function postsSuccessFn(data, status, headers, config) {
        vm.posts = data.data;
      }


      /**
        * @name postsErrorFn
        * @desc
        */
      function postsErrorFn(data, status, headers, config) {
      }
    }
  }
})();
