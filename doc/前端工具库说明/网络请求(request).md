`lib/request.js`包含调用后端接口所需要的方法。后端接口理论上可以使用任何方法发起的网络请求进行调用，但是使用该库可以大幅减轻工作量。

该库使用了cordova模拟的HTML5 File API，因此必须在cordova环境下运行。

```js
import request from 'lib/request';
```

----

`request.set(config)`方法进行全局设置，参数`config`为字典，每个字段对应一个配置项。目前支持的配置有：
* `base`后端的根URL。对于本地服务器该值应为`http://localhost:<port>`，其中`<port>`为服务器监听的端口。

`request.login(ticket, debug = false)`登录用户账户。`ticket`参数为登录票据，应该通过CAS登录服务接口取得，或者指定为某个调试登录接口所接受的票据，此时`debug`参数应置为`true`。该接口返回一个Promise对象，内容同后端API说明中的`POST /angel/login`或`POST /angel/login~debug`。

`request.logout()`注销当前登录的用户。返回一个Promise对象，值为空。若当前没有登录则抛出异常。

`request.get(path, payload)`和`request.post(path, payload)`分别调用后端`GET`和`POST`方法的接口，必须在使用`login`成功登陆后才能调用，否则抛出异常。`path`为接口路径，`payload`为接口参数，如调用获取一组用户信息的接口：

```js
request.get('/angel', {'id_list': [1, 2, 3, 4]}).then(angels => {
  // do something with `angels`...
});
```

