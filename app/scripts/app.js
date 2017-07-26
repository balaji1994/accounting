'use strict';

/**
 * @ngdoc overview
 * @name accountingApp
 * @description
 * # accountingApp
 *
 * Main module of the application.
 */
angular
  .module('accountingApp', [
    'ngAnimate',
    'ngAria',
    'ngCookies',
    'ngMessages',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch'
  ])
  .config(function ($routeProvider, $locationProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/login.html',
        controller: 'MainCtrl',
        controllerAs: 'main'
      })
      .when('/register', {
        templateUrl: 'views/register.html',
        controller: 'AboutCtrl',
        controllerAs: 'about'
      })
      .otherwise({
        redirectTo: '/'
      });
  //   $stateProvider
  //   .state({
  //   name: 'hello',
  //   url: '/hello',
  //   template: 'views/login.html'
  // })

      $locationProvider.hashPrefix('');
  });