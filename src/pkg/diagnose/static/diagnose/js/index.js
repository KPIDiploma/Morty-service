/**
 * Created by Kryvonis on 3/23/17.
 */
var app = angular.module('diagnoseApp', ['ngMaterial', 'ngMessages']);
app.config(
    ['$interpolateProvider', '$httpProvider', function ($interpolateProvider, $httpProvider) {
        $interpolateProvider.startSymbol('[[');
        $interpolateProvider.endSymbol(']]');
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }]
);


app.controller('indexController', function ($scope, $location, $http, $mdDialog) {

    $scope.diagnosesLoad = function () {
        $http
            .get('/api/v1/current-diagnoses')
            .success(function (data) {
                $scope.diagnoses = data.diagnoses;

            }).error(function (data, status, header, config) {

        });
    };

    $scope.showEditTask = function (ev, files) {
        $scope.files = files;
        $mdDialog.show({
            controller: DialogController,
            templateUrl: 'files.tmpl.html',
            parent: angular.element(document.body),
            targetEvent: ev,
            scope: $scope,
            preserveScope: true,
            clickOutsideToClose: true
        });
    };

    function DialogController($scope, $mdDialog) {
        $scope.hide = function () {
            $mdDialog.hide();
        };

        $scope.cancel = function () {
            $mdDialog.cancel();
        };

        $scope.answer = function (answer) {
            $mdDialog.hide(answer);
        };
    }

    $scope.diagnosesLoad()
});
