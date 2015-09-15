'use strict';

/**
 * @ngdoc overview
 * @name airquailfrontApp
 * @description
 * # airquailfrontApp
 *
 * Main module of the application.
 */
angular
  .module('airquailfrontApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl',
        controllerAs: 'main'
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl',
        controllerAs: 'about'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
angular.module('myModule', ['chart.js']);
