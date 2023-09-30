# 磁盘管理与常用软件安装！

### 1.磁盘管理，分区，扩容

在**此电脑**中查看磁盘占用情况

![image-20230929162246929](assets\image-20230929162246929.png)

**鼠标右键windows开始，点击磁盘管理**

<img src="assets\image-20230929162050656.png" alt="image-20230929162050656" style="zoom:25%;" />

![image-20230929162317371](assets\image-20230929162317371.png)

可以看到我的电脑现在有四个分区，因为我安装了双系统（150GB用于Ubuntu），在windows下只有C盘和D盘两个区，前面的100mb用于系统的启动。

我认为比较良好的分区方式就是C+D盘模式。

从左到右，随着分区的逐渐增多，电脑对其的读写速度也会相应减慢，C>D>E>F......，不过一般情况下感知不明显，除非玩大型游戏，需要加载很多资源数据文件。

C盘用于存放核心软件，占用较大的软件。比如

通常安装在此文件夹下面：

![image-20230929163203453](assets\image-20230929163203453.png)



为了更好的管理个人文件，或者减少C盘的压力，虽然现在大家的空间都很大，但是将所有软件安装在一个盘，查询起来相对不方便。

此时，我们便可以将一些非核心软件，比如QQ，百度云等放入D盘，该有自己的私人文件，比如上课的PPT，要交的Word文档。

![image-20230929163417436](assets\image-20230929163417436.png)

分区，即从我们现存的盘符中，根据我们的需要，进一步细化我们的磁盘，比如C盘存核心文件，D盘存非核心软件，此时，你还想分一个E盘出来存放你的个人照片，视频等。

首先，我们要知道我们所分出来的一块新的分区，是会紧靠于原分区的右侧，例如我们在C盘的基础上分出20G的空间(前提是你的C盘还有超过20G的空间)

右键C盘，点击，压缩卷

![image-20230929164313887](assets\image-20230929164313887.png)

此时，会显示我们的C盘的空间占用情况

压缩前总计大小即我们的C盘目前的总空间：

255536MB/1024=249GB

可压缩空间：

105177MB/1024=102GB

**我们需要压缩20GB**

**20x1024=20480MB**

**故我们在输入压缩空间量输入20480**

点击压缩。

<img src="assets\image-20230929164429820.png" alt="image-20230929164429820" style="zoom: 50%;" />

而后，便会有一个会有一个未分配区域，20G

![image-20230929165107821](assets\image-20230929165107821.png)

此时可以看到我们的C盘也从原来的249GB变成了229GB。

此时我们便可以使用这20G去创建一个新盘符，鼠标右键未分配区域，点击新建简单卷

<img src="assets\image-20230929165311313.png" alt="image-20230929165311313" style="zoom:33%;" />

点击下一页

<img src="assets\image-20230929165428415.png" alt="image-20230929165428415" style="zoom:33%;" />

点击下一页。

<img src="assets\image-20230929165512349.png" alt="image-20230929165512349" style="zoom:33%;" />

默认即可，但是可以**自定义你的卷标，比如可以设置为pics**

![image-20230929165548725](assets\image-20230929165548725.png)

点击完成

<img src="assets\image-20230929165702352.png" alt="image-20230929165702352" style="zoom:33%;" />



我们就可以看到此时我们的新添加的一个分区pics了。

![image-20230929165747141](assets\image-20230929165747141.png)

![image-20230929165823176](assets\image-20230929165823176.png)



假设我不想要这么多分区，我想把原来的20G重新放入我的C盘该怎么办呢？

此时我们就需要做**扩展卷**，可以看到此时的扩展卷是不可被选择的，因为**扩展卷需要在被扩展的盘符的右侧存在未分配区域**，才可进行扩展。



<img src="assets\image-20230929170017163.png" alt="image-20230929170017163" style="zoom:50%;" />

我们刚刚从C盘压缩了20G出来，我们现在需要将这20G给扩展到C盘，首先需要把原盘符的文件备份到其他盘符

假设我的pics里面有一个重要文件

<img src="assets\image-20230929170649566.png" alt="image-20230929170649566" style="zoom:50%;" />

你可以直接将其剪切，并粘贴到其他盘符，**尽量确保你的此时这20G的盘符是一个空盘符**，如果存在一些不需要备份的数据文件，你可以打开磁盘管理，右键20G磁盘，直接格式化该盘符，

<img src="assets\image-20230929170848746.png" alt="image-20230929170848746" style="zoom:50%;" />

点击确定

<img src="assets\image-20230929171025522.png" alt="image-20230929171025522" style="zoom:50%;" />

格式化完成后，此时便是一个空盘符，右键该盘符，点击删除卷

<img src="assets\image-20230929171121569.png" alt="image-20230929171121569" style="zoom:33%;" />

点击是

<img src="assets\image-20230929171156332.png" alt="image-20230929171156332" style="zoom:50%;" />

此时我们可以看到我们的磁盘管理中出现了那20G未分配空间

![image-20230929171233146](assets\image-20230929171233146.png)

此时右键C盘，扩展卷便可选，点击扩展卷

<img src="assets\image-20230929171328849.png" alt="image-20230929171328849" style="zoom:33%;" />

点击下一页

<img src="assets\image-20230929171352598.png" alt="image-20230929171352598" style="zoom:25%;" />

20479/1024=19.999~=20，20479便是我们的原来的20G的未分配

我们在选择空间量处选择20479，即全部将未分配空间分配给C盘，点击下一页

<img src="assets\image-20230929171426199.png" alt="image-20230929171426199" style="zoom:50%;" />

点击完成

<img src="assets\image-20230929171725619.png" alt="image-20230929171725619" style="zoom:33%;" />

此时我们可以看到我们的磁盘管理中C盘又变成249GB了，原来的未分配区域也不在了。

![](assets\image-20230929171815386.png)

**:exclamation:注意，磁盘的压缩与扩展都要在其右侧**

**压缩20G新区域，会放置于原盘符的右侧，**

**扩展某盘符(如C盘)，需要在被扩展盘符(C盘)的右侧需要存在未分配区域**

**我们不能直接在D盘分配一部分空间然后再扩展到C盘**

但是可以间接操作，

以我的电脑为例，假设我们需要再给扩展C盘20GB空间

现在我的D盘已经使用了76.5-51.5=25GB，

我可以从D盘中，分配50G创建一个新盘符，将原来D盘的数据复制到新盘符

然后格式化D盘，并删除D盘的卷，此时就可以将剩余的76.5-50=26.5GB扩展C盘。



![image-20230929172815250](assets\image-20230929172815250.png)









### 2.软件安装

**python,anaconda,pycharm,git**

之后我们会经常使用到power shell这个工具，power shell算是一种终端模拟器，

```latex
power shell在这个目录下，user代表用户，justin是我的用户名，你打开的时候是你的用户名
C:\Users\justin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Windows PowerShell
```

<img src="assets\image-20230929192423817.png" alt="image-20230929192423817" style="zoom:25%;" />
可以将其发送到桌面快捷方式，然后固定到任务栏

我的电脑已经配置好这些环境了，但是秉着认真负责的态度，我还是决定给卸载并重装一次！

0. pycharm
   
   pycharm是一个集成开发环境,就是几乎所有的事情都可以在这里面做。[pycharm](官网)，选择社区版就可以了
   
   <img src="assets\image-20230929191405892.png" alt="image-20230929191405892" style="zoom:33%;" />
   
   下载完成后点击安装
   <img src="assets\image-20230929191545149.png" alt="image-20230929191545149" style="zoom:33%;" />
   
   
   
   放C盘也可
   <img src="assets\image-20230929191621025.png" alt="image-20230929191621025" style="zoom:33%;" />
   
   
   
   全选，next
   第一个创建桌面快捷方式，第二个是配置环境变量
   第三个是可以以项目形式打开文件夹，最后一个是创建链接到.py，即python文件默认用pycharm打开。
   
   <img src="assets\image-20230929191641252.png" alt="image-20230929191641252" style="zoom:33%;" />
   
   
   
   install,然后等待安装完成
   
   <img src="assets\image-20230929191659629.png" alt="image-20230929191659629" style="zoom:33%;" />
   finish，reboot later
   
   <img src="assets\image-20230929191915224.png" alt="image-20230929191915224" style="zoom:33%;" />
   
   
   
   
   
   

1. python
   在power shell中输入python，我已经安装好了python3.10.8

   ![image-20230929174458322](assets\image-20230929174458322.png)

   卸载它先！设置里点击应用搜索python，点击三个点然后点卸载
   ![image-20230929174633631](assets\image-20230929174633631.png)

   卸载成功！

   <img src="assets\image-20230929174846068.png" alt="image-20230929174846068" style="zoom:50%;" />

   此时在power shell中输入python
   便不会显示任何信息，而是推荐我们安装

   <img src="assets\image-20230929174952183.png" alt="image-20230929174952183" style="zoom:33%;" />

   但是我们不在微软商店安装，而是官网安装，python更新至今有很多很多版本

   我最常用的是python3.10.8,因为现在很多AI项目要求python3.10.6，所以我们选择3.10.8兼容性更好一点

   安装方法

   在[python官网](https://www.python.org/)

   python官网，这是一个链接，你按住ctrl，然后鼠标左键点击即可跳到浏览器

   **在Downloads中点击All releases。**

   ![image-20230929175631888](assets\image-20230929175631888.png)

   

   **在looking for a specific release中找到python3.10.8,点击download**

   <img src="assets\image-20230929175736918.png" alt="image-20230929175736918" style="zoom:50%;" />

   然后点击Windows installer64bit，

   <img src="assets\image-20230929175916177.png" alt="image-20230929175916177" style="zoom:50%;" />

   等待下载完成

   ![image-20230929180006830](assets\image-20230929180006830.png)

   下载完成后，我们打开其所在文件夹

   <img src="assets\image-20230929180119166.png" alt="image-20230929180119166" style="zoom:50%;" />

   然后勾选下面两个，选框，第一个表示安装时会使用管理员权限，第二个代表将其放入到环境变量（即我们在电脑的全局可使用python），并选择Customize installation(自定义安装)，

   <img src="assets\image-20230929180208470.png" alt="image-20230929180208470" style="zoom:50%;" />

   所有都勾选，

   第一个代表会下载python的使用手册，很长很长，但是是官方的，可以看一看，虽然我没看过

   第二个代表安装pip用于安装第三方库，依赖之类的，以后配置虚拟环境会经常用到

   第三个代表安装将tkinter安装到IDLE中，IDLE指的是集成开发环境，但是其实我们可以不需要这一个，因为我们待会要安装pycharm，不过也可以安装，等你厉害了可以用他官方的IDLE写代码的时候，也可能会用到这个tkinter，用于创建一些界面啊之类的

   第四个代表测试框架，我对测试不太了解，但是还是安装上吧，万一以后用的上

   第五个for all users 代表为所有用户安装，这个也安装上吧，虽然是全民pc的时代了，但是万一你之后想创建新的users就不用重新安装python了

   点击next

   <img src="assets\image-20230929180423251.png" alt="image-20230929180423251" style="zoom:50%;" />

   勾选如下，安装路径可以的话就放在C盘吧，因为python也算是相对比较重要的软件，点击install

   <img src="assets\image-20230929181314577.png" alt="image-20230929181314577" style="zoom:33%;" />

   

   安装完成，点击close

   <img src="assets\image-20230929181606449.png" alt="image-20230929181606449" style="zoom:33%;" />

   我们再次再powershell中输入python，此时就会显示python的版本信息。

   ![image-20230929181704808](assets\image-20230929181704808.png)

   

2. anaconda
   anaconda是一个很强大的管理工具，帮助你管理python的版本，创建不同版本的虚拟环境，

   <img src="assets\image-20230929174814540.png" alt="image-20230929174814540" style="zoom:33%;" />

   还是先卸载：

   <img src="assets\image-20230929181916724.png" alt="image-20230929181916724" style="zoom:33%;" />

   然后去[官网](https://www.anaconda.com/),点击Free Download
   ![image-20230929182019398](assets\image-20230929182019398.png)

   选择windows
   <img src="assets\image-20230929182105556.png" alt="image-20230929182105556" style="zoom:33%;" />

   下载好后，双击

   <img src="assets\image-20230929182146734.png" alt="image-20230929182146734" style="zoom:33%;" />

   

   next

   <img src="assets\image-20230929182220966.png" alt="image-20230929182220966" style="zoom: 33%;" />
   I agree

   <img src="assets\image-20230929182241771.png" alt="image-20230929182241771" style="zoom: 33%;" />

   all users吧，需要管理员授权

   <img src="assets\image-20230929182331912.png" alt="image-20230929182331912" style="zoom:33%;" />

   放在C盘可以的，如果空间够的话

   <img src="assets\image-20230929182413738.png" alt="image-20230929182413738" style="zoom:33%;" />

   全部勾选

   <img src="assets\image-20230929182450909.png" alt="image-20230929182450909" style="zoom:33%;" />

   等待安装完成，即可。点击Finish

   <img src="assets\image-20230929182918078.png" alt="image-20230929182918078" style="zoom:33%;" />


   然后它可能会跳出来一个绿色的圈圈，一会就会打开其主页，我们什么都不用管，

   点击**No,don't show again，然后直接退出**

   

   <img src="assets\image-20230929183115631.png" alt="image-20230929183115631" style="zoom:33%;" />

   **点击Yes**

   <img src="assets\image-20230929183253680.png" alt="image-20230929183253680" style="zoom:33%;" />
   此时你可以在应用里看到，Anaconda3这个文件夹
   ![image-20230929183413895](assets\image-20230929183413895.png)

   <img src="assets\image-20230929183358104.png" alt="image-20230929183358104" style="zoom:33%;" />
   右键Anaconda Prompt，更多，点击打开文件位置，此后，我们使用的最多的便是这个类似于专属于anaconda的终端模拟器

   <img src="assets\image-20230929183811989.png" alt="image-20230929183811989" style="zoom:33%;" />
   将其快捷方式发送到桌面快捷方式。

   <img src="assets\image-20230929183916333.png" alt="image-20230929183916333" style="zoom:33%;" />

   

   然后将其托到任务栏，直到出现链接，即可
   <img src="C:\Users\justin\Documents\Tencent Files\2094623381\nt_qq\nt_data\Pic\2023-09\Thumb\01edc775e5cbc51dad90c8174a4e2b50_720.png" alt="01edc775e5cbc51dad90c8174a4e2b50_720" style="zoom:33%;" />

   我们在任务栏中打开它并输入

   ```latex
   conda env list
   ```

   <img src="assets\image-20230929184245533.png" alt="image-20230929184245533" style="zoom:33%;" />

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

   ![image-20230929185850899](assets\image-20230929185850899.png)

   

   直到它出现，下图，输入y,并回车

   <img src="assets\image-20230929190032361.png" alt="image-20230929190032361" style="zoom:50%;" />
   便可以看到一些基础的包，和python3.10.6正在安装

   <img src="assets\image-20230929190114384.png" alt="image-20230929190114384" style="zoom:33%;" />
   安装完成
   <img src="assets\image-20230929190219779.png" alt="image-20230929190219779" style="zoom:33%;" />

   ```latex
   #输入 conda env list即可看到我们刚创建的base_learn虚拟环境（）
   ```

   <img src="assets\image-20230929190427967.png" alt="image-20230929190427967" style="zoom:33%;" />
   ```latex
   输入cls 并回车，来清屏
   
   ```

   ![image-20230929190530711](assets\image-20230929190530711.png)

   ```latex
   #进入虚拟环境（进入虚拟环境来管理第三方库）
   conda activate base_learn
   #可以看到前面的base变成了base_learn，前面的()代表我们目前在那个虚拟环境下
   ```

   <img src="assets\image-20230929190724972.png" alt="image-20230929190724972" style="zoom:33%;" />

   ```latex
   使用conda deactivate 退出当前虚拟环境
   ```

   <img src="assets\image-20230929190906367.png" alt="image-20230929190906367" style="zoom:33%;" />

   

3. 创建一个项目

   打开pycharm，点击 New Project
   <img src="assets\image-20230929192632817.png" alt="image-20230929192632817" style="zoom:33%;" />

   location代表项目位置最后的pythonProject代表项目名称

   

   <img src="assets\image-20230929192720496.png" alt="image-20230929192720496" style="zoom:33%;" />
   ```latex
   我们设置项目名称为baselearn
   选择虚拟环境为Previousls configured interpreter(之前配置的解释器（即我们之前创建的虚拟环境）)
   点击add local interpreter
   ```

   <img src="assets\image-20230929192906546.png" alt="image-20230929192906546" style="zoom:33%;" />

   ```latex
   点击conda enviroment
   选择 using existing enviroment 然后找到我们之前创建的base_learn
   点击ok
   ```

   <img src="assets\image-20230929193132246.png" alt="image-20230929193132246" style="zoom:33%;" />

   ```latex
   点击create
   ```

   <img src="assets\image-20230929193257316.png" alt="image-20230929193257316" style="zoom:33%;" />

   ```la
   等待下面进度条加载完成，表示我们的虚拟环境被读取完成
   ```

   <img src="assets\image-20230929193435526.png" alt="image-20230929193435526" style="zoom:33%;" />

   ```latex
   左下角这几个从上到下分别是
   控制台:主要用于程序的调式，debug
   包:运行代码的第三方库
   服务:比如网页服务，jupyter这种在线代码编辑
   终端:这个应该是之后用的最多的，安装第三方库啊之类的，git创建版本啊，都在这里
   报错:程序问题
   版本控制(git):显示版本信息，这个也很有用！我会在接下来的教程教会你如何使用git和githubg
   ```

   

   <img src="assets\image-20230929193738909.png" alt="image-20230929193738909" style="zoom:33%;" />

4. 项目管理之良好的文件管理方式
   ```latex
   通常，我们的项目有如下文件，文件夹
   project_name
   	--src(源代码)
   		--train.py
   		--test.py
   		--......
   	--data(数据文件，根据自己的项目来创建)
   		--example.csv
   		--train
   			--a.png
   			--b.png
   			--c.png
   			......
   		--test
   			--d.png
   			--e.png
   			--f.png
   			......
   	--assets(通常存放一些媒体文件，比如图标啊，图片啊，readme.md,介绍文档中的图片之类的)
   		--icon.svg
   		--pics
   			--ui.svg
   			......
   	main.py/run.py/app.py(一般情况下，这三个文件用于整个项目的启动)
   	README.md(项目介绍文档，使用markdown语言编写，markdown是一种轻量级的标记语言，可以用于记笔记，撰写文档等多种用途。)
   	requirement.txt(依赖文档，列出了该项目中所用到的第三方库)
   
   #在pycharm中右键项目选择new来创建对应的文件，或者文件夹
   比如我们现在要创建一个能够将两个csv文件合并的项目
   ```

   

   <img src="assets\image-20230930101323474.png" alt="image-20230930101323474" style="zoom:33%;" />

   

   创建一个表格，在文件类型处选择csv（逗号分隔符）文件类型

   ![image-20230930102758088](assets\image-20230930102758088.png)

   直接存放到我们的项目文件的data项目中，同理再创建一个csv文件，命名最好不要带中文，经常会出现编码问题，最好使用英文字母

   <img src="assets\image-20230930102856991.png" alt="image-20230930102856991" style="zoom:33%;" />

   ```latex
   此时可以看到我们的项目文件结构如下，是不是相对清晰明了
   ```

   <img src="assets\image-20230930103058446.png" alt="image-20230930103058446" style="zoom:33%;" />

   ```latex
   ok,我们现在需要合并这两个csv文件，解决方案有很多，
   在此教程中，我们选择使用pandas这个第三方库中的pd.concat来完成,代码如下：
   
   import pandas as pd #导入第三方库pandas并实例化一个对象叫pd
   
   #定义一个函数名叫con_csv,接受两个参数，file1，file2
   def con_csv(file1,file2):
       # 读取两个CSV文件
       df1 = pd.read_csv(file1)
       df2 = pd.read_csv(file2)
   
       # 使用concat函数合并两个数据框
       merged_df = pd.concat([df1, df2],axis=1)
   
       # 将合并后的数据框保存为新的CSV文件
       merged_df.to_csv('merged_file.csv', index=False)
   
   
   
   我们将代码复制到csv_con.py文件中,发现提示no module named 'pandas',表示我们没有pandas这个第三方库
   下面的PEP 8: E231 missing whitespace after ',':4 表示在第四行的,后面确实一个空格。（这种是代码美观性的提示，可以不予管理，但是你要是有强迫症，可以右键它，选择 show quick fixes 选择reformat the file）
   ```

   <img src="assets\image-20230930104204118.png" alt="image-20230930104204118" style="zoom:33%;" />

   ```latex
   在pycharm的左下角，点击终端模拟器
   输入conda install pandas，回车，在我们的虚拟环境中安装pandas
   ```

   <img src="assets\image-20230930104840770.png" alt="image-20230930104840770" style="zoom:33%;" />

   ```latex
   同样会输出很多调试信息（），直到最后提示你输入y/n 输入y回车即可
   ```

   <img src="assets\image-20230930104923848.png" alt="image-20230930104923848" style="zoom:33%;" />
   <img src="assets\image-20230930105010512.png" alt="image-20230930105010512" style="zoom:33%;" />

   ```latex
   等待安装成功,显示done，然后pycharm右下角会自动更新虚拟环境
   ```

   

   <img src="assets\image-20230930105418158.png" alt="image-20230930105418158" style="zoom:33%;" />
   <img src="assets\image-20230930105515303.png" alt="image-20230930105515303" style="zoom:33%;" />

   ```latex
   然后我们在终端中输入conda list即可看到我们安装的第三方库
   此时就可以看到我们的pandas版本是2.0.3，可以使用ctrl键+l清屏
   ```

   <img src="assets\image-20230930105755269.png" alt="image-20230930105755269" style="zoom:33%;" />

   ```latex
   可以看到我们的代码此时已经不再报错
   ```

   ![image-20230930105955744](assets\image-20230930105955744.png)

   

   ```latex
   此时我们创建两个路径的字符串，并调用上述函数，即可给我们创建出合并后的csv文件，并存放于代码文件的同级目录下
   
   import pandas as pd
   
   
   def con_csv(file1, file2):
       # 读取两个CSV文件
       df1 = pd.read_csv(file1)
       df2 = pd.read_csv(file2)
   
       # 使用concat函数合并两个数据框
       merged_df = pd.concat([df1, df2],axis=1)
   
       # 将合并后的数据框保存为新的CSV文件
       merged_df.to_csv('merged_file.csv', index=False)
   
   
   path1 = "../data/name_age.csv"
   path2 = "../data/score.csv"
   con_csv(path1, path2)
   ```

   ```latex
   ok，这里再提一下关于文件路径的问题，我们一般常用的是绝对路径和相对路径
   对于整个盘符来讲，绝对路径就是从你这个盘的最初开始一步一步去检索
   在pycharm中，我们可以，右键某个文件，或者文件夹，点击copy path/Reference
   然后会跳出来三个选项，第一个便是绝对路径，从c盘开始检索，一直到最后的文件名
   C:\Users\justin\PycharmProjects\baselearn\data\score.csv
   而相对路径则是从文件所在的文件夹开始检索
   data/score.csv
   在上述项目代码中，我们的路径前面为什么要加../呢?
   path1 = "../data/name_age.csv"
   path2 = "../data/score.csv"
   是因为我们的代码文件在src文件夹下，../代表的是上一级目录，
   ```

   

   <img src="assets\image-20230930111222484.png" alt="image-20230930111222484" style="zoom:50%;" />
   <img src="assets\image-20230930111346908.png" alt="image-20230930111346908" style="zoom:50%;" />
   ```latex
   csv_con.py要调用data下的文件就必须使用../来访问，
   当然也可以使用绝对路径
   # 绝对路径
   path1 = r"C:\Users\justin\PycharmProjects\baselearn\data\name_age.csv"
   path2 = r"C:\Users\justin\PycharmProjects\baselearn\data\score.csv"
   但是在使用绝对路径的时候一定要加上r，因为在python中有很多格式化输入与输出所用的特殊字符，
   比如\n,用于换行输出，
   ```

   <img src="assets\image-20230930111809138.png" alt="image-20230930111809138" style="zoom:33%;" />

   ```latex
   不在前面加r就会在代码中显示出特殊字符
   ```

   ![image-20230930112520133](assets\image-20230930112520133.png)

   ```latex
   添加了r便不会
   ```

   ![image-20230930112618709](assets\image-20230930112618709.png)

   ```latex
   通常我比较喜欢使用相对路径，
   相对路劲较短，且检索项目文件比较好检索
   ```

   ```latex
   ok 相信你已经运行成功，输出了最后的merged_file.csv
   ```

   name_age.csv

   ![image-20230930113022291](assets\image-20230930113022291.png)

   score.csv

   ![image-20230930112953928](assets\image-20230930112953928.png)

   合并后的merged_file.csv
   ![image-20230930112905614](assets\image-20230930112905614.png)

   

   ```latex
   一般情况下，我们完整的项目的代码文件只需要一个文件去驱动，你会在main.py/run.py/app.py这些文件中看到很多import
   此时我们也尝试将我们刚写的代码变成一个随处可调用的函数，将代码改成如下即可
   import pandas as pd
   
   
   def con_csv(file1, file2):
       # 读取两个CSV文件
       df1 = pd.read_csv(file1)
       df2 = pd.read_csv(file2)
   
       # 使用concat函数合并两个数据框
       merged_df = pd.concat([df1, df2], axis=1)
   
       # 将合并后的数据框保存为新的CSV文件
       merged_df.to_csv('merged_file.csv', index=False)
   ```

   ```latex
   我们在我们的main.py中，调用该函数，导入src中的csv_con.py模块，并重命名为con
   此时我们就可以使用con来调用csv_con.py中的所有函数
   在我们csv_con.py中只有一个函数，con_csv,
   这个时候我们便可使用con.con_csv()来调用该函数
   ```

   ![image-20230930113646630](assets\image-20230930113646630.png)


   ![image-20230930114402879](assets\image-20230930114402879.png)

   ```latex
   运行main.py,你便可得到一个csv文件于main在同一目录下
   或者你也可以自行定义存放的输出的文件的位置，比如我们在项目文件夹下创建一个output文件夹，
   并将csv_con.py中最后一行中的，改为如下：merged_df.to_csv('output/merged_file.csv', index=False)
   import pandas as pd
   
   
   def con_csv(file1, file2):
       # 读取两个CSV文件
       df1 = pd.read_csv(file1)
       df2 = pd.read_csv(file2)
   
       # 使用concat函数合并两个数据框
       merged_df = pd.concat([df1, df2], axis=1)
   
       # 将合并后的数据框保存为新的CSV文件
       merged_df.to_csv('output/merged_file.csv', index=False)
   ```

   ```latex
   此时我们再次运行main.py,就可以看到我们的输出的文件在output文件夹下
   ```

   <img src="assets\image-20230930114909107.png" alt="image-20230930114909107" style="zoom:50%;" />

   ```latex
   OK,此时你已经学会了基础的python项目的创建，配置，管理，也许在实际开发中还需要添加更多的其他的东西
   比如项目的说明文档，依赖需求，添加更多的测试数据，还有docker(我也还在学习中！！！)......等等等，
   很多时候我们不是做项目，可能只是学习，或者做一个简单东西不需要很复杂，我们确实没有必要创建这么多东西，
   通常一个项目文件夹下，有几个py文件，然后如果要进行数据操作，甚至不创建data文件夹，直接使用数据的文件名访问数据
   为了方便也都是可以的，但是如果你要做相对大型一点的项目，此时我认为就应该有一个比较整洁的项目结构，
   如第四点刚开始所展示的一样。
   而且创建项目的文件和文件夹的命名也没有确定的格式或者要求，
   但是最好是简洁，明了，易懂，这三点不仅是针对自己，同时也针对可能会访问到你的项目的人，比如工作中同组的开发人员之类的。
   ```

   <img src="assets\image-20230930115417955.png" alt="image-20230930115417955" style="zoom:50%;" />

   ```latex
   最后，我将向你展示如何去使用git管理自己的项目，并且上传到自己的github
   首先得安装git，我的电脑已经安装好了，现在我卸载重装一次。
   ```

   ![image-20230930120242577](assets\image-20230930120242577.png)

   1. 安装git

      git官网[git](https://git-scm.com/book/zh/v2/%E8%B5%B7%E6%AD%A5-%E5%AE%89%E8%A3%85-Git)	

   ```latex
   点击download
   ```

   <img src="assets\image-20230930120553022.png" alt="image-20230930120553022" style="zoom:33%;" />

   ```latex
   点击windows
   ```

   <img src="assets\image-20230930120654939.png" alt="image-20230930120654939" style="zoom:33%;" />

   ```latex
   选择Standalone installer中的64-bit，等待下载完成
   ```

   ![image-20230930120716464](assets\image-20230930120716464.png)

```latex
双击文件安装
```

<img src="assets\image-20230930120912839.png" alt="image-20230930120912839" style="zoom:33%;" />



```latex
next
```

<img src="assets\image-20230930121004377.png" alt="image-20230930121004377" style="zoom:33%;" />

```latex
这个软件可以随意安装在一个位置
```

<img src="assets\image-20230930121041990.png" alt="image-20230930121041990" style="zoom:33%;" />

```latex
勾选情况如下
```

<img src="assets\image-20230930121103921.png" alt="image-20230930121103921" style="zoom:33%;" />

```latex
后面的全部默认即可，安装完成后，我们打开power shell，输入git --version,即可看到我们所安装的git版本
```

![image-20230930121347562](assets\image-20230930121347562.png)

```latex
同时它也会在桌面创建一个快捷方式，这power shell中使用git和git bash中使用git没有差别
```

![image-20230930121443691](assets\image-20230930121443691.png)

```latex
ok,此时，我们再来介绍一下什么是git，git是一个版本管理工具，比如我们的项目，我们完成了一个功能，我们需要记录当前项目的状态，
方便之后做了修改，想回到这个版本，或者其他用途，最为明显的应用场景就是
你完成了某项目的某个功能，或者你即将做一个重大的修改，在修改前，你想保存一个当前项目的状态，方便做对比，或者害怕自己修改错误，
此时git就派上了用场，我们可以是使用git 来创建一个版本，比如1.0 ，使用
git commit -m "version1.0"
创建版本之后，你可以随时回到这个版本，这个版本的项目状态就是你创建的时候的的状态
git的使用很简单，但是我得先教你如何将其和github配合起来使用
github是全球最大的开源代码社区，你能在上面找到很多有意思的东西，比如什么AI相关的啊乱七八糟的什么都有。
```

```latex
注册一个github账号，可以使用qq邮箱，也可使用其他的邮箱，创建用户名的时候尽量简短一点
```

创建好github账号之后，我们就要配置git和github的链接,首先配置用户名和邮箱

```latex
#打开git bash，分别输入如下内容，
#配置用户名
git config --global user.name "test"
#配置邮箱
git config --global user.email abc@163.com


比如我的就是
git config --global user.name "Justin-12138"
git config --global user.email lz12138@mails.guet.edu.cn

最后，使用
git config --global --list
查看你的配置信息
```

![image-20230930123201465](assets\image-20230930123201465.png)



```latex
之后生成ssh密钥，在git bash中输入如下内容，
ssh-keygen -t rsa
第一次询问你密钥的保存位置，默认即可，回车
```

![image-20230930123409585](assets\image-20230930123409585.png)

```latex
默认回车
```

![image-20230930123701869](assets\image-20230930123701869.png)

```latex
再次回车
```

![image-20230930123735071](assets\image-20230930123735071.png)

```latex
此时可以看到创建成功，使用ctrl+l清屏
```

<img src="assets\image-20230930123759335.png" alt="image-20230930123759335" style="zoom:33%;" />



```latex
# 进入.ssh目录 在git bash中输入
cd .ssh
# 列出.ssh文件夹下的目录
ls
# 查看id_rsa.pub的文件内容，然后复制 
cat id_rsa.pub

```

![image-20230930124341696](assets\image-20230930124341696.png)

```latex
然后使用鼠标选中文件内容，右键并复制
```

![image-20230930124501015](assets\image-20230930124501015.png)



```latex
之后打开github，点击你的头像，并选择settings
```

<img src="assets\image-20230930124622365.png" alt="image-20230930124622365" style="zoom:33%;" />

```latex
在SSH and GPG keys中选择点击New SSH key
```

![image-20230930124718338](assets\image-20230930124718338.png)

```latex
title随便取什么都可，然后将你刚复制的ssh key粘贴到Key，点击add ssh key
```

<img src="assets\image-20230930124853529.png" alt="image-20230930124853529" style="zoom:33%;" />

```latex
然后输入密码确认即可
```

<img src="assets\image-20230930125022871.png" alt="image-20230930125022871" style="zoom:33%;" />

```latex
然后我们就可以看到我们刚刚创建的ssh Key了，这个ssh key 是用来我们方便拉取，并将代码上传到github的
它不同于其他的链接ssh链接更加稳定和安全，具体的传输原理你可以上网搜索一下，🆗，到这里我们的配置算是完成了，
接下来就是实际应用了
```

![image-20230930125128089](assets\image-20230930125128089.png)



首先创建一个新仓库

点击your repositories
<img src="assets\image-20230930125454876.png" alt="image-20230930125454876" style="zoom:33%;" />



点击右上角的new

<img src="assets\image-20230930125534616.png" alt="image-20230930125534616" style="zoom:33%;" />




```latex
第一个是项目名称，精良也还是相对简短一点
description是项目的描述，
public or private就是公开或者私有，公开代表大家都可以看，但是private就只有你自己可以和你授权的人可以看
add a readme.md代表的是创建一个项目说明文档
add.gitignore,代表的是，在我们本地的项目中，会创建一些不必要的配置文件，我们就没有必要上传到github，
我们选择python代表的是我们这个项目大概率是python主要代码，然后python的一些无需上传的配置文件会帮我们自动忽略掉
choose a license 代表的是选择开源协议，这个开源协议还有点复杂，不同的开源协议有不同的要求，
MIT协议大概是你可以用我的这个项目去商用啊什么都可以，
当然也有一些严苛的开源协议，比如你可以商用，但是比必须开源，等等
最后点击create repository
```

<img src="assets\image-20230930125632618.png" alt="image-20230930125632618" style="zoom:33%;" />

```latex
创建完成后，我们的项目就如下图所示，现在我们要把刚刚的那个合并csv的文件，作为一个项目上传到github的这个testrepo仓库中
```

<img src="assets\image-20230930130339741.png" alt="image-20230930130339741" style="zoom:33%;" />

```latex
第一步克隆仓库到本地，点击code，选择ssh，点击右边的复制即可
```

<img src="assets\image-20230930130522845.png" alt="image-20230930130522845" style="zoom:33%;" />

```latex
我们在桌面中右键，选择在终端中打开
并在终端中输入 
git clone 我们刚复制的仓库地址
比如，我的就是
git clone git@github.com:Justin-12138/testrepo.git
```

<img src="assets\image-20230930130725309.png" alt="image-20230930130725309" style="zoom:50%;" />



```latex
回车并等待克隆完成，同时也可在桌面中看到我们多了一个testrepo的文件夹
```

<img src="assets\image-20230930130937772.png" alt="image-20230930130937772" style="zoom:33%;" />

![image-20230930131029166](assets\image-20230930131029166.png)

```latex
点击进入，可以看到现在这个仓库中除了多了一个.git,其他的文件都是我们创建仓库的时候所自带的
```

<img src="assets\image-20230930131055088.png" alt="image-20230930131055088" style="zoom:33%;" />



```latex
此时，我们便可以将之前的python的项目文件复制到该文件夹中
并在终端中使用 git status 查看仓库状态
可以看到它提示我们标红的文件和文件夹未追踪（untracked）
这里就涉及到一个之前没讲到东西就是git如何进行版本管理
我这里就稍微提供一下简单的教程，其实git还有很多功能
比如我们现在向项目中添加，删除，更改了一些文件或者文件夹
我们想更好的管理他们都需要把他们放入暂存区
使用git add * 代表将所有文件都放入暂存区 你也可以使用git add 某文件或者某文件夹 将某文件或者某文件夹放入暂存区，
又或者说追踪这些文件或者文件夹，也许你看到这里有点懵，但是只要记住，你想使用git更好的去管理你的项目，管理版本
一般的步骤就是
修改某个文件，之后，使用
git add 某个文件

创建版本
git commit -m "我修改了这个文件的某个地方"

git push 上传到github
然后使用git log可以查看版本记录
接下来，我们就基于我们当前的项目来做一次演示
```

<img src="assets\image-20230930131554272.png" alt="image-20230930131554272" style="zoom:33%;" />


```latex
git add *
git status #再次查看git状态
git commit -m "第一次提交" #创建一个版本
git log #查看git log版本日志

```

<img src="assets\image-20230930132556193.png" alt="image-20230930132556193" style="zoom:33%;" />

```latex
git push #上传到github
```

<img src="assets\image-20230930132757807.png" alt="image-20230930132757807" style="zoom:33%;" />

```latex
刷新我们的github仓库，即可看到我们上传的文件
```

<img src="assets\image-20230930132839336.png" alt="image-20230930132839336" style="zoom: 33%;" />

```latex
ok
到这里也接近该教程的尾声了，本教程花费接近6小时完成，全程自己手打字完成，最后计数9000字有余，
去掉其中的一些非手写字数应有5000字左右，我做该教程的初衷便是让更多没有什么基础的同学(eg:jiojio)能够尽快的入门一些基础知识
本教程还有很多不完善的地方，
markdown语言的基础教程，
常用Linux操作密令，
操作系统基础知识，
git详细教程，
python其他虚拟环境的创建方式
这些基础的知识在我的baselearn的仓库中有所体现，希望你能够从中学到一些东西，或者帮我完善这个教程！
最后如果觉得本教程不错帮忙点个star！！！
```

