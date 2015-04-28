var app = angular.module('TravelApp', [
    'ui.router'
])

app.config(['$urlRouterProvider', '$locationProvider', '$stateProvider', '$httpProvider',
    function($urlRouterProvider, $locationProvider, $stateProvider, $httpProvider) {



        /*
        ROUTING
        */
        $urlRouterProvider.otherwise('/search');
        $stateProvider
            .state('search', {
                url: '/search',
                views: {
                    'box@search': {
                        templateUrl: '/static/frontend/templates/search.html',
                        controller: function($scope) {
                            console.log('search');
                        }
                    }
                }
            })

    }
]);