var bower, dest, src;

src = __dirname;

dest = __dirname + '/../static/frontend';

bower = src + '/bower_components';

module.exports = {
    css: {
        src: [src + '/css/**/*.css'],
        dest: dest + '/css'
    },
    compass: {
        src: [src + '/css/**/*.css'],
        dest: dest + '/css'
    },
    js: {
        src: [src + '/js/**/*.js'],
        dest: dest + '/js'
    },
    templates: {
        src: [src + '/templates/**/*.html'],
        dest: dest + '/templates'
    },
    images: {
        src: [src + '/images/**/*.*'],
        dest: dest + '/images'
    },
    json: {
        src: [src + '/json/**/*.*'],
        dest: dest + '/json'
    },
    sounds: {
        src: [src + '/sounds/**/*.*'],
        dest: dest + '/sounds'
    },
    fonts: {
        src: [src + '/fonts/**/*.*'],
        dest: dest + '/fonts'
    },
    vendors: {
        css: {
            src: [
                bower + '/bootswatch-dist/css/bootstrap.css',
                bower + '/css-toggle-switch/dist/toggle-switch.css',
                bower + '/fontawesome/css/font-awesome.css',
                bower + '/eonasdan-bootstrap-datetimepicker/build/css/bootstrap-datetimepicker.css',
                bower + '/jquery.taginput/src/jquery.taginput.css',
                bower + '/bootstrap-star-rating/css/star-rating.css',
                bower + '/Hover/css/hover.css',
                bower + '/angular-ui-select/dist/select.css'
            ],
            dest: dest + '/css'
        },
        js: {
            src: [
                bower + '/angular/angular.js',
                bower + '/angular-ui-router/release/angular-ui-router.js'
            ],
            dest: dest + '/js'
        },
        fonts: {
            src: [
                bower + '/fontawesome/fonts/*',
                bower + '/bootstrap/fonts/*'
            ],
            dest: dest + '/fonts'
        }
    }
};