'use strict';

/**
 * @ngdoc function
 * @name accountingApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the accountingApp
 */
angular.module('accountingApp')
  .controller('MainCtrl', function ($scope,$state,Auth) {
    var self = this;
    self.scope = $scope;
    self.scope.login = {};
    self.scope.userexists= false;
    self.scope.userNotexists = false;
    self.scope.checkUser = checkUser;

    function checkUser(){
    	var data = {};
    	data['username'] = self.scope.login.username;
    	Auth.checkuser(data,function(response){
    		if(response.Status == "200"){
    			self.scope.userexists = true;
    		}
    		else{
    			self.scope.userNotexists = true;
    		}
    	});
    }
  });
