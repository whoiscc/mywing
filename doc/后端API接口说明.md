默认的行为模式遵循设计规范中的描述。非必要项在缺失时，字段仍然保留，对应值为`null`。

## 账户模块

`GET /angel`

获取用户信息。请求参数：

* `id_list`列表，查询的用户ID
* `token`

返回一个列表，其中每一项为：

* `id`用户ID
* `nickname`用户昵称
* `distribution`用户捐赠总额（浮点数）
* `imToken`用于即时通讯的token

----

`POST /angel/login~debug`

调试版本的用户登录。请求参数：

* `ticket`登录凭证，该接口所支持的调试凭证有：
  * `debug-ticket-create-angel`创建一个新的账户

返回：

* `created`是否为新创建的用户（布尔值）
* `token`登录令牌，在请求其他接口时使用
* `angel`当前登录的账户信息，其字段与`GET /angel`返回的列表项一致

----

`POST /angel/logout`

登出当前账户。请求参数：

* `token`

返回空数据。

## 任务模块

`GET /task`

获取任务信息。请求参数：

* `id_list`列表，查询的任务ID
* `token`

返回一个列表，其中每一项为

* `id`
* `description`任务描述
* `srcLongitude` `srcLatitude`出发地坐标（非必要）
* `dstLongitude` `dstLatitude`目的地坐标（非必要）
* `cost`任务价值（浮点数）
* `distribution`捐赠金额（浮点数）
* `status`任务状态，其值为
  * `0`已发起，未被接下
  * `1`已被接下，未完成
  * `2`已被完成，未确认
  * `3`已确认完成（完成者已获得奖励）
  * `-1`已发起并被取消，未被接下
  * `-2`已被接下并被取消（只能由发起者取消）
  * `-3`完成者认为已完成，但与发起者达成一致取消任务
  * 其它，错误或未知情况
* `owner` 发起者ID
* `helper` 完成者ID（非必要）
* `createdAt` 发起时间（时间戳，下同）
* `acceptedAt` `finishedAt` `confirmedAt` 被接下、被完成和确认完成的时间（非必要）
* `canceledAt` 被取消的时间（非必要）

以下接口中，与上述字段同名的参数，具有相同的含义。

----

`POST /task/create`

以当前登录用户为拥有者，创建一个任务，请求参数

* `description`
* `cost`
* `srcLongitude` `srcLatitude`（非必要）
* `dstLongitude` `dstLatitude` (非必要)
* `token`

返回字段与`GET /task`返回的列表项一致。

----

`POST /task/accept`

以当前登录用户为完成者，接下一个任务，请求参数

* `id`任务ID
* `distribution`
* `token`

返回字段同上。

----

`POST /task/finish`

以当前登录用户为完成者，完成一个任务（只能完成自己接下的任务），请求参数

* `id`任务ID
* `token`

返回字段同上。

----

`POST /task/confirm`

以当前登录用户为发起者，确认完成一个任务（只能确认自己发起的任务），请求参数

* `id`任务ID
* `token`

返回字段同上。

----

`POST /task/cancel`

以当前登录用户为发起者，取消一个任务（只能取消自己发起的任务），请求参数

* `id`任务ID
* `token`

----

`GET /task/available`

获取可以被接下的任务列表，请求参数

* `srcLatitude` `srcLongitude` `dstLatitude` `dstLongitude`（非必须）
* `max`返回任务个数最大值
* `reset`是否重置（布尔值）。不重置时，每次请求返回任务集合均不相交，重置后后端将「遗忘」之前返回过的任务集合。
* `token`

返回一个列表，其中每一项与`GET /task`字段相同。

----

`GET /task/self`

获取当前用户参与过的所有任务，请求参数

* `inProgress`是否只包含正在进行中（没有被确认完成或取消）的任务（布尔值）
* `token`

返回一个列表，其中每一项与`GET /task`字段相同。

## 公共信息模块

> 以下所有接口均需要`token`参数

`GET /info/board/<board_id>`

获取排行榜数据。`<board_id>`为排行榜ID，另作规定。

返回字段：
* `angels` 上榜用户列表。列表中的每一项为一个用户，拥有`id`、`nickname`和`value`字段。`id`和`nickname`含义同上，`value`为排行榜相关的数据。
* `updateAt` 排行榜更新时间（UNIX时间戳）

`GET /info/news`

`GET /info/news/<news_id>`

获取所有新闻列表和某一条新闻的详细信息。一条新闻包含以下字段：

* `id`
* `title`
* `author`
* `updatedAt`
* `content`

获取新闻列表的接口返回一列新闻，列表的每一项只包含前四个字段。

（另外，`GET /info/board`和`GET /info/news`也可以以类似于`GET /angel`的方式，使用`id_list`参数进行调用。）
