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
                bower + '/ng-table/dist/ng-table.css',
                bower + '/bootstrap/dist/css/bootstrap.css'
            ],
            dest: dest + '/css'
        },
        js: {
            src: [
                bower + '/angular/angular.js',
                bower + '/angular-ui-router/release/angular-ui-router.js',
                bower + '/ng-table/dist/ng-table.js'
                //bower + '/angular-smart-table/dist/smart-table.js'
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