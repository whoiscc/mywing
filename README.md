# ~~某个始终无法定下来名字的公益App~~

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
    * `src` 业务逻辑
      * `assets` 参与Webpack构建的资源文件
      * `components` Vue单文件组件
    * `lib` 接入第三方服务的封装库
      * `request.js` AJAX请求API
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

将`${IP}`替换为开发环境的外部IP，以方便运行在Android/iOS模拟器中的前端应用访问后端API。

----

构建前端应用前，先将`client/src/main.js`中

```js
request.set({
  // ...
})
```

配置表中的`base`设置为后端服务器运行的`${IP}`。

```
$ npm install --global cordova
$ cd client
$ npm install
$ npm run build -- --watch
# 再打开一个终端
$ cordova run browser --port=8080 -- --live-reload
```

## 开发规范（适度遵循）

所有文件名用英文，注释和文档尽量用中文，但是所有变量名必须为英文单词，注释和文档中出现的术语必须有明确的英文单词对应。提交Git仓库时的注释不要在末尾加标点符号，如果用英文则首字母大写。

所有Vue单文件组件的文件名用首字母大写的驼峰命名，`lib`文件夹下的封装库文件用连词符连接的小写字母命名。其余文件命名与同路径下已有文件命名风格保持一致。

永远不向`master`分支提交代码，以功能特性/漏洞修复为单位创建分支，工作完成后向`master`分支发起合并请求。确保`master`分支上的每一个提交都可以作为发布版本提供给终端用户，其中真正发布的版本会被打上附注标签（`git tag -a`）。分支的命名格式为`xxx-[bug-]some-short-description`，其中`xxx`为负责该分支的开发者代号，漏洞修复的分支带有`bug-`修饰。
