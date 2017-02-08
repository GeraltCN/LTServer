# 1. 请求格式



## 1.1 用户登陆
### 1.1.1 接口调用请求说明

|      |         |
| ------------- |:-------------:|
| 协议      | http |
|请求方式|GET|
| 请求 Url      | http:/127.0.0.1:5000/user_login?username=USERNAME&password=Password      |
| GET数据 | token: String, result: 1/0      |

### 1.1.2 请求参数说明

| 参数        | 是否必须           | 说明  |
|: -------------: |:-------------:| :-----:|
| username      | 是 | 用户名，明文 |
| password      | 是 |   用户密码，加密 |




## 1.2 用户注册
###1.2.1 接口调用请求说明

|       |            |
| ------------- |:-------------:|
| 协议      | http |
|请求方式|GET|
| 请求 Url      | http:/127.0.0.1:5000/user_register?username=USERNAME&password=PASSWORD      |
| GET数据 |  result: 1/0      |

###1.2.2 请求参数说明

| 参数        | 是否必须           | 说明  |
|: -------------: |:-------------:| :-----:|
| token      | 是 | 由服务器发放，有效期7天 |


## 1.3 用户获取信息

###1.3.1 接口调用请求说明

| 参数        | 是否必须           | 说明  |
|: -------------: |:-------------:| :-----:|
| token      | 是 | 由服务器发放，有效期7天 |


###1.3.2 请求参数说明

| 参数        | 是否必须           | 说明  |
|: -------------: |:-------------:| :-----:|
| token      | 是 | 由服务器发放，有效期7天 |


## 1.4 更新用户信息
###1.4.1 接口调用请求说明

|       |            |
| ------------- |:-------------:|
| 协议      | http |
|请求方式|GET|
| 请求 Url      | http:/127.0.0.1:5000/get_user_info?token=TOKEN&content={'column1':'sth1','column2':'sth2}      |
| GET数据 | result: 1/0|


###1.4.2 请求参数说明


| 参数        | 是否必须           | 说明  |
|: -------------: |:-------------:| :-----:|
| token      | 是 | 服务器发放的token，有效期 7天 |
|content|是|所包含需要更新的内容的json数字，key与数据库一致|