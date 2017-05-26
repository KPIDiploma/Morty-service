/**
 * Created by Kryvonis on 3/23/17.
 */
var app = angular.module('profileApp', ['ngMaterial', 'ngMessages']);
app.config(
    ['$interpolateProvider', '$httpProvider', '$mdThemingProvider',
        function ($interpolateProvider, $httpProvider, $mdThemingProvider) {
            $mdThemingProvider.theme('docs-dark', 'default')
                .primaryPalette('blue')
                .dark();
            $interpolateProvider.startSymbol('[[');
            $interpolateProvider.endSymbol(']]');
            $httpProvider.defaults.xsrfCookieName = 'csrftoken';
            $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        }]
);

app.controller('profileController', function ($scope) {
    $scope.profile = {
        id: 1,
        fullname: "Artem Kryvonis",
        email: "kryvonis.artem@gmail.com",
        birthday: null,
        address: null,
        mobile: null,
        sex: null,
        blood_type: null
    };

    $scope.sexs = [{"abbrev": "Male"}, {"abbrev": "Female"}];
    $scope.bloods = [
        {abbrev: '0+'}, {abbrev: "0-"},
        {abbrev: "A+"}, {abbrev: "A-"},
        {abbrev: "B+"}, {abbrev: "B-"},
        {abbrev: "AB+"}, {abbrev: "AB-"}
    ];
    $scope.toggleSidenav = function (menuId) {
        $mdSidenav(menuId).toggle();
    };
    $scope.profilePage = function () {
//            $http
//                .get('api/v1/current-user')
//                .success(function (data, status, headers, config) {
//                    $scope.profile = data;
//                }).error(function (data, status, header, config) {
//
//            });


        $scope.profileActive = 'active';
        $scope.diagnosesActive = '';
        $scope.diagnoseRowShow = false
    };

    // $scope.profileActive = 'active';
    // $scope.profilePage();


});