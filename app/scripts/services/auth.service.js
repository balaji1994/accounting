/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
  angular
        .module('accountingApp')
		.service('Auth', function($http, $rootScope, $timeout, $cookieStore) {
    var postDomain = window.location.host;
    var postProtocol = window.location.protocol;
    return {
    	login:function(data,callback){
    		$http({
                    url: __env.apiUrl + '/validate/',
                    method: "POST",
                    data: data,
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
                })
                .then(function successCallback(result) {
                	if(result.data.Status == "200"){
                		$cookieStore.put('userid',result.data.user_details.id);
	                	$cookieStore.put('login_token',result.data.user_details.login_token);
	                	$cookieStore.put('name',result.data.user_details.first_name);
                	}
                	callback(result.data);
                	
                }, function errorCallback(result) {
                    callback(result);
                });
    	},
        checkuser:function(data,callback){
            $http({
                    url: __env.apiUrl + '/checkuser/',
                    method: "POST",
                    data: data,
                    headers: { 'Content-Type': 'application/json' }
                })
                .then(function successCallback(result) {
                    // if(result.data.Status == "200"){
                    //     $cookieStore.put('userid',result.data.user_details.id);
                    //     $cookieStore.put('login_token',result.data.user_details.login_token);
                    //     $cookieStore.put('name',result.data.user_details.first_name);
                    // }
                    callback(result.data);
                    
                }, function errorCallback(result) {
                    callback(result.data);
                });
        }
    };
});