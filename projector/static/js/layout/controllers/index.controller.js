/**
 * IndexController
 * @namespace projector.layout.controllers
 */
(function () {
  'use strict';

  angular
    .module('projector.layout.controllers')
    .controller('IndexController', IndexController);

  IndexController.$inject = ['$scope', 'Authentication', 'Posts'];

  /**
   * @namespace IndexController
   */
  function IndexController($scope, Authentication, Posts) {
    var vm = this;

    vm.isAuthenticated = Authentication.isAuthenticated();
    vm.posts = [];

    activate();

    /**
     * @name activate
     * @desc Actions to be performed when this controller is instantiated
     * @memberOf projector.layout.controllers.IndexController
     */
    function activate() {
      Posts.all().then(postsSuccessFn, postsErrorFn);

      $scope.$on('post.created', function (event, post) {
        vm.posts.unshift(post);
      });

      $scope.$on('post.created.error', function () {
        vm.posts.shift();
      });


      /**
       * @name postsSuccessFn
       * @desc Update thoughts array on view
       */
      function postsSuccessFn(data, status, headers, config) {
        vm.posts = data.data;
      }


      /**
       * @name postsErrorFn
       * @desc Show snackbar with error
       */
      function postsErrorFn(data, status, headers, config) {
        // Snackbar.error(data.error);
      }
    }
  }
})();
