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
        $scope.profileActive = 'active';
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
        $scope.profilePage = function () {
            $scope.profileActive = 'active';
            $scope.diagnosesActive = '';
            $scope.diagnoseRowShow = false
        };
        $scope.diagnosesPage = function () {
            $scope.profileActive = '';
            $scope.diagnoseRowShow = false;
            $scope.diagnosesActive = 'active'
        };
        $scope.diagnoseRow = function (id) {
            $scope.profileActive = '';
            $scope.diagnosesActive = '';
            $scope.diagnoseRowShow = true;
            $http.get('api/v1/diagnose/'+id)
                .success(function (data, status, headers, config) {
                    $scope.diagnose = data
                }
            )

        };
        $scope.goToLink = function (id) {
            $scope.profile.first_name = "LOL " + id;
            $window.location = 'api/v1/diagnose/' + id;
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