//

const path = require('path');
const webpack = require('webpack')

module.exports = {
  outputDir: path.resolve(__dirname, './www'),
  baseUrl: './',
  configureWebpack: {
    watchOptions: {
      ignored: /platforms|node_modules|package\.json/,
    },
  },
};
