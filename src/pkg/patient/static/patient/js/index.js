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


    .controller('indexController', function ($scope, $location, $http) {
        $scope.email = 'test@test.com';
        $scope.password = 'password';

        $scope.updateValue = function () {
            var post_data = {
                email: $scope.email,
                password: $scope.password
            };
            $http({
                method: 'POST',
                url: 'api/v1/auth/login/',
                data: post_data,
                headers: {'Content-Type': 'application/x-www-form-urlencoded'}
            }).success(function (data, status, headers, config) {
                // $scope.session.setUser(data.user);
                //
                // session.setAccessToken(data.accessToken);
            }).error(function (data, status, header, config) {
                $scope.login = 'ERROR';
            });
        };


    });
