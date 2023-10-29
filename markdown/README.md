# markdown学习

写在前面：本文件是我于2023.08.11的markdown学习笔记。<br>

学习资料来源：[markdown官网](https://markdown.com.cn)

学习工具：[typora官网](https://typoraio.cn/)

## 1：标题

markdown中有六级标题，可根据需要自行定义

a:typora编辑中，可使用ctrl+1,2,3,4,5,6快捷键来定义各级标题

b:源码模式中可使用如下语法进行定义

```markdown
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题
```

**注意不同的 Markdown 应用程序处理 `#` 和标题之间的空格方式并不一致。为了兼容考虑，请用一个空格在 `#` 和标题之间进行分隔。**

c:特殊的一级和二级标题：

源码模式中，可在文字的下方分别添加任意数量的=，-来定义一级和二级标题
```markdown
一级标题（一个=）
=

一级标题（多个====）
=========

二级标题（一个-）
-

二级标题（多个------）
----------------------

```


## 2：段落

:one::两个空格
```markdown
我要在这行之后创建段落(在我输入完成之后，在末尾添加两个空格)  
```
eg:我要在这行之后创建段落(在我输入完成之后，在末尾添加两个空格)  
:two::单行或者多行空白行

```markdown
这是第一段

这是第二段

这是第三段
```
这是第一段

这是第二段

这是第三段

:three::"\<br>"

第一段<br>第二段<br>第三段<br>:warning:在源码模式中，你可以想这样输入

```markdown
第一段<br>第二段<br>第三段
```

:warning:在typora快捷键编辑模式中，使用之后会自动帮助你换行

:x:不要用空格（spaces）或制表符（ tabs）缩进段落。

:cactus:markdown中有很多表情(emoji :smile:)，在快捷键模式下，你只需要在键盘英文的模式下输入冒号，然后输入你想要的符号的简称
如：:ice_skate:
:ice_cream:
:sun_with_face:
:moon:
:one:(:one:)
:two:(\:two:)
:three:(\:three:)
:heart:（\:heart:）

## 3：强调

:one::粗体（bold）使用“\** 需要加粗的文本**”或者“\__需要加粗的文本__”

```markdown
**我被加粗了**
__我也被加粗了__
```
**在typora快捷键模式和源码模式下都适用！**
:exclamation:：使用下划线加粗时，总共需要在英文输入模式下的4根下划线

_ _ 这样_ _，但是下划线需要连接在一起才能实现加粗

:exclamation::单词中加粗尽量要使用“\**星号**”而不使用“\__下划线__”

```markdown
 iloveyou
i**love**you 
i__love__you
```

（Markdown 应用程序在如何处理单词或短语中间的下划线上并不一致。为兼容考虑，在单词或短语中间部分加粗的话，请使用星号）

:two::斜体（Italic）使用“\* 需要变斜的文本*”或者“\_需要变斜的文本_”

```markdown
*我变斜了*
_我也是_
```

:exclamation::同样的，单词中斜体尽量要使用“\*星号*”而不使用“\_下划线_”

:three::斜体:heavy_plus_sign:粗体（bold and italic）使用“\***需要加粗的文本***”或者“ \___需要加粗的文本___”

```markdown
***我被变得粗和斜***
___我也是___
三个*** ***
三个___ ___
```

:exclamation::同样的，单词中斜体+粗体尽量要使用“星号”而不使用“下划线”

## 4：引用

:one:：使用一个\>

> 欲买桂花同载酒，终不似，少年游！

:two::使用多个\>

> 1:
>
> 2:
>
> 
>
> 
>
> n:

:three::带其他引用
>欲买桂花同载酒，终不似，**少年游！**
>
>- 深山踏红叶，耳畔闻鹿鸣
>- 

## 5：列表

1. 有序列表（在快捷键模式下使用1.空格）
   如同标题5下的目录一般

   ```markdown
   1. 源码模式也适用
   2. typora快捷键模式同样适用
   ```

2. 使用（快捷键模式和源码下-，*，+，然后空格）

   - -

     ```markdown
     - 
     - 
     - 
     ```

   - *

     ```markdown
     * 
     * 
     * 
     ```

     

     

   - +

     ```markdown
     + 
     + 
     + 
     ```

3. 嵌套

   - 代码（两个tab或者八个空格，快捷键模式下使用```）

     ```text
             <html>
               <head>
                 <title>Test</title>
               </head>
     ```

     ```la
     MID=max2-max1
     MIQ=max1/max1
     ```

     ```python
     print("hello,world!")
     ```

   

   - 图片
     ![无须嵌套的图片](pics/2052225.jpg "壁纸")

     

     

     
     
- 引用
  
  > *Nothing is* **perfect!**

## 6：代码语法

1. 密令或单词
   - 我们需要使用 `echo "print('hello,world!')" >> test.py` 在test.py中添加文件
   - `su - root`

2. 
   转义反引号

   ``Use `code` in your Markdown file.``

   ```markdown
   ``Use `code` in your Markdown file.`
   ```

3. 代码块

   在快捷键模式下我们直接使用```，然后根据typora的提醒创建代码块

   ````markdown
   ```markdown
   
   ```
   ````

## 7:分隔线

1. 三个或者多个*
   ***

   上面的线用三个\*，下面线多个\*

   ********************************

   

2. 三个或者多个-

   

   ---

   上面的线用三个\-，下面线多个\_

   --------

   

3. 三个或者多个_

   


___

   上面的线用三个\_，下面线多个\_


____________

   

   :exclamation:为了兼容性，请在分隔线的前后均添加空白行。<br>

   例如
   ---

   我们直接在例如下面添加---就会让其变成二级标题，而不会生成分割线

## 8:链接

1. 普通连接(\[超链接显示名](超链接地址 "超链接title"))

   这是我的个人网页[It's Justin Here!](https://justin-12138.github.io/ "myweb")

   :exclamation:链接title是当鼠标悬停在链接上时会出现的文字，这个title是可选的，它放在圆括号中链接地址后面，跟链接地址之间以空格分隔。"my own website"会显示，当你将鼠标停在我的个人连接。
   :exclamation::当你直接点击的时候，不会跳转，需要ctrl+鼠标左键

   

2. 网址和Email
   使用尖括号可以很方便地把URL或者email地址变成可点击的链接。
   如下
   <https://justin-12138.github.io/>

   <fake@example.com>

   :exclamation::同样需要ctrl+鼠标左键
   
3. 格式化连接：
   这是我的个人网页(加粗版)**[It's Justin Here!](https://justin-12138.github.io/)**<br>

   将链接变代码：[`code`](https://justin-12138.github.io/)

   :exclamation::需要在方括号中添加反引号。

4. 

## 9:图片

1. 普通图片使用!+[alt]+(连接 title)

   ![pic](pics/2052225.jpg "壁纸")

2. 这是一个图片连接(ctrl+鼠标左键)

   [![](pics/IMG_5211.JPG)](https://justin-12138.github.io/ "myweb")

## 10：转义字符语法

1. 要显示原本用于格式化 Markdown 文档的字符，请在字符前面添加反斜杠字符 \ 
   ```markdown
   \# 这不是标题
   # 这是标题
   \*none italic 
   *italic
   ```

2. 可转义的字符

   | **Character** |
   | :-----------: |
   |       \       |
   |       `       |
   |       *       |
   |       _       |
   |      {}       |
   |      []       |
   |      ()       |
   |       #       |
   |       +       |

3. 特殊字符自动转义（&和<）
   不同于html，markdown允许我们直接使用这两个符号
   
   - Justin&Julie
   - 4<5
   
   详细解释请参照：[特殊字符自动转义](https://markdown.com.cn/basic-syntax/escaping-characters.html)

## 11：内嵌html

1. 行级內联标签
   HTML 的行级內联标签如 `<span>`、`<cite>`、`<del>` 不受限制，可以在 Markdown 的段落、列表或是标题里任意使用。依照个人习惯，甚至可以不用 Markdown 格式，而采用 HTML 标签来格式化。

   This **word** is bold.This <em>word</em> is italic.

   ```markdown
   This **word** is bold. This <em>word</em> is italic.
   ```

   这是一张图片：<img src="pics/IMG_5211.JPG"  alt="实例" height=180 width=600/>

   ```html
   <img src="pics/IMG_5211.JPG"  alt="实例" height=180 width=600 />
   ```

2. 区块标签
   ```tex
   区块元素──比如 <div>、<table>、<pre>、<p> 等标签，必须在前后加上空行，以便于内容区分。而且这些元素的开始与结尾标签，不可以用 tab 或是空白来缩进。Markdown 会自动识别这区块元素，避免在区块标签前后加上没有必要的 <p> 标签。
   ```

   This is a regular paragraph.

   <table>
       <tr>
           <td>Foo</td>
       </tr>
   </table>

   This is another regular paragraph.

   

   
