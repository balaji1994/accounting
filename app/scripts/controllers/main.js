'use strict';

/**
 * @ngdoc function
 * @name accountingApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the accountingApp
 */
angular.module('accountingApp')
  .controller('MainCtrl', function ($scope,$state,Auth,$cookieStore) {
    var self = this;
    self.scope = $scope;
    self.scope.login = {};
    self.scope.userexists= false;
    self.scope.userNotexists = false;
    self.scope.checkUser = checkUser;
    self.scope.userLogin = userLogin;
    self.scope.loginSubmit = loginSubmit;

    function checkUser(){
    	if(self.scope.login.username){

    	}
    	
    }

    //To login
    function userLogin(){
    	var data = {};
    	data['username'] = self.scope.login.username;
    	data['password'] = self.scope.login.password;
    	// console.log(data);
    	Auth.userlogin(data,function(response){
    		if(response.Status == "200"){
    			alert('login successful!!');
    		}
    	});
    }

    // for validations

    self.scope.validationOptions = {
	    rules: {
	        username: {
	            required: true
	        },
	        password: {
	            required: true,
	            minlength: 6
	        }
	    },
	    messages: {
	        username: {
	            required: "Username is required"
	        },
	        password: {
	            required: "You must enter a password"
	        }
	    }
	}
	// loginform submit
	function loginSubmit(form){
		if(form.validate()){
			if(!self.scope.userexists){
				var data = {};
		    	data['username'] = self.scope.login.username;
		    	Auth.checkuser(data,function(response){
	    		if(response.Status == "200"){
	    			self.scope.userexists = true;
	    		}
	    		else{
	    			self.scope.userNotexists = true;
	    			$state.go('register');
    		}
    	});
    }
    		else{
    			userLogin();
    		}
			
		}
	}
  });
