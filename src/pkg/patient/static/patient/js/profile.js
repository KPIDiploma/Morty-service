/**
 * Created by Kryvonis on 3/23/17.
 */
angular.module('profileApp', ['ngRoute'])
    .config(
        ['$interpolateProvider', '$httpProvider', function ($interpolateProvider, $httpProvider) {
            $interpolateProvider.startSymbol('[[');
            $interpolateProvider.endSymbol(']]');
            $httpProvider.defaults.xsrfCookieName = 'csrftoken';
            $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        }]
    )


    .controller('profileController', function ($scope, $location, $http, $window) {
        $scope.profile = {
            "id": 6,
            "first_name": "Test",
            "last_name": "Testovich",
            "email": "test@test.com",
            "blood_type": "0+"
        };
        $scope.diagnoses = [
            {
                "id": 1,
                "text": "Basic text",
                "files": [
                    {
                        "id": 1,
                        "file": "http://127.0.0.1:8000/media/ticket_38061888.pdf"
                    },
                    {
                        "id": 2,
                        "file": "http://127.0.0.1:8000/media/v-Fpnb4wvAY.jpg"
                    }
                ]
            },
            {
                "id": 2,
                "text": "test2",
                "files": [
                    {
                        "id": 3,
                        "file": "http://127.0.0.1:8000/media/wallhaven-442687.jpg"
                    }
                ]
            }
        ];
        $scope.profile_page = function () {
            $scope.profile_active = 'active';
            $scope.diagnoses_active = ''
        };
        $scope.diagnoses_page = function () {
            $scope.profile_active = '';
            $scope.diagnoses_active = 'active'
        };
        $scope.logout = function () {
            $http
                .post('api/v1/auth/logout')
                .success(function (data, status, headers, config) {
                    delete $window.sessionStorage.token;
                    $window.location = '/';
                }).error(function (data, status, header, config) {
                delete $window.sessionStorage.token;
                $window.location = '/';
            });
        };


    });