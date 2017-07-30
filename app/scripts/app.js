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
    'ngTouch',
    'ui.router',
    'ngValidate'
  ])
  .config(function ($routeProvider, $locationProvider, $stateProvider, $urlRouterProvider) {
    // $routeProvider
    //   .when('/', {
    //     templateUrl: 'views/login.html',
    //     controller: 'MainCtrl',
    //     controllerAs: 'main'
    //   })
    //   .when('/register', {
    //     templateUrl: 'views/register.html',
    //     controller: 'AboutCtrl',
    //     controllerAs: 'about'
    //   })
    //   .otherwise({
    //     redirectTo: '/'
    //   });
    $urlRouterProvider.otherwise('/login');
    $stateProvider
    .state('login', {
                url: '/login',
                views: {
                    '@': {
                        templateUrl: 'views/login.html',
                        controller: 'MainCtrl',
                        controllerAs:'login'
                    }
                }
      })
    .state('register', {
                url: '/register',
                views: {
                    '@': {
                        templateUrl: 'views/register.html',
                        controller: 'SignupCtrl',
                        controllerAs:'reg'
                    }
                }
      })


      $locationProvider.hashPrefix('');
  });