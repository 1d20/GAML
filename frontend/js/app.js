var app = angular.module('GAML', [
    'ui.router',
    'ngTable',
    //'smart-table'
])

app.config(['$urlRouterProvider', '$locationProvider', '$stateProvider', '$httpProvider',
    function($urlRouterProvider, $locationProvider, $stateProvider, $httpProvider) {
        /*
        ROUTING
        */
        $urlRouterProvider.otherwise('/table');
        $stateProvider
            .state('table', {
                url: '/table',
                views: {
                    'table': {
                        templateUrl: '/static/frontend/templates/table.html',
                        controller: function($scope) {
                            console.log('table view');
                        }
                    }
                }
            })

    }
]);