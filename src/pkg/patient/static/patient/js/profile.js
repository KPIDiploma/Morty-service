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
        $scope.profilePage = function () {
            $http
                .get('api/v1/current-user')
                .success(function (data, status, headers, config) {
                    $scope.profile = data;
                }).error(function (data, status, header, config) {

            });


            $scope.profileActive = 'active';
            $scope.diagnosesActive = '';
            $scope.diagnoseRowShow = false
        };

        $scope.diagnosesPage = function () {
            $http
                .get('api/v1/current-diagnoses')
                .success(function (data, status, headers, config) {
                    $scope.diagnoses = data.diagnoses;
                }).error(function (data, status, header, config) {

            });

            $scope.profileActive = '';
            $scope.diagnoseRowShow = false;
            $scope.diagnosesActive = 'active'
        };

        $scope.diagnoseRow = function (id) {
            angular.forEach($scope.diagnoses, function (value, key) {
                if (value['id'] == id) {
                    $scope.diagnose = value;
                    return;
                }
            });

            $scope.profileActive = '';
            $scope.diagnosesActive = '';
            $scope.diagnoseRowShow = true;


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

        $scope.setBlood = function (type) {
            $scope.profile.blood_type = type;
        };

        $scope.profileActive = 'active';
        $scope.profilePage();


    });