const path = require('path')
const CopyWebpackPlugin = require('copy-webpack-plugin')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const scopeName = JSON.stringify(require('./package.json').name)
// 是否为开发模式
const isDevMode = process.env.NODE_ENV === 'development'
// 设置URL
const requestHost = '192.168.20.127:9016'
const serviceUrl = isDevMode
  ? { // so on dev we'll have
    http_base_url: JSON.stringify(`http://${requestHost}`),
    websocket_base_url: JSON.stringify(`ws://${requestHost}/monitor/websocket_url`)
  }
  : { // and on build (production):
    http_base_url: '"http://" + location.host',
    websocket_base_url: '"ws://" + location.host + location.pathname + "websocket_url"'
  }
const compileMode = process.argv[process.argv.length - 1].substr(2) // 编译模式: dev app lib
// 定义全局变量
const envObj = Object.assign(serviceUrl, {
  APP_SCOPE_NAME: scopeName, // app作用域
  VUE_ROUTER_MODE: JSON.stringify('hash'),
  VUE_ROUTER_BASE: JSON.stringify('/'),
  COMPILE_MODE: JSON.stringify(compileMode)
})

module.exports = {
  // publicPath: !isDevMode ? scopeName : '/',
  outputDir: 'dist',
  productionSourceMap: false,
  css: {
    extract: false
  },
  indexPath: '/index.html',
  configureWebpack: (config) => {
    const alias = config.resolve.alias
    Object.assign(alias, {
      'http': path.resolve(__dirname, './src/api/http'),
      'components': path.resolve(__dirname, './src/components'),
      'assets': path.resolve(__dirname, './src/assets')
    })

    config.externals = {
      'vue': 'Vue',
      'vuex': 'Vuex',
      'vue-router': 'VueRouter'
    }

    config.plugins.push(
      new CopyWebpackPlugin([
          {
            from: path.resolve(__dirname, 'public'),
            ignore: ['.*']
          }
      ])
    )

    config.plugins.push(
      new HtmlWebpackPlugin({
        template: 'public/index.html'
      })
    )
  },
  chainWebpack: (config) => {

    // 'src/lib' 目录下为外部库文件，不参与 eslint 检测
    config.module
      .rule('eslint')
      .exclude
      .add('/')
      .end()

      config.plugin('define').tap(args => {
        const processEnv = args[0]['process.env']
        Object.assign(processEnv, envObj)
        return args
      })

      config.plugins.delete('demo-html')

  },

  // All options for webpack-dev-server are supported
  // https://webpack.js.org/configuration/dev-server/
  devServer: {
    host: '0.0.0.0',
    port: 8080,
    open: true,
    watchOptions: {
      poll: true
    }
  },
  // 构建时开启多进程处理 babel 编译
  parallel: require('os').cpus().length > 1,

  // https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-pwa
  pwa: {},

  // 第三方插件配置
  pluginOptions: {
    quasar: {
      theme: 'mat',
      rtlSupport: true,
      importAll: true
    }
  },
  transpileDependencies: [
    /[\\\/]node_modules[\\\/]quasar-framework[\\\/]/
  ]
}

