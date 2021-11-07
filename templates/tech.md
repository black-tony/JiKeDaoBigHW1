



#### 对多人项目的建议

每天在自己的分支上commit, 可以commit若干次

每天写代码之前push(和别人的代码合并)
,合并到分支`dev`中

例如:

> `Yang`->`dev`
> 
> `Zhang`->`dev`

如果有冲突文件, 自己和文件所有者联系调解

每天写项目之前让自己的branch和`dev`保持一致, 方便别人合并代码啥的

每天晚上(不要太晚) pull(把别人今天的内容下载到电脑上)


在完成一定的功能之后, 再将`dev`合并到`main`中







## 可能会有用到的内容

### 前端传递参数到后端:

#### 方法1
使用post方法 从form中读取数据
```html
<form action="url" method="post">
        <input name="varName">
```
url写的是表单要交到哪一个位置(后端在哪里处理数据)

method要写post

input中`name`属性是变量名, **必须要写这个**, 否则后端获取数据比较麻烦

~~**在一个页面中有多个form时, 需要指定form的name加以区分**~~

在一个页面有多个form时, 需要使用方法2 或者 (action填写不同的url). form的name必须指定以方便电脑区分

#### 方法2
使用socket.emit方法

同样是用form

1. 给form一个id
2. 在html文件中插入如下内容:
```html

<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js" integrity="sha512-bLT0Qm9VnAYZDflyKcBaQ2gg0hSYNQrJ8RilYldYQ1FxQYoCLtUjuuRuZo+fjqhx/qtq/1itJ0C2ejDxltZVFg==" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/3.0.4/socket.io.js" integrity="sha512-aMGMvNYu8Ue4G+fHa359jcPb1u+ytAF+P2SCb+PxrjCdO3n3ZTxJ30zuH39rimUggmTwmh2u7wvQsDTHESnmfQ==" crossorigin="anonymous"></script>
<script type="text/javascript" charset="utf-8">
$(document).ready(function() {
    var socket = io();
    $('form#表单的ID').submit(function(event) {
        socket.emit('这里写下对这个事件的命名', 
        {
            提交回服务端的变量名1: 变量1的内容,
            .........变量名2: 变量2的内容,
            //可以使用$('元件类型(可省略)#元件ID').val()的形式获取内容
            //可以有0个或若干个变量, 对事件的命名是必须的
        });
        return false;
    });
}
</script>

```
### 在不需要换网页实时进行数据传递的方法


使用socket.on方法

1. 在html文件中插入如下内容(重复内容只需要插入一次):
```html

<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js" integrity="sha512-bLT0Qm9VnAYZDflyKcBaQ2gg0hSYNQrJ8RilYldYQ1FxQYoCLtUjuuRuZo+fjqhx/qtq/1itJ0C2ejDxltZVFg==" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/3.0.4/socket.io.js" integrity="sha512-aMGMvNYu8Ue4G+fHa359jcPb1u+ytAF+P2SCb+PxrjCdO3n3ZTxJ30zuH39rimUggmTwmh2u7wvQsDTHESnmfQ==" crossorigin="anonymous"></script>
<script type="text/javascript" charset="utf-8">
$(document).ready(function() {
    var socket = io();
    //这之前都是重复内容
    
    
    socket.on(”事件名“, function(data, callback) {
        使用data.变量名 方法访问服务器端传来的数据
        也可以在这里socket.emit(参数见上文), 再向服务器发送一条消息
        if(callback)//回调函数, 暂时不知道有啥用(
            callback(函数参数);
    });
}
</script>

```
**对实时通信的socket功能还不太了解的话, 可以看在/TonyTestFile/test_socket.py和/TonyTestFile/templates/socket_html.html来进一步看源代码**


### html中使用传递的变量的方法

`{{变量名|过滤器(参数)}}`

变量名: 我趋向于驼峰命名法

例如: `getName` `getVar`

下划线命名法我也能接受

例如: `get_name` `get_var`

1. 不建议两种命名法混用
2. 不建议在下划线命名法中使用大写字母

过滤器:
`capitalize` 首字符变大写,其他变小写

`lower` 将值转换为小写

`upper` 将值转换为大写

`title` 将值中的每个单词首字符变大写

`trim` 去掉值两端的空格

`default(‘xx’)` 如果变量不存在,将采用default中的值作为默认输出

`truncate(num[,bool])` 截取指定长度字符串,后面使用…显示

使用示例: `{{userName | trim}}`

#### 在这里写下html文件和对应需要的参数
例如 <font color = red>仅仅是例子!</font>

-----
`login.html` 
1. `title` 标题
2. `userName` 数据库中的用户名
3. `userPswd` 数据库中对应的密码
--------
在这里仿照上面的格式写下你的需求

----------------
-------------
建议看一下模板文件, `{% extends 'layout.html' %}`可以引用公共文件, 可以将通用的部分写到公共文件里, 减少代码的复制粘贴
