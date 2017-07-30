'use strict';

/**
 * @ngdoc function
 * @name accountingApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the accountingApp
 */
angular.module('accountingApp')
  .controller('SignupCtrl', function ($scope,$state,Auth,$cookieStore) {
  	var self=this;
  	self.scope = $scope;
  	self.scope.signup = {};
  	self.scope.signUp = signUp;
  	var currentState = $state.current.name;
  	if(currentState === "register"){
  		// self.scope.signup.account_no= $cookieStore.get('account_no');
  		// console.log(self.scope.signup.account_no);
  		var accno = Math.floor(Math.random()*90000) + 10000;
		self.scope.is_unique = false;
		var data = {};
		data['account_no'] = accno;
		// while(!self.scope.is_unique){
		// 	Auth.checkaccno(data,function(response){
		// 	if(response.Status == "200"){
		// 		self.scope.signup.account_no = accno;
		// 		self.scope.is_unique = true;
		// 	}
		// });
		
		// }
  	}

  	// for validations

    self.scope.validationOptions = {
	    rules: {
	    	account_no:{
	    		required:true,
	    		number:true
	    	},
	        first_name:{
	        	required: true
	        },
	        confirm_name:{
	        	required: true,
	        	equalTo: "#name"
	        },
	        phonenumber:{
	        	required:true
	        },
	        email:{
	        	required:true,
	        	email:true
	        },
	        address:{
	        	required:true
	        },
	        state:{
	        	required:true
	        },
	        city:{
	        	required:true
	        },
	        postcode:{
	        	required:true
	        }

	    },
	    messages: {
	    	account_no:{
	    		required:"Account number cannot be blank",
	    		number:"Should be a number"
	    	},
	        first_name: {
	            required: "Name cannot be blank"
	        },
	        confirm_name: {
	            required: "You must confirm your name",
	            equalTo: "Confirm name should be equal to name"
	        },
	        phonenumber:{
	        	required:"Phone number cannot be blank"
	        },
	        email:{
	        	required:"Email cannot be blank",
	        	email:"Entered email is not valid!!"
	        },
	        address:{
	        	required:"Address cannot be blank"
	        },
	        state:{
	        	required:"State cannot be blank"
	        },
	        city:{
	        	required:"City cannot be blank"
	        },
	        postcode:{
	        	required:"Postcode cannot be blank"
	        }

	    }
	}

	// to signup
	function signUp(form){
		if(form.validate()){
			alert('success');
		}
	}
  });