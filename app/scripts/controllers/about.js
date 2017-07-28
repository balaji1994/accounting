'use strict';

/**
 * @ngdoc function
 * @name accountingApp.controller:AboutCtrl
 * @description
 * # AboutCtrl
 * Controller of the accountingApp
 */
angular.module('accountingApp')
  .controller('registerCtrl', function ($scope,$state,Auth,$cookieStore) {
    var self = this;
    self.scope = $scope;

    //function
    self.scope.signUp = signUp;
  });
