/**
 * Created by Kryvonis on 3/23/17.
 */
angular.module('indexApp', ['ngRoute'])



// .factory('Authentication', function ($cookies, $http) {
//     function login() {
//         return
//     }
// })


    .config(
        ['$interpolateProvider', '$httpProvider', function ($interpolateProvider, $httpProvider) {
            $interpolateProvider.startSymbol('[[');
            $interpolateProvider.endSymbol(']]');
            $httpProvider.defaults.xsrfCookieName = 'csrftoken';
            $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        }]
    )


    .controller('indexController', function ($scope, $location, $http, $window) {
        $scope.email = 'test@test.com';
        $scope.password = 'password';

        $scope.updateValue = function () {
            $http
                .post('api/v1/auth/login', $scope.user)
                .success(function (data, status, headers, config) {
                    $window.sessionStorage.token = data.token;
                    $window.location = 'api/v1/profile';
                    $scope.login = 'Welcome';
                }).error(function (data, status, header, config) {
                    delete $window.sessionStorage.token;
                    $scope.login = 'ERROR';
            });
        };


    });
