`lib/im.js`对第三方IM服务进行了封装，目前采用的IM服务商为GoBelieve，该封装库有待完善。

```js
import Im from 'lib/im'
```

----

```js
const im = new Im(angel, onMessage)
```

创建一个新的服务实例。每个实例应该与一位登录用户对应。如果在实例创建之前有信息发给该用户，则这些信息将在该实例被创建以后立即被送达而不会丢失。但是这个实例也不应该在聊天见面位于前台时再创建，而是应当尽早创建，由App负责对用户收到信息的暂存工作。

参数`angel`为网络请求库中登陆后返回的对象。参数`onMessage`将在用户每次收到消息时被调用，调用参数为一个字典，具有以下字段：
* `id` 发送者的ID。可以使用此ID和`GET /angel`接口获取发送者资料
* `message` 消息内容

```js
im.start()
im.stop()
```

激活和关闭一个服务实例。只有在实例被激活期间才能收发消息。通常来说应该在实例被创建以后尽早激活。

```js
im.send(message, receiver)
```

发送消息。`message`为消息内容，`receiver`为接受者的angel对象。
