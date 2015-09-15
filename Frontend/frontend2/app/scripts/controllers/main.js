'use strict';

/**
 * @ngdoc function
 * @name airquailfrontApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the airquailfrontApp
 */
angular.module('airquailfrontApp')
  .controller('MainCtrl', function () {
    this.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });

angular.module('myModule', ['chart.js']);
