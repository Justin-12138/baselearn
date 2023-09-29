# 磁盘管理与常用软件安装！

### 1.磁盘管理，分区，扩容，

在**此电脑**中查看磁盘占用情况

![image-20230929162246929](C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929162246929.png)

**鼠标右键windows开始，点击磁盘管理**

<img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929162050656.png" alt="image-20230929162050656" style="zoom:25%;" />

![image-20230929162317371](C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929162317371.png)

可以看到我的电脑现在有四个分区，因为我安装了双系统（150GB用于Ubuntu），在windows下只有C盘和D盘两个区，前面的100mb用于系统的启动。

我认为比较良好的分区方式就是C+D盘模式。

从左到右，随着分区的逐渐增多，电脑对其的读写速度也会相应减慢，C>D>E>F......，不过一般情况下感知不明显，除非玩大型游戏，需要加载很多资源数据文件。

C盘用于存放核心软件，占用较大的软件。比如

通常安装在此文件夹下面：

![image-20230929163203453](C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929163203453.png)



为了更好的管理个人文件，或者减少C盘的压力，虽然现在大家的空间都很大，但是将所有软件安装在一个盘，查询起来相对不方便。

此时，我们便可以将一些非核心软件，比如QQ，百度云等放入D盘，该有自己的私人文件，比如上课的PPT，要交的Word文档。

![image-20230929163417436](C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929163417436.png)

分区，即从我们现存的盘符中，根据我们的需要，进一步细化我们的磁盘，比如C盘存核心文件，D盘存非核心软件，此时，你还想分一个E盘出来存放你的个人照片，视频等。

首先，我们要知道我们所分出来的一块新的分区，是会紧靠于原分区的右侧，例如我们在C盘的基础上分出20G的空间(前提是你的C盘还有超过20G的空间)

右键C盘，点击，压缩卷

![image-20230929164313887](C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929164313887.png)

此时，会显示我们的C盘的空间占用情况

压缩前总计大小即我们的C盘目前的总空间：

255536MB/1024=249GB

可压缩空间：

105177MB/1024=102GB

**我们需要压缩20GB**

**20x1024=20480MB**

**故我们在输入压缩空间量输入20480**

点击压缩。

<img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929164429820.png" alt="image-20230929164429820" style="zoom: 50%;" />

而后，便会有一个会有一个未分配区域，20G

![image-20230929165107821](C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929165107821.png)

此时可以看到我们的C盘也从原来的249GB变成了229GB。

此时我们便可以使用这20G去创建一个新盘符，鼠标右键未分配区域，点击新建简单卷

<img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929165311313.png" alt="image-20230929165311313" style="zoom:33%;" />

点击下一页

<img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929165428415.png" alt="image-20230929165428415" style="zoom:33%;" />

点击下一页。

<img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929165512349.png" alt="image-20230929165512349" style="zoom:33%;" />

默认即可，但是可以**自定义你的卷标，比如可以设置为pics**

![image-20230929165548725](C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929165548725.png)

点击完成

<img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929165702352.png" alt="image-20230929165702352" style="zoom:33%;" />



我们就可以看到此时我们的新添加的一个分区pics了。

![image-20230929165747141](C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929165747141.png)

![image-20230929165823176](C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929165823176.png)



假设我不想要这么多分区，我想把原来的20G重新放入我的C盘该怎么办呢？

此时我们就需要做**扩展卷**，可以看到此时的扩展卷是不可被选择的，因为**扩展卷需要在被扩展的盘符的右侧存在未分配区域**，才可进行扩展。



<img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929170017163.png" alt="image-20230929170017163" style="zoom:50%;" />

我们刚刚从C盘压缩了20G出来，我们现在需要将这20G给扩展到C盘，首先需要把原盘符的文件备份到其他盘符

假设我的pics里面有一个重要文件

<img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929170649566.png" alt="image-20230929170649566" style="zoom:50%;" />

你可以直接将其剪切，并粘贴到其他盘符，**尽量确保你的此时这20G的盘符是一个空盘符**，如果存在一些不需要备份的数据文件，你可以打开磁盘管理，右键20G磁盘，直接格式化该盘符，

<img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929170848746.png" alt="image-20230929170848746" style="zoom:50%;" />

点击确定

<img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929171025522.png" alt="image-20230929171025522" style="zoom:50%;" />

格式化完成后，此时便是一个空盘符，右键该盘符，点击删除卷

<img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929171121569.png" alt="image-20230929171121569" style="zoom:33%;" />

点击是

<img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929171156332.png" alt="image-20230929171156332" style="zoom:50%;" />

此时我们可以看到我们的磁盘管理中出现了那20G未分配空间

![image-20230929171233146](C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929171233146.png)

此时右键C盘，扩展卷便可选，点击扩展卷

<img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929171328849.png" alt="image-20230929171328849" style="zoom:33%;" />

点击下一页

<img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929171352598.png" alt="image-20230929171352598" style="zoom:25%;" />

20479/1024=19.999~=20，20479便是我们的原来的20G的未分配

我们在选择空间量处选择20479，即全部将未分配空间分配给C盘，点击下一页

<img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929171426199.png" alt="image-20230929171426199" style="zoom:50%;" />

点击完成

<img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929171725619.png" alt="image-20230929171725619" style="zoom:33%;" />

此时我们可以看到我们的磁盘管理中C盘又变成249GB了，原来的未分配区域也不在了。

![](C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929171815386.png)

**:exclamation:注意，磁盘的压缩与扩展都要在其右侧**

**压缩20G新区域，会放置于原盘符的右侧，**

**扩展某盘符(如C盘)，需要在被扩展盘符(C盘)的右侧需要存在未分配区域**

**我们不能直接在D盘分配一部分空间然后再扩展到C盘**

但是可以间接操作，

以我的电脑为例，假设我们需要再给扩展C盘20GB空间

现在我的D盘已经使用了76.5-51.5=25GB，

我可以从D盘中，分配50G创建一个新盘符，将原来D盘的数据复制到新盘符

然后格式化D盘，并删除D盘的卷，此时就可以将剩余的76.5-50=26.5GB扩展C盘。



![image-20230929172815250](C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929172815250.png)









### 2.软件安装

**python,anaconda,pycharm,git**

之后我们会经常使用到power shell这个工具，power shell算是一种终端模拟器，

```latex
power shell在这个目录下，user代表用户，justin是我的用户名，你打开的时候是你的用户名
C:\Users\justin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Windows PowerShell
```

<img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929192423817.png" alt="image-20230929192423817" style="zoom:25%;" />
可以将其发送到桌面快捷方式，然后固定到任务栏

我的电脑已经配置好这些环境了，但是秉着认真负责的态度，我还是决定给卸载并重装一次！

0. pycharm
   pycharm是一个集成开发环境,就是几乎所有的事情都可以在这里面做。[pycharm](官网)，选择社区版就可以了

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929191405892.png" alt="image-20230929191405892" style="zoom:33%;" />

   下载完成后点击安装
   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929191545149.png" alt="image-20230929191545149" style="zoom:33%;" />

   

   放C盘也可
   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929191621025.png" alt="image-20230929191621025" style="zoom:33%;" />

   

   全选，next
   第一个创建桌面快捷方式，第二个是配置环境变量
   第三个是可以以项目形式打开文件夹，最后一个是创建链接到.py，即python文件默认用pycharm打开。

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929191641252.png" alt="image-20230929191641252" style="zoom:33%;" />

   

   install,然后等待安装完成

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929191659629.png" alt="image-20230929191659629" style="zoom:33%;" />
   finish，reboot later

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929191915224.png" alt="image-20230929191915224" style="zoom:33%;" />

   

   

   
   

   

1. python
   在power shell中输入python，我已经安装好了python3.10.8

   ![image-20230929174458322](C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929174458322.png)

   卸载它先！设置里点击应用搜索python，点击三个点然后点卸载
   ![image-20230929174633631](C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929174633631.png)

   卸载成功！

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929174846068.png" alt="image-20230929174846068" style="zoom:50%;" />

   此时在power shell中输入python
   便不会显示任何信息，而是推荐我们安装

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929174952183.png" alt="image-20230929174952183" style="zoom:33%;" />

   但是我们不在微软商店安装，而是官网安装，python更新至今有很多很多版本

   我最常用的是python3.10.8,因为现在很多AI项目要求python3.10.6，所以我们选择3.10.8兼容性更好一点

   安装方法

   在[python官网](https://www.python.org/)

   python官网，这是一个链接，你按住ctrl，然后鼠标左键点击即可跳到浏览器

   **在Downloads中点击All releases。**

   ![image-20230929175631888](C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929175631888.png)

   

   **在looking for a specific release中找到python3.10.8,点击download**

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929175736918.png" alt="image-20230929175736918" style="zoom:50%;" />

   然后点击Windows installer64bit，

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929175916177.png" alt="image-20230929175916177" style="zoom:50%;" />

   等待下载完成

   ![image-20230929180006830](C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929180006830.png)

   下载完成后，我们打开其所在文件夹

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929180119166.png" alt="image-20230929180119166" style="zoom:50%;" />

   然后勾选下面两个，选框，第一个表示安装时会使用管理员权限，第二个代表将其放入到环境变量（即我们在电脑的全局可使用python），并选择Customize installation(自定义安装)，

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929180208470.png" alt="image-20230929180208470" style="zoom:50%;" />

   所有都勾选，

   第一个代表会下载python的使用手册，很长很长，但是是官方的，可以看一看，虽然我没看过

   第二个代表安装pip用于安装第三方库，依赖之类的，以后配置虚拟环境会经常用到

   第三个代表安装将tkinter安装到IDLE中，IDLE指的是集成开发环境，但是其实我们可以不需要这一个，因为我们待会要安装pycharm，不过也可以安装，等你厉害了可以用他官方的IDLE写代码的时候，也可能会用到这个tkinter，用于创建一些界面啊之类的

   第四个代表测试框架，我对测试不太了解，但是还是安装上吧，万一以后用的上

   第五个for all users 代表为所有用户安装，这个也安装上吧，虽然是全民pc的时代了，但是万一你之后想创建新的users就不用重新安装python了

   点击next

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929180423251.png" alt="image-20230929180423251" style="zoom:50%;" />

   勾选如下，安装路径可以的话就放在C盘吧，因为python也算是相对比较重要的软件，点击install

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929181314577.png" alt="image-20230929181314577" style="zoom:33%;" />

   

   安装完成，点击close

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929181606449.png" alt="image-20230929181606449" style="zoom:33%;" />

   我们再次再powershell中输入python，此时就会显示python的版本信息。

   ![image-20230929181704808](C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929181704808.png)

   

2. anaconda
   anaconda是一个很强大的管理工具，帮助你管理python的版本，创建不同版本的虚拟环境，

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929174814540.png" alt="image-20230929174814540" style="zoom:33%;" />

   还是先卸载：

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929181916724.png" alt="image-20230929181916724" style="zoom:33%;" />

   然后去[官网](https://www.anaconda.com/),点击Free Download
   ![image-20230929182019398](C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929182019398.png)

   选择windows
   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929182105556.png" alt="image-20230929182105556" style="zoom:33%;" />

   下载好后，双击

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929182146734.png" alt="image-20230929182146734" style="zoom:33%;" />

   

   next

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929182220966.png" alt="image-20230929182220966" style="zoom: 33%;" />
   I agree

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929182241771.png" alt="image-20230929182241771" style="zoom: 33%;" />

   all users吧，需要管理员授权

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929182331912.png" alt="image-20230929182331912" style="zoom:33%;" />

   放在C盘可以的，如果空间够的话

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929182413738.png" alt="image-20230929182413738" style="zoom:33%;" />

   全部勾选

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929182450909.png" alt="image-20230929182450909" style="zoom:33%;" />

   等待安装完成，即可。点击Finish

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929182918078.png" alt="image-20230929182918078" style="zoom:33%;" />


   然后它可能会跳出来一个绿色的圈圈，一会就会打开其主页，我们什么都不用管，

   点击**No,don't show again，然后直接退出**

   

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929183115631.png" alt="image-20230929183115631" style="zoom:33%;" />

   **点击Yes**

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929183253680.png" alt="image-20230929183253680" style="zoom:33%;" />
   此时你可以在应用里看到，Anaconda3这个文件夹
   ![image-20230929183413895](C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929183413895.png)

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929183358104.png" alt="image-20230929183358104" style="zoom:33%;" />
   右键Anaconda Prompt，更多，点击打开文件位置，此后，我们使用的最多的便是这个类似于专属于anaconda的终端模拟器

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929183811989.png" alt="image-20230929183811989" style="zoom:33%;" />
   将其快捷方式发送到桌面快捷方式。

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929183916333.png" alt="image-20230929183916333" style="zoom:33%;" />

   

   然后将其托到任务栏，直到出现链接，即可
   <img src="C:\Users\justin\Documents\Tencent Files\2094623381\nt_qq\nt_data\Pic\2023-09\Thumb\01edc775e5cbc51dad90c8174a4e2b50_720.png" alt="01edc775e5cbc51dad90c8174a4e2b50_720" style="zoom:33%;" />

   我们在任务栏中打开它并输入

   ```latex
   conda env list
   ```

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929184245533.png" alt="image-20230929184245533" style="zoom:33%;" />

   就会显示我们系统中现有的虚拟环境，你初次安装应该是只有base这个虚拟环境

   ok，接下来我给你稍微讲一下什么是虚拟环境(可能不太准确)，就是我们在开发项目的过程中，或者是说去运行别人的项目的过程中，每个人所需要的python版本都不一样，然后需要的第三方库，依赖也不一样

   我们创建并配置我们的虚拟环境来满足项目虚拟环境要求。

   在虚拟环境中包括了python版本，python解释器们还有python的第三方库等。

   对于虚拟环境就大概讲这么多，就是为了帮我们的项目满足实现我们依赖，版本等要求。

   为什么使用anaconda？因为anaconda是一个很好python的虚拟环境管理的软件，其实有很多创建虚拟环境的方式，但是相比起来，使用anaconda来管你虚拟环境是最为方便快捷的。

   那么接下来，我们便可以使用使用简单的密令来创建一下虚拟环境。

   比如我们刚开始学习python我们创建了一个项目叫做base_python。

   我们希望我们的虚拟环境的python版本是3.10.6，我们便可通过如下密令创建虚拟环境

   ```latex
   #代表创建一个新的名叫base_learn，python版本为3.10.6的虚拟环境
   conda create -n base_learn python==3.10.6
   
   #打开固定到任务栏的Anaconda prompt，输入上述密令并回车，期间会出现一些调试信息，不用管
   ```

   ![image-20230929185850899](C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929185850899.png)

   

   直到它出现，下图，输入y,并回车

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929190032361.png" alt="image-20230929190032361" style="zoom:50%;" />
   便可以看到一些基础的包，和python3.10.6正在安装

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929190114384.png" alt="image-20230929190114384" style="zoom:33%;" />
   安装完成
   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929190219779.png" alt="image-20230929190219779" style="zoom:33%;" />

   ```latex
   #输入 conda env list即可看到我们刚创建的base_learn虚拟环境（）
   ```

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929190427967.png" alt="image-20230929190427967" style="zoom:33%;" />
   ```latex
   输入cls 并回车，来清屏
   
   ```

   ![image-20230929190530711](C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929190530711.png)

   ```latex
   #进入虚拟环境（进入虚拟环境来管理第三方库）
   conda activate base_learn
   #可以看到前面的base变成了base_learn，前面的()代表我们目前在那个虚拟环境下
   ```

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929190724972.png" alt="image-20230929190724972" style="zoom:33%;" />

   ```latex
   使用conda deactivate 退出当前虚拟环境
   ```

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929190906367.png" alt="image-20230929190906367" style="zoom:33%;" />

   

3. 创建一个项目

   打开pycharm，点击 New Project
   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929192632817.png" alt="image-20230929192632817" style="zoom:33%;" />

   location代表项目位置最后的pythonProject代表项目名称

   

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929192720496.png" alt="image-20230929192720496" style="zoom:33%;" />
   ```latex
   我们设置项目名称为baselearn
   选择虚拟环境为Previousls configured interpreter(之前配置的解释器（即我们之前创建的虚拟环境）)
   点击add local interpreter
   ```

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929192906546.png" alt="image-20230929192906546" style="zoom:33%;" />

   ```latex
   点击conda enviroment
   选择 using existing enviroment 然后找到我们之前创建的base_learn
   点击ok
   ```

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929193132246.png" alt="image-20230929193132246" style="zoom:33%;" />

   ```latex
   点击create
   ```

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929193257316.png" alt="image-20230929193257316" style="zoom:33%;" />

   ```la
   等待下面进度条加载完成，表示我们的虚拟环境被读取完成
   ```

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929193435526.png" alt="image-20230929193435526" style="zoom:33%;" />

   ```latex
   左下角这几个从上到下分别是
   控制台:主要用于程序的调式，debug
   包:运行代码的第三方库
   服务:比如网页服务，jupyter这种在线代码编辑
   终端:这个应该是之后用的最多的，安装第三方库啊之类的，git创建版本啊，都在这里
   报错:程序问题
   版本控制(git):显示版本信息，这个也很有用！我会在接下来的教程教会你如何使用git和githubg
   ```

   

   <img src="C:\Users\justin\AppData\Roaming\Typora\typora-user-images\image-20230929193738909.png" alt="image-20230929193738909" style="zoom:33%;" />

4. 

5. 

6. 





























