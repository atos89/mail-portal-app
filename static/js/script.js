(function (window, undefine) {
    var document,
        console,
        fn = {},
        _fn = {};

    document = window.document;
    console = window.console;

    fn.init = function () {
        _fn.init();
    };

    _fn.init = function () {
        console.log('called.');
    };

    fn.init();
}(window, this));