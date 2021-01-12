const withPlugins = require('next-compose-plugins');
const withSass = require('@zeit/next-sass')
const withCSS = require('@zeit/next-css')
const optimizedImages = require('next-optimized-images');

module.exports = withPlugins(
    [
        [withCSS, {}],
        [withSass, {}],
        [optimizedImages, {}]
    ]
)