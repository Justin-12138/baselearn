# GNU/LINUX

## 1.写在前面

:100:: 这是本人于2023.08.01在bilibil开始学习Linux操作系统的学习笔记
:penguin:本人所用的操作系统:`uname -a`

```tex
Linux justin-labtop 6.2.0-26-generic #26~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Jul 13 16:27:29 UTC 2 x86_64 x86_64 x86_64 GNU/Linux
```

:book::本人在学习课程之前对GNU/Linux操作的了解

- 操作系统的发展历史
  [Unix_to Gnu/Linux](https://www.bilibili.com/video/BV1Mv4y127wA/?spm_id_from=333.880.my_history.page.click&vd_source=233482ad6c5a629ccdd3bf05f2c6ed41 "Unix to Gnu/Linux") :exclamation::(强烈推荐观看！)

- 会一些简单操作密令<br>

  ```tex
  ls # 列出当前目录下的文件
  cd # 进入某文件夹
  sudo apt-get update && sudo apt-get upgrade 
  ......
  ```

- 安装过的软件及服务

  - Hadoop+Spark(大数据课程所学)
  - Nginx(个人网站，但是服务器太贵，还是白嫖github吧)
    我的:spider_web:: [My web](https://justin-12138.github.io/ "Justin")
  - Mysql(数据库系统所学)
  - Genshin Impact Launch！(自学)
    1. 安装wine
    2. 安装vulkan
    3. 安装dxvk
    4. 打补丁
    5. 原神！启动！
    6. ......已经退坑！(深渊已满星，出过双金!)
  - ......还有些忘记了

- 为什么学习Linux:heart:

  - 刚开始是想深度学习加速，但是后面才发现还是需要特定的卡才能加速
  - 入坑之后折腾了很多服务端:computer:的东西，数据库，nginx，但是都是浅尝辄止
  - Linux总给我一种很优雅的，很干净的感觉，而且很稳定(哈哈哈):star2:
  - 技多不压身～！:skier:主要是还想从事运维的一些工作，不想卷开发!!!:cactus:

## 2.Linux简介以及如何安装Linux

:one::Linux 还是 GNU/Linux？

- 关于这个问题可以去观看一个视频，讲了从mutics到Linux的很长一段历史,很有意义！

  [Unix_to Gnu/Linux](https://www.bilibili.com/video/BV1Mv4y127wA/?spm_id_from=333.880.my_history.page.click&vd_source=233482ad6c5a629ccdd3bf05f2c6ed41 "Unix to Gnu/Linux") :heart_decoration:

:two::如何安装Linux
在Linux中学习Linux！

- 虚拟机

  常用的的虚拟机软件有[VirtualBox](https://www.virtualbox.org/wiki/Downloads)，VMWare
  本教程的安装使用VirtualBox演示，如有需要，小伙伴们也可以根据网上教程使用VMWare安装。

  1. 下载并安装virtualbox
     我这边使用的是https://www.virtualbox.org/wiki/Download_Old_Builds_6_1

     ​         6.1.40（教程使用为：windows hosts），小伙伴们可以根据自己的操作系统进行选择。
     <img src="pics\installation\ins\image-20230813135244431.png" alt="image-20230813135244431" style="zoom: 33%;" />

     双击下载完成的.exe安装:

<img src="pics\installation\ins\image-20230813140458186.png" alt="image-20230813140458186" style="zoom: 33%;" />

<img src="pics\installation\ins\image-20230813140534553.png" alt="image-20230813140534553" style="zoom: 33%;" />

1. 下载Ubuntu iso文件
   本人学习过程中使用的为ubuntu 18.04
   大家可以根据自己的需要安装不通的版本

[ubuntu阿里云](http://mirrors.aliyun.com/oldubuntu-releases/releases/?spm=a2c6h.25603864.0.0.5ee66f0fOBy7kn "Ubuntu阿里云镜像源")
<img src="pics\installation\ins\image-20230813135918856.png" alt="image-20230813135918856" style="zoom: 25%;" />

点击新建：并配置文件所在目录
名称：自己取（英文）
文件夹：选择有足够空间的文件夹
类型：Linux
版本Ubuntu64位



<img src="pics\installation\ins\image-20230813140821651.png" style="zoom:33%;" />

内存大小一般可设置为3G或者4G



<img src="pics\installation\ins\image-20230813140927610.png" alt="image-20230813140927610" style="zoom: 50%;" />
后面的操作基本就是下一步：

<img src="pics\installation\ins\image-20230813141003333.png" alt="image-20230813141003333" style="zoom: 50%;" />
下一步

<img src="pics\installation\ins\image-20230813141020403.png" alt="image-20230813141020403" style="zoom: 50%;" />
:warning::动态分配！

<img src="pics\installation\ins\image-20230813141033414.png" alt="image-20230813141033414" style="zoom: 50%;" />

一般设置为20G，基本够用了

<img src="pics\installation\ins\image-20230813141056309.png" alt="image-20230813141056309" style="zoom: 50%;" />
启动！

<img src="pics\installation\ins\image-20230813141117125.png" alt="image-20230813141117125" style="zoom: 33%;" />
选择一个虚拟光盘文件

<img src="pics\installation\ins\image-20230813141157590.png" alt="image-20230813141157590" style="zoom:50%;" />

选择下载好的iso文件

<img src="pics\installation\ins\image-20230813141228907.png" alt="image-20230813141228907" style="zoom: 33%;" />

选择

<img src="pics\installation\ins\image-20230813141302172.png" alt="image-20230813141302172" style="zoom: 33%;" />
启动！

<img src="pics\installation\ins\image-20230813141316200.png" alt="image-20230813141316200" style="zoom:50%;" />

中文简体+安装ubuntu

<img src="pics\installation\ins\image-20230813141624788.png" alt="image-20230813141624788" style="zoom:50%;" />

汉语

<img src="pics\installation\ins\image-20230813141654299.png" alt="image-20230813141654299" style="zoom:50%;" />

最小安装！

<img src="pics\installation\ins\image-20230813141757260.png" alt="image-20230813141757260" style="zoom:50%;" />

现在安装

<img src="pics\installation\ins\image-20230813141830739.png" alt="image-20230813141830739" style="zoom:50%;" />

继续

<img src="pics\installation\ins\image-20230813141854922.png" alt="image-20230813141854922" style="zoom:50%;" />

设置位置时区

<img src="pics\installation\ins\image-20230813141919407.png" alt="image-20230813141919407" style="zoom:50%;" />

创建用户密码

<img src="pics\installation\ins\image-20230813142004619.png" alt="image-20230813142004619" style="zoom:50%;" />

等待安装

<img src="pics\installation\ins\image-20230813142018983.png" alt="image-20230813142018983" style="zoom:50%;" />

安装完成，重启！

<img src="pics\installation\ins\image-20230813142907632.png" alt="image-20230813142907632" style="zoom: 50%;" />

输入密码登录账户

<img src="pics\installation\ins\image-20230813143016923.png" alt="image-20230813143016923" style="zoom:50%;" />

不升级
<img src="pics\installation\ins\image-20230813143422911.png" alt="image-20230813143422911" style="zoom:50%;" />
稍后提醒
<img src="pics\installation\ins\image-20230813143520039.png" alt="image-20230813143520039" style="zoom:50%;" />

鼠标右键打开终端或者ctrl+alt+t

<img src="pics\installation\ins\image-20230813143627397.png" alt="image-20230813143627397" style="zoom:50%;" />

输入`uname -a`,即可看到我们的版本信息

<img src="pics\installation\ins\image-20230813143721885.png" alt="image-20230813143721885" style="zoom:50%;" />

设备:soon::安装增强功能

<img src="pics\installation\ins\image-20230813143835598.png" alt="image-20230813143835598" style="zoom:50%;" />

运行！

<img src="pics\installation\ins\image-20230813144047231.png" alt="image-20230813144047231" style="zoom:50%;" />

按下回车

<img src="pics\installation\ins\image-20230813144134476.png" alt="image-20230813144134476" style="zoom:50%;" />
此处提示我们需要安装gcc make perl
于是我们在终端中输入如下命令，并按下回车

```markdown
sudo apt-get update
sudo apt-get install gcc make perl
```

<img src="pics\installation\ins\image-20230813151911578.png" alt="image-20230813151911578" style="zoom:50%;" />

双击桌面的光盘图标文件，点击运行软件

<img src="pics\installation\ins\image-20230813152029768.png" alt="image-20230813152029768" style="zoom:50%;" />



打开终端输入`reboot` 重启
<img src="pics\installation\ins\image-20230813144242508.png" alt="image-20230813144242508" style="zoom:50%;" />


此时我们便可以调整我们的窗口大小

<img src="pics\installation\ins\image-20230813144435889.png" alt="image-20230813144435889" style="zoom:50%;" />



设置共享粘贴板双向
<img src="pics\installation\ins\image-20230813152308953.png" alt="image-20230813152308953" style="zoom:50%;" />

ok，我们的Ubuntu18.04在VirtualBox的安装就算完成啦！



- **双系统win基础安装ubuntu**
  

  0. 在已有的windows下去安装Linux，操作也很简单，Ubuntu安装基本也是下一步，下一步......

  我的双系统如下，本着认真负责的态度，我再给大家介绍一下如何在windows的基础上去安装ubuntu22.04Lts
  <img src="pics\installation\ins\image-20230813152809103.png" alt="image-20230813152809103" style="zoom:50%;" />

  使用DiskGenius删除我原来的Ubuntu22.04lts，右键开始找到磁盘管理，自行准备大概100G或者150G或者根据你自己的需求进行划分，我这里就是用我未分配的空间（未分配需要你自己从原来的磁盘压缩，），网上大多数都是100G，大家可自行斟酌。

  <img src="pics\installation\ins\image-20230813172749748.png" alt="image-20230813172749748" style="zoom:50%;" />

  emmm还是说一下分盘的一些常识：
  从左往右:C,D,我们买来的新电脑经常会由厂商帮助我们分好盘，不过现在大家动不动就是1t，正常使用的情况，根本不用担心C盘爆满，而且盘符的读写速度会随着你从左往右下降，C盘的读写速度是最快的，但是一般来说感知不明显，但是你玩一些大型游戏放在移动硬盘和C盘应该就会有明显的感觉。<br>

  再次秉着认真负责的态度，我在这里再向大家展示如何去分盘(先把未分配的区域扩展到D盘)
  :exclamation:注意扩展只能相邻扩展，不能跨盘符扩展，比如我上面的156.57GB就不能直接扩展到C盘，只能扩展到D盘。


<img src="pics\installation\ins\image-20230813175310881.png" alt="image-20230813175310881" style="zoom:50%;" />

将之前的未分配区域扩展到D盘

<img src="pics\installation\ins\image-20230813180308341.png" alt="image-20230813180308341" style="zoom:50%;" />

右键D盘，点击压缩卷，

<img src="pics\installation\ins\image-20230813180753006.png" alt="image-20230813180753006" style="zoom:50%;" />

我们在这里压缩1024 x 150 = 153600MB，点击压缩

<img src="pics\installation\ins\image-20230813180930000.png" alt="image-20230813180930000" style="zoom:50%;" />

压缩完成：
<img src="pics\installation\ins\image-20230813181152999.png" alt="image-20230813181152999" style="zoom:50%;" />

1. 制作启动盘

   一个大小8G以上的U盘，16，32都行
   使用工具：[Rufus](https://rufus.ie/zh/)

   <img src="pics\installation\ins\image-20230813181436496.png" alt="image-20230813181436496" style="zoom:50%;" />

   先将空U盘插入电脑，Rufus下载完成后，直接双击启动镜像文件可以选择你下载好的镜像文件，我建议你使用22.04lts
   [Ubuntu22.04Lts](http://mirrors.aliyun.com/oldubuntu-releases/releases/22.04.1/?spm=a2c6h.25603864.0.0.41457ff3wmSZVM "ubuntu22.04")(阿里云下载)
   

<img src="pics\installation\ins\image-20230813203931260.png" alt="image-20230813203931260" style="zoom: 33%;" />

文件系统选择默认即可。然后点击开始，下面进度条显示完成之后我们就完成了启动盘的制作。







1. 

   

2. 

   

   

3. 

   

   

4. 

   

   

5. 

   

   

   

6. 
7. 
8. 



- 纯Linux

  

:three::

:four::









## 3.linux的目录结构

0. GUI和命令行

    - :computer::GUI（Graphics User Interface）图形用户界面
      简言之：就是你可以看到可视化的窗口，直观，如树形结构中的🌰

    - :scroll:CUI（Character user interface）字符用户界面
      简言之：就是你只有一个命令行，用多了也直观，如树形结构中的🌰

    - |    对比属性    |            GUI             |        CUI         |
      | :------------: | :------------------------: | :----------------: |
      |      交互      |    使用图形(图像、图标)    |  使用命令(仅文本)  |
      |      导航      |            容易            |        困难        |
      | 使用的外围设备 | 键盘和鼠标(或任何指点设备) |       仅键盘       |
      |      精度      |             低             |         高         |
      |      速度      |             低             |         高         |
      |    操作简单    |            简单            | 困难，需要专业知识 |
      |    所需内存    |             高             |         低         |
      |     灵活性     |           更灵活           |      一般灵活      |
      |   自定义外观   |        高度可自定义        |    外观无法更改    |

    Table source:[GUI&CUI](https://geek-docs.com/operating-system/os-ask-answer/whats-the-difference-between-gui-and-cui.html "GUI&CUI")
    🌰：
    GUI::framed_picture:
    <img src="pics/files/image-20230813001315495.png" alt="image-20230813001315495" style="zoom:25%;" />

    CUI::black_medium_square:
    <img src="pics/files/image-20230813001412011.png" alt="image-20230813001412011" style="zoom:50%;" />

    

1. **树形结构**

   可以看出我们的文件目录结构是一个”所谓“的树形结构
   即一个根目录`/`，然后根目录里面有子目录

   `usr`,`dev`,`opt`......

   :question::当你看到这里的时候，可能会有一些不知所措，这里面的文件都是什么？

   [![](pics/files/file_struct.jpeg)](https://cn.bing.com/images/search?view=detailV2&ccid=MG44P%2FUt&id=817701BE773A33A08EDE45C4830641F9B52A5538&thid=OIP-C.MG44P_Ut1K8z-DKuB40FbAHaEi&mediaurl=https%3A%2F%2Fts1.cn.mm.bing.net%2Fth%2Fid%2FR-C.306e383ff52dd4af33f832ae078d056c%3Frik%3DOFUqtflBBoPERQ%26riu%3Dhttp%253a%252f%252fstatic.oschina.net%252fuploads%252fimg%252f201407%252f13012401_WCtc.jpg%26ehk%3Df3lvuFPzO%252bSFhgi80TapEZJswe4Sa6fKA99Jb6X3n0w%253d%26risl%3D%26pid%3DImgRaw%26r%3D0&exph=456&expw=744&q=linux%e6%96%87%e4%bb%b6%e7%bb%93%e6%9e%84&simid=608024978603727909&form=IRPRST&ck=F537326F3CF646384A4E26BBBA15E120&selectedindex=3&ajaxhist=0&ajaxserp=0&vt=0&sim=11 "filestruct")

   

   :memo::作为一个学习过的人来说，这些文件对刚开始来说了解的意义并不是特别重要<br>:expressionless::如果你非要了解，可以上网搜索，或者后面的Linux目录介绍<br>

   :key::学习一项新东西的诀窍就是从简单到难，并且持之以恒！
   :ok_hand::话不多说，让我们开始CUI命令开始愉快学习吧！

## 4.terminal 命令简介

再次写在前面：
GNU/Linux是主要服务于服务器的的操作系统，一般来说是不太用于，生活，娱乐。
什么是服务器嘞，我的理解是，提供服务的机器叫服务器
多数情况来说它是一台电脑，一台性能，配置各方面都是非常顶级的电脑。
根据不同的应用场景呢，所在意的点也不一样，比如我们学院的服务器。
主要用于跑很多机器学习，深度学习，神经网络等的代码，
所以我们学院的某台服务器据说是配备了6张A100:star2:

emm，扯远了，服务器大致就是提供服务的机器，根据不同的应用场景，

提供不同的服务，比如加速，网站服务，app服务，等等

很多教程都是从一些简单的密令开始学习，我学习过程中没有什么特别大的问题。
但是在学习过程中，难免会忘记，所以学习一定要温故而知新，🆗

话不多说，那我们开始吧！

- **终端模拟器**
  ubuntu中使用`ctrl+alt+t`，打开终端，关于什么是终端呢，这个又跟计算机的历史发展存在联系。大家可以看一下这位博主的视频，从历史的角度向我们展示了[终端与shell的发展与区别](https://www.bilibili.com/video/BV16A411675V/?spm_id_from=333.880.my_history.page.click)?
  在此处呢，我们所面临的终端界面就是我们之前所提及的CUI，用于输入密令的一个交互界面。在工作中绝大多数时间我们所接触的就是一个终端，或者远程的连接，操作也是一个简单的终端，纯字符操作，纯字符反馈。

- **密令的通用格式(组成)**
  
  `command [-options] [parameters]`
  `命令 [选项] [参数]`
  
  -options :[可选，非必填] 命令的一些选项，可通过选项来控股之命令细节
  
  -parameter :[可选，非必填]命令的参数，多用于命令的指向目标
  OK，相信很多小伙伴看到这里还是很懵逼，没关系大家接着往下看一个简单的命令的栗子:
  
  `ls`:(list directory contents)命令用于显示指定工作目录下之内容
  
  ls -l                    # 以长格式显示当前目录中的文件和目录
  ls -a                    # 显示当前目录中的所有文件和目录，包括隐藏文件
  ls -lh                   # 以人类可读的方式显示当前目录中的文件和目录大小
  ls -t                    # 按照修改时间排序显示当前目录中的文件和目录
  ls -R                    # 递归显示当前目录中的所有文件和子目录
  ls -l /etc/passwd        # 显示/etc/passwd文件的详细信息
  
- **内建密令与外部密令**
  
  + 内建密令
    
    内部命令实际上是shell程序的一部分，其中包含的是一些比较简单的linux系统命令，这些命令由shell程序识别并在shell程序内部完成运行，通常在linux系统加载运行时shell就被加载并驻留在系统内存中。内部命令是写在bashy源码里面的，其执行速度比外部命令快，因为解析内部命令shell不需要创建子进程。比如：exit，history，cd，echo等。
    
  + 外部密令
    
    外部密令是linux系统中的实用程序部分，因为实用程序的功能通常都比较强大，所以其包含的程序量也会很大，在系统加载时并不随系统一起被加载到内存中，而是在需要时才将其调用内存。通常外部命令的实体并不包含在shell中，但是其命令执行过程是由shell程序控制的。shell程序管理外部命令执行的路径查找、加载存放，并控制命令的执行。外部命令是在bash之外额外安装的，通常放在/bin，/usr/bin，/sbin，/usr/sbin……等等。可通过“echo $PATH”命令查看外部命令的存储路径，比如：ls、vi等。
    
    [Linux内部命令和外部命令](https://blog.51cto.com/u_15060546/2651988[)
  
  例如 `cd` 和 `exit` 命令都是内建于 bash shell。可以利用 `type` 命令来查看某个命令是否是内建的]。比如 `echo` 和 `pwd` 既有内建命令也有外部命令。可以使用 `type -a` 来查看。
  ```la
  julie@julie-VirtualBox:~$ type -a exit
  exit 是 shell 内建
  julie@julie-VirtualBox:~$ type -a cd
  cd 是 shell 内建
  julie@julie-VirtualBox:~$ type -a echo
  echo 是 shell 内建
  echo 是 /bin/echo
  julie@julie-VirtualBox:~$ 
  ```

## 5.Linux通用常用密令

再次写在前面，由于本教程纯属是个人的学习笔记，关于密令的学习顺序基本都是根据本人的实际情况来定制的.

help
--help
man
info
help **命令只能用于内建命令的帮助信息查询**
[帮助密令](https://zhuanlan.zhihu.com/p/105096446)

1. **帮助密令之help(只适用于内建密令)**
   ```help``` command,显示内建命令的相关信息。
   **意思是如果你想知道某个 *内建密令*  的用法，直接使用 ```help```+ command**
   例如:	help help
   			help cd

   ​			help exit
   ......	
   🌰

   julie@julie-VirtualBox:~$ help help
   help: help [-dms] [模式 ...]
   	%此处我们可以看到说help的
       显示内建命令的相关信息。
   
   ```latex
   julie@julie-VirtualBox:~$ help help
   help: help [-dms] [模式 ...]
   	%此处我们可以看到说help的
       显示内建命令的相关信息。
       显示内建命令的简略信息。如果指定了 PATTERN 模式，
       给出所有匹配 PATTERN 模式的命令的详细帮助，否则打
       印一个帮助主题列表
       %注意此处就是我们之前所提及的密令的通用格式：命令 [选项] [参数]
       选项：
         -d	输出每个主题的简短描述
         -m	以伪 man 手册的格式显示使用方法
         -s	为每一个匹配 PATTERN 模式的主题仅显示一个用法
       	简介
       
       参数：
         PATTERN	Pattern 模式指定一个帮助主题
       
       退出状态：
       返回成功，除非 PATTERN 模式没有找到或者使用了无效选项。
   %在这里，"PATTERN" 是一个占位符，代表你可以在 `help` 命令后面输入任何你想要获取帮助的命令。例如，如果你想要获取 `cd` 命令的帮助，你可以输入 `help cd`，这里的 `cd` 就是 "PATTERN"。所以 "PATTERN" 可以是任何有效的 bash 命令。
   %如果你在 help 命令后面指定了一个模式（PATTERN），那么它会显示所有匹配该模式的命令的详细帮助信息。如果你没有指定模式，那么它会打印一个帮助主题列表。例如，如果你输入 help cd，它会显示 cd 命令的详细帮助信息。如果你只输入 help，那么它会列出所有可用的内建命令，你可以从中选择一个命令来获取更多的帮助信息。
   上述主要内容有：相关信息+选项+参数
   
   ```
   ```latex
   julie@julie-VirtualBox:~$ help exit
   exit: exit [n]
       退出shell。
       
       以状态 N 退出 shell。  如果 N 被省略，则退出状态
       为最后一个执行的命令的退出状态。
   julie@julie-VirtualBox:~$ help history 
   history: history [-c] [-d 偏移量] [n] 或 history -anrw [文件名] 或 history -ps 参数 [参数...]
       Display or manipulate the history list.
       
       Display the history list with line numbers, prefixing each modified
       entry with a `*'.  An argument of N lists only the last N entries.
   ......
   ```
   
   
   
2. **帮助密令之 ```--help```**

   当我们想知道某些**外部密令或者内建密令**的时候，可以使用 **--help**来获取其用法

   其使用格式为：```command --help```

   ```latex
   julie@julie-VirtualBox:~$ help ls
   bash: help: 没有与 `ls' 匹配的帮助主题。尝试 `help help' 或 `man -k ls' 或 `info ls'。
   julie@julie-VirtualBox:~$ type -a ls
   ls 是 `ls --color=auto' 的别名
   ls 是 /bin/ls
   julie@julie-VirtualBox:~$ ls --help
   用法：ls [选项]... [文件]...
   List information about the FILEs (the current directory by default).
   Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.
   
   必选参数对长短选项同时适用。
     -a, --all			不隐藏任何以. 开始的项目
     -A, --almost-all		列出除. 及.. 以外的任何项目
         --author			与-l 同时使用时列出每个文件的作者
     -b, --escape			以八进制溢出序列表示不可打印的字符
         --block-size=SIZE      scale sizes by SIZE before printing them; e.g.,
                                  '--block-size=M' prints sizes in units of
                                  1,048,576 bytes; see SIZE format below
     -B, --ignore-backups       do not list implied entries ending with ~
   ......
   %注意此处表示ls支持 --help参数
         --help		显示此帮助信息并退出
         --version		显示版本信息并退出
   ```
   
   内建密令也可以使用 --help展示其用法
   
   ```latex
   julie@julie-VirtualBox:~$ cd --help
   cd: cd [-L|[-P [-e]] [-@]] [目录]
       改变 shell 工作目录。
       改变当前目录至 DIR 目录。默认的 DIR 目录是 shell 变量 HOME
       的值。
       变量 CDPATH 定义了含有 DIR 的目录的搜索路径，其中不同的目录名称由冒号 (:)分隔。
       一个空的目录名称表示当前目录。如果要切换到的 DIR 由斜杠 (/) 开头，则 CDPATH
       变量不会被使用。
       
       如果路径找不到，并且 shell 选项 `cdable_vars' 被设定，则参数词被假定为一个
       变量名。如果该变量有值，则它的值被当作 DIR 目录。
       
       选项：
           -L	强制跟随符号链接: 在处理 `..' 之后解析 DIR 中的符号链接。
           -P	使用物理目录结构而不跟随符号链接: 在处理 `..' 之前解析 DIR 中的符号链接。
           -e	如果使用了 -P 参数，但不能成功确定当前工作目录时，返回非零的返回值。
   ......
   ```
   
3. 帮助密令之man

   ```latex
   %尝试使用man --help来获取man的使用方法
   julie@julie-VirtualBox:~$ man --help
   用法： man [选项...] [章节] 手册页...
   
     -C, --config-file=文件   使用该用户设置文件
     -d, --debug                输出调试信息
     -D, --default              将所有选项都重置为默认值
         --warnings[=警告]    开启 groff 的警告
   
    主要运行模式：
     -f, --whatis               等同于 whatis
     -k, --apropos              等同于 apropos
                                把“手册页”参数当成本地文件名来解读
   ......
     -V, --version              打印程序版本
   ```


   ```latex
   %	man ls
   LS(1)                                                            User Commands                                                            LS(1)
   
   NAME%名称
          ls - list directory contents
   SYNOPSIS%概要
          ls [OPTION]... [FILE]...
   DESCRIPTION%描述
          List  information  about  the  FILEs (the current directory by default).  Sort entries alphabetically if none of -cftuvSUX nor --sort is
          specified.
          Mandatory arguments to long options are mandatory for short options too.
          -a, --all
                 do not ignore entries starting with .
   ......
      Exit status:
          0      if OK,
   
          1      if minor problems (e.g., cannot access subdirectory),
   
          2      if serious trouble (e.g., cannot access command-line argument).
   
   AUTHOR%作者
          Written by Richard M. Stallman and David MacKenzie.
   
   REPORTING BUGS%反馈bug
          GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
          Report ls translation bugs to <http://translationproject.org/team/>
   
   COPYRIGHT%版权
          Copyright © 2017 Free Software Foundation, Inc.  License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.
   ......
   ```

   

   


4. 帮助密令之info

   

5. 常用密令之cat mkdir，cd，ls，cp，mv，rm，grep
   
   
   
   + cat
     
     
     ```latex
     ```
     
     
     
   + mkdir
     
     ```latex
     julie@julie-VirtualBox:~/renametest$ mkdir --help
     用法：mkdir [选项]... 目录...
     Create the DIRECTORY(ies), if they do not already exist.
     %	mkdir	testdir 创建文件夹
     julie@julie-VirtualBox:~/renametest$ ls
     testcp.sh
     julie@julie-VirtualBox:~/renametest$ mkdir testdir
     julie@julie-VirtualBox:~/renametest$ ls
     testcp.sh  testdir
     %	mkdir -p test/lss 创建带有父目录的文件夹
     
     julie@julie-VirtualBox:~/renametest$ mkdir test/lss
     mkdir: 无法创建目录"test/lss": 没有那个文件或目录
     julie@julie-VirtualBox:~/renametest$ mkdir -p test/lss
     julie@julie-VirtualBox:~/renametest$ ls
     test  testcp.sh  testdir
     julie@julie-VirtualBox:~/renametest$ cd test
     julie@julie-VirtualBox:~/renametest/test$ ls
     lss
     julie@julie-VirtualBox:~/renametest/test$
     ```
     
   + cd，改变路径
     
     
     ```latex
     %    选项：
     %      -d	输出每个主题的简短描述
     julie@julie-VirtualBox:~$ help -d cd
     cd - Change the shell working directory.
     
     ```
     
     ```latex
     %	cd #切换至用户的home目录
     julie@julie-VirtualBox:/etc$ cd
     julie@julie-VirtualBox:~$ ls
     snap  公共的  视频  文档  音乐
     test  模板    图片  下载  桌面
     %	cd .. #切换至上一级目录
     %	pwd 打印当前工作目录
     julie@julie-VirtualBox:~/test$ pwd 
     /home/julie/test
     julie@julie-VirtualBox:~/test$ cd ..
     julie@julie-VirtualBox:~$ pwd
     /home/julie
     %	cd 目标目录
     julie@julie-VirtualBox:~$ cd /var/log
     julie@julie-VirtualBox:/var/log$ pwd
     /var/log
     ```
     
   + ls
     ```latex
     %List information about the FILEs (the current directory by default).
     %Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.
     % 使用ls --help解锁更多用法
     julie@julie-VirtualBox:/$ ls
     bin    initrd.img      mnt   snap      var
     boot   initrd.img.old  opt   srv       vmlinuz
     cdrom  lib             proc  swapfile  vmlinuz.old
     dev    lib64           root  sys
     etc    lost+found      run   tmp
     home   media           sbin  usr
     %	ls -a -a, --all			不隐藏任何以. 开始的项目
     %	ls -l	  -l				使用较长格式列出信息
     julie@julie-VirtualBox:~/test$ ls -al
     总用量 16
     drwxrwxr-x  3 julie julie 4096 9月  16 22:10 .
     drwxr-xr-x 17 julie julie 4096 9月  20 17:03 ..
     lrwxrwxrwx  1 julie julie    7 9月  16 22:10 j.sh -> test.sh
     drwxrwxr-x  2 julie julie 4096 9月  16 22:03 src
     -rwxrwxrwx  1 julie julie   20 9月  16 12:31 test.sh
     %	ls +指定目录
     julie@julie-VirtualBox:~$ ls -al /var/log
     总用量 4312
     drwxrwxr-x  11 root              syslog             4096 9月  20 17:08 .
     drwxr-xr-x  14 root              root               4096 4月  27  2018 ..
     -rw-r--r--   1 root              root              15415 9月  16 12:31 alternatives.log
     -rw-r--r--   1 root              root              27420 9月  15 23:10 alternatives.log.1
     -rw-r-----   1 root              adm                   0 9月  15 23:10 apport.log
     ......
     ```
     
   + cp
     ```latex
     %将源复制到目标目录，或将多个源复制到目录。
     %	cp 已存在文件 目标文件
     %	cp test.sh testcp.sh
     julie@julie-VirtualBox:~/test$ ls
     j.sh  src  test.sh
     julie@julie-VirtualBox:~/test$ cp test.sh testcp.sh
     julie@julie-VirtualBox:~/test$ ls
     j.sh  src  testcp.sh  test.sh
     %	cp 已存在文件 目标文件
     julie@julie-VirtualBox:~$ cp test/test.sh /test.sh
     cp: 无法创建普通文件'/test.sh': 权限不够
     julie@julie-VirtualBox:~$ sudo cp test/test.sh /test.sh
     [sudo] julie 的密码： 
     julie@julie-VirtualBox:~$ cd /
     julie@julie-VirtualBox:/$ ls
     bin    etc             lib         mnt   run   swapfile  usr
     boot   home            lib64       opt   sbin  sys       var
     cdrom  initrd.img      lost+found  proc  snap  test.sh   vmlinuz
     dev    initrd.img.old  media       root  srv   tmp       vmlinuz.old
     %使用cp --help解锁更多使用方法
     
     ```
     
   + mv
     
     ```latex
     %julie@julie-VirtualBox:~$ mv --help
     %用法：mv [选项]... [-T] 源文件 目标文件
     　%或：mv [选项]... 源文件... 目录
     　%或：mv [选项]... -t 目录 源文件...
     %Rename SOURCE to DEST, or move SOURCE(s) to DIRECTORY.
     % mv 某存在文件名 想更改的文件名 
     julie@julie-VirtualBox:~$ ls
     snap  test  公共的  模板  视频  图片  文档  下载  音乐  桌面
     julie@julie-VirtualBox:~$ mv test renametest
     julie@julie-VirtualBox:~$ ls
     renametest  snap  公共的  模板  视频  图片  文档  下载  音乐  桌面
     
     % mv 某存在的文件 目标目录
     julie@julie-VirtualBox:~/renametest$ vim test.py
     julie@julie-VirtualBox:~/renametest$ ls
     src  testcp.sh  test.py  test.sh
     julie@julie-VirtualBox:~/renametest$ cp test.py ../
     julie@julie-VirtualBox:~/renametest$ ls ..
     renametest  snap  test.py  公共的  模板  视频  图片  文档  下载  音乐  桌面
     ```
   
   + rm
   
     ```latex
     julie@julie-VirtualBox:/home$ rm --help
     用法：rm [选项]... [文件]...
     Remove (unlink) the FILE(s).
     
       -f, --force 
     ......
     % rm 某文件
     julie@julie-VirtualBox:~/renametest$ ls
     src  testcp.sh  test.py
     julie@julie-VirtualBox:~/renametest$ rm test.py 
     julie@julie-VirtualBox:~/renametest$ ls
     src  testcp.sh
     % rm -r 文件夹
     julie@julie-VirtualBox:~/renametest$ ls
     src  testcp.sh
     julie@julie-VirtualBox:~/renametest$ rm src
     rm: 无法删除'src': 是一个目录
     julie@julie-VirtualBox:~/renametest$ rm -r src/
     % rmdir 空文件夹 删除一个空的目录
     julie@julie-VirtualBox:~/renametest$ ls
     src  testcp.sh
     julie@julie-VirtualBox:~/renametest$ rmdir src
     julie@julie-VirtualBox:~/renametest$ ls
     testcp.sh
     julie@julie-VirtualBox:~/renametest$ 
     使用rm --help解锁更多知识！
     ```

   + grep
     ```latex
     julie@julie-VirtualBox:~$ grep --help
     用法: grep [选项]... PATTERN [FILE]...
     Search for PATTERN in each FILE.
     Example: grep -i 'hello world' menu.h main.c
     %	grep 需要查询的内容 目标文件
     在实际中hello（被查询到的内容）会被突出显示
     ```
   
     ![image-20230922111922694](C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230922111922694.png)
     ```latex
     %	grep 需要查询的内容 目标文件1 目标文件2
     ```
   
     ![image-20230922112436939](C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230922112436939.png)
   
     ```la
     grep --help 解锁更多玩法！
     ```
   
     
   
   
   
   
   
   + 
   
   + 
   
   
   
6. 用户与用户组

   > Linux系统是一个多用户多任务的分时操作系统，任何一个要使用系统资源的用户，都必须首先向系统管理员申请一个账号，然后以这个账号的身份进入系统。
   >
   > 用户的账号一方面可以帮助系统管理员对使用系统的用户进行跟踪，并控制他们对系统资源的访问；另一方面也可以帮助用户组织文件，并为用户提供安全性保护。
   >
   > 每个用户账号都拥有一个唯一的用户名和各自的口令。
   >
   > 用户在登录时键入正确的用户名和口令后，就能够进入系统和自己的主目录。
   >
   > 实现用户账号的管理，要完成的工作主要有如下几个方面：
   >
   > 1:用户账号的添加、删除与修改。
   > 2:用户口令的管理。
   > 3:用户组的管理。

   大家都知道，Linux 系统中用户信息存放在 `/etc/passwd` 文件中。

   这是一个包含每个用户基本信息的文本文件。当我们在系统中创建一个用户，新用户的详细信息就会被添加到这个文件中。

   `/etc/passwd` 文件将每个用户的基本信息记录为文件中的一行，一行中包含 7 个字段。
   <img src="pics\user&group\des_of_user.jpeg"/>

   ```latex
   justin:x:1001:1001::/home/justin:/bin/sh
   ```

   `/etc/passwd` 文件的一行代表一个单独的用户。该文件将用户的信息分为 3 个部分。


   + 用户的创建，配置密码，删除
     	

     1. 创建：``useradd 选项 用户名``

        ```latex
        %创建名叫testuser的新用户，且为其创建用户主目录为/home/testuser
        %尝试使用useradd --help了解用法，但常规的添加用户，一般使用如下方式即可
        useradd -d /home/testuser -m testuser
        
        julie@julie-VirtualBox:/home$ ls
        julie  justin  testuser
        ```
     
        :exclamation::创建用户时，要使用sudo权限
        ```latex
        julie@julie-VirtualBox:/$ 
        julie@julie-VirtualBox:/$ useradd -d /home/testuser -m testuser
        useradd: Permission denied.
        useradd：无法锁定 /etc/passwd，请稍后再试。
        julie@julie-VirtualBox:/$ sudo useradd -d /home/testuser -m testuser
        julie@julie-VirtualBox:/$ awk -F':' '{ print $1}' /etc/passwd #查看已存在用户
        root
        daemon
        bin
        sys
        ...
        gdm
        julie
        vboxadd
        cups-pk-helper
        justin
        testuser %我们刚创建的testuser
        ```
     
     2. 配置密码``passwd 选项 用户名``
        ```latex
        sudo passwd testuser
        ```
     
     3. 修改```usermod 选项 用户名```
     
        ```latex
        julie@julie-VirtualBox:~/renametest$ usermod --help
        用法：usermod [选项] 登录
        
        选项：
          -c, --comment 注释            GECOS 字段的新值
          -d, --home HOME_DIR           用户的新主目录
          -e, --expiredate EXPIRE_DATE  设定帐户过期的日期为 EXPIRE_DATE
          -f, --inactive INACTIVE       过期 INACTIVE 天数后，设定密码为失效状态
          -g, --gid GROUP               强制使用 GROUP 为新主组
          -G, --groups GROUPS           新的附加组列表 GROUPS
          -a, --append GROUP            将用户追加至上边 -G 中提到的附加组中，
                                        并不从其它组中删除此用户
          -h, --help                    显示此帮助信息并推出
          -l, --login LOGIN             新的登录名称
          -L, --lock                    锁定用户帐号
          -m, --move-home               将家目录内容移至新位置 (仅于 -d 一起使用)
          -o, --non-unique              允许使用重复的(非唯一的) UID
          -p, --password PASSWORD       将加密过的密码 (PASSWORD) 设为新密码
          -R, --root CHROOT_DIR         chroot 到的目录
          -s, --shell SHELL             该用户帐号的新登录 shell
          -u, --uid UID                 用户帐号的新 UID
          -U, --unlock                  解锁用户帐号
          -v, --add-subuids FIRST-LAST  add range of subordinate uids
          -V, --del-subuids FIRST-LAST  remove range of subordinate uids
          -w, --add-subgids FIRST-LAST  add range of subordinate gids
          -W, --del-subgids FIRST-LAST  remove range of subordinate gids
          -Z, --selinux-user  SEUSER       用户账户的新 SELinux 用户映射
        
        ```
     
        ```latex
        justin:x:1001:1001::/home/justin:/bin/sh
        julie@julie-VirtualBox:/home$ ls
        julie  justin  newhome
        julie@julie-VirtualBox:/home$ sudo usermod -d /home/newhome justin
        julie@julie-VirtualBox:/home$ cat /etc/passwd
        ......
        justin:x:1001:1001::/home/newhome:/bin/sh
        
        ```
     
        
     
     4. 
     
        
     
        删除``userdel 选项 用户名``
     
        ```latex
        julie@julie-VirtualBox:/home$ sudo userdel -r testuser #用户的主目录一起删除。
        userdel: testuser 邮件池 (/var/mail/testuser) 未找到
        julie@julie-VirtualBox:/home$ ls
        julie  justin
        julie@julie-VirtualBox:/home$ cat /etc/pqsswd
        ......
        julie:x:1000:1000:julie,,,:/home/julie:/bin/bash
        vboxadd:x:999:1::/var/run/vboxadd:/bin/false
        cups-pk-helper:x:121:116:user for cups-pk-helper service,,,:/home/cups-pk-helper:/usr/sbin/nologin
        justin:x:1001:1001::/home/justin:/bin/sh
        ```
        
     5. 查看当前已经拥有的账户名:```awk -F':' '{ print $1}' /etc/passwd```
     
     ```latex
     julie@julie-VirtualBox:/home$ cat /etc/pqsswd
     ......
     julie:x:1000:1000:julie,,,:/home/julie:/bin/bash
     vboxadd:x:999:1::/var/run/vboxadd:/bin/false
     cups-pk-helper:x:121:116:user for cups-pk-helper service,,,:/home/cups-pk-helper:/usr/sbin/nologin
     justin:x:1001:1001::/home/justin:/bin/sh
     ```
     
     
     
   + 用户组的创建，配置，删除
     
     

    <img src="pics\user&group\usergp.png"/>

   + 

   

7. chmod&chown

   Linux 系统是一种典型的多用户系统，不同的用户处于不同的地位，拥有不同的权限。

   为了保护系统的安全性，Linux 系统对不同的用户访问同一文件（包括目录文件）的权限做了不同的规定。

   在 Linux 中我们通常使用以下两个命令来修改文件或目录的所属用户与权限：

   ![](pics\files\file-llls22.jpg)
   ```latex
   julie@julie-VirtualBox:~/renametest$ ls -al
   总用量 20
   drwxrwxr-x  3 julie julie 4096 9月  20 17:54 .
   drwxr-xr-x 17 julie julie 4096 9月  20 18:56 ..
   drwxrwxr-x  2 julie julie 4096 9月  16 22:03 src
   -rwxrwxr-x  1 julie julie   20 9月  20 17:19 testcp.sh
   -rw-rw-r--  1 julie julie   22 9月  20 17:34 test.py
   %testcp.sh -代表文件，rwx代表用户权限，即julie对该文件可读，写，执行同组用户的也可读，写，执行其他用户只能读和执行，不能写
   r read
   w write
   x execute
   -代表文件，d代表文件夹
   
   ```

   

   + chmod
     ```latex
     %Change the mode of each FILE to MODE.
     %With --reference, change the mode of each FILE to that of RFILE.
     
     ```

     

     

   + 

     

   + 

     

   + 

     

   

8. 

   

9. 

   

10. 

    

11. 

    

12. 

    

13. 





## 6.



## 7.



## 8.



## 9.



## 10.



## 11.

