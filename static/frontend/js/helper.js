(
    function abcGen() {
        var res = []
        for (var i = 0; i < 26; i++) {
            res.push(String.fromCharCode(97 + i));
        };
        console.log(res);
        return res;
    }
)()