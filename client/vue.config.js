//

const path = require('path');
const webpack = require('webpack')

module.exports = {
  outputDir: path.resolve(__dirname, './www'),
  publicPath: './',
  configureWebpack: {
    watchOptions: {
      ignored: /platforms|node_modules|package\.json/,
    },
  },
};
