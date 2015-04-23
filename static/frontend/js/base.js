$(document).ready(function() {

    var
    /*data = [
      ['', 'Maserati', 'Mazda', 'Mercedes', 'Mini', 'Mitsubishi'],
      ['2009', 0, 2941, 4303, 354, 5814],
      ['2010', 3, 2905, 2867, 412, 5284],
      ['2011', 4, 2517, 4822, 552, 6127],
      ['2012', 2, 2422, 5399, 776, 4151]
    ],*/
        container = document.getElementById('example'),
        hot;
    /*color;
    color = function(instance, td, row, col, prop, value, cellProperties) {
        Handsontable.renderers.TextRenderer.apply(this, arguments);
        td.style.backgroundColor = '#2d2e2f';

    };*/

    function create_table(obj) {
        console.log('create_table called')
        console.log('data', obj);
        hot = new Handsontable(container, {
            data: (function() {
                var data = obj;
                var page = parseInt(window.location.hash.replace('#', ''), 10) || 1,
                    limit = 10,
                    row = (page - 1) * limit,
                    count = page * limit,
                    part = [];

                for (; row < count; row++) {
                    part.push(data[row]);
                }

                return part;
            })(),
            //minSpareRows: 1,
            colWidths: [200, 200],
            colHeaders: ["Name", "Description"],
            contextMenu: false,
            columnSorting: true,
            readOnly: true
        });


        function bindDumpButton() {

            Handsontable.Dom.addEvent(document.body, 'click', function(e) {

                var element = e.target || e.srcElement;

                if (element.nodeName == "BUTTON" && element.name == 'dump') {
                    var name = element.getAttribute('data-dump');
                    var instance = element.getAttribute('data-instance');
                    var hot = window[instance];
                    console.log('data of ' + name, hot.getData());
                }
            });
        }
        bindDumpButton();

    }


    function getSinger() {
        var obj;
        $.ajax({
            url: '/api/singers/',
            type: 'GET',
            success: function(responce) {
                console.log('responce', responce);
                var obj = [];
                for (var i = 0; i < responce.results.length; i++) {
                    var singer = [responce.results[i].name, responce.results[i].description];
                    obj.push(singer);
                };
                create_table(obj);
            }
        });
    }
    getSinger();
});