function abcGen() {
    var res = []
    for (var i = 0; i < 26; i++) {
        res.push(String.fromCharCode(97 - 32 + i));
    };
    console.log(res);
    return res;
}

function generateList(input, aS) {
    appendObj = $(aS);
    console.log(appendObj);
    $.each(input, function(i) {
        var li = $('<li/>')
            .addClass('ui-menu-item')
            .attr('role', 'menuitem')
            .appendTo(appendObj);
        var aaa = $('<a/>')
            .addClass('ui-all')
            .text(input[i])
            .appendTo(li);
    });
}


$(document).ready(function() {
    generateList(abcGen(), 'ul.alpha_cont_ul');
})