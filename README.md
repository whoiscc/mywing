<h1 style="text-align: center; font-family: cursive">某个始终无法定下来名字的公益App</h1>

## 项目结构

* `mywing`
  * `server` 后端子项目（Django）
    * `mywing`
      * `settings.py` 全局配置（适用于开发环境）
      * `urls.py` API路由配置
    * `angel` 账号模块
    * `task` 任务模块
    * `info` 公共信息模块
  * `client` 前端子项目（Vue + Cordova）
    * `src` Vue组件，业务逻辑
      * `assets` 参与Webpack构建的资源文件
    * `lib` 接入第三方服务的封装库
    * `public` 不参与Webpack构建的资源文件
    * `res` 原生应用相关的资源文件

## 搭建开发环境

搭建后端环境：

```
$ pip3 install django django-cors-header
$ cd server
$ python3 manage.py migrate
$ python3 manage.py runserver ${IP}:8000
```

将`${IP}`替换为开发环境的子网IP，以方便运行在Android/iOS模拟器中的前端应用访问后端API。

----

构建前端应用

```
$ npm install --global cordova
$ cd client
$ npm install
$ npm run build -- --watch
# 再打开一个终端
$ cordova run browser --port=8080 -- --live-reload
```
