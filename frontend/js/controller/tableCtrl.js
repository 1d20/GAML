app.controller('tableCtrl', ['$scope', 'ngTableParams', '$http',
    function($scope, ngTableParams, $http) {
        $scope.getSingers = function(page, count) {
            $http.get('/api/singers/').
            success(function(responce) {
                console.log(responce);
                //---add to table singers from server
                $scope.tableParams = new ngTableParams({
                    page: page, // show first page
                    count: count // count per page
                }, {
                    total: responce.count, // length of data
                    getData: function($defer, params) {
                        $defer.resolve(responce.results.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                    }
                });
                console.log($scope.tableParams)
            }).
            error(function(responce) {
                console.log('error:', responce)
            });
        }

        $scope.getSingers(1, 10);
        /*$scope.tableParams = new ngTableParams({
            page: 1, // show first page
            count: 10 // count per page
        }, {
            total: data.length, // length of data
            getData: function($defer, params) {
                $defer.resolve(data.slice((params.page() - 1) * params.count(), params.page() * params.count()));
            }
        });*/
    }
]);