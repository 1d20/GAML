app.controller('tableCtrl', ['$scope', 'ngTableParams', '$http',
    function($scope, ngTableParams, $http) {
        var data = [{
            name: "Moroni",
            age: 50
        }, {
            name: "Tiancum",
            age: 43
        }, {
            name: "Jacob",
            age: 27
        }, {
            name: "Nephi",
            age: 29
        }, {
            name: "Enos",
            age: 34
        }, {
            name: "Tiancum",
            age: 43
        }, {
            name: "Jacob",
            age: 27
        }, {
            name: "Nephi",
            age: 29
        }, {
            name: "Enos",
            age: 34
        }, {
            name: "Tiancum",
            age: 43
        }, {
            name: "Jacob",
            age: 27
        }, {
            name: "Nephi",
            age: 29
        }, {
            name: "Enos",
            age: 34
        }, {
            name: "Tiancum",
            age: 43
        }, {
            name: "Jacob",
            age: 27
        }, {
            name: "Nephi",
            age: 29
        }, {
            name: "Enos",
            age: 34
        }];



        $scope.getSingers = function() {
            $http.get('/api/singers/').
            success(function(responce) {
                console.log(responce);
                //$scope.singers = responce;
                $scope.tableParams = new ngTableParams({
                    page: 1, // show first page
                    count: 10 // count per page
                }, {
                    total: responce.count, // length of data
                    getData: function($defer, params) {
                        $defer.resolve(responce.result.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                    }
                });
                console.log($scope.tableParams)
                console.log($scope.singers)
            }).
            error(function(responce) {
                console.log('error:', responce)
            });
        }

        $scope.getSingers();
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