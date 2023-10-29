# Docker

#### 0.前言

:star:

[使用docker手册学习docker](https://docs.docker.com/engine/reference/commandline/push/)



```latex
A self-sufficient runtime for containers

Common Commands:
  run         Create and run a new container from an image
  根据镜像，运行一个新的容器。镜像可能来源于本地，也可能来源于公开或者私有的仓库。
  如果我们直接运行一个本地没有的镜像，那么docker会在docker hub中搜索该镜像的最新版
  eg:
	(base) justin@justin:~$ docker run centos
	Unable to find image 'centos:latest' locally
	latest: Pulling from library/centos
	
 
  exec 重新进入一个正在运行的容器中
  docker exec -it /bin/bash
  比如使用docker
  
  ps          List containers
  -a 输出所有容器(docker ps 默认只输出正在运行的)
  -f 根据某条件过滤符合容器
  -n m 输出最近的m个容器
  -l 展示最新创建的容器包括所有的状态
  -q 只展示容器的ID
  -s 展示总文件大小(在原来的基础上添加size列)
  在实际使用中可以混合上面的参数
  eg:docker ps -aq #输出所有容器的ID 
  
  build 使用Dockerfile创建一个镜像
  eg:docker build -t cdf .
  -t
  
  pull        Download an image from a registry
  从仓库中拉取镜像(默认从docker hub中拉取镜像)
  docker pull ubuntu:18.04 #:后面可以选择tag用于指定的镜像版本
  不选择tag的话，默认选择最新版 :latest
  docker pull 可以选择不同的仓库，例如阿里云的镜像服务
  -a
  
  push        Upload an image to a registry
  推送镜像到仓库
  images      List images
  列出镜像
  login       Log in to a registry
  登录到镜像仓库
  logout      Log out from a registry
  登出
  search      Search Docker Hub for images
  查询镜像，从docker hub中
  version     Show the Docker version information
  docker的版本
  info        Display system-wide information
  docker info 用于显示 docker 的系统级信息，比如内核，镜像数，容器数等

Management Commands:
  builder     Manage builds
  buildx*     Docker Buildx (Docker Inc., v0.11.2)
  compose*    Docker Compose (Docker Inc., v2.21.0)
  container   Manage containers
  context     Manage contexts
  image       Manage images
  manifest    Manage Docker image manifests and manifest lists
  network     Manage networks
  plugin      Manage plugins
  system      Manage Docker
  trust       Manage trust on Docker images
  volume      Manage volumes

Swarm Commands:
  swarm       Manage Swarm

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  events      Get real time events from the server
  export      Export a container's filesystem as a tar archive
  history     Show the history of an image
  import      Import the contents from a tarball to create a filesystem image
  inspect     Return low-level information on Docker objects
  kill        Kill one or more running containers
  load        Load an image from a tar archive or STDIN
  logs        Fetch the logs of a container
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  wait        Block until one or more containers stop, then print their exit codes

```





#### 1.docker常规使用 

```latex
0.docker密令查询
eg:docker image --help 
1.查看docker版本：
docker -v
2.查看镜像
docker image ls
docker images
3.查询某个镜像
docker search --limit 3 hadoop #查询前三个hadoop镜像
docker search -f stars=7659 centos
4.拉取镜像
docker pull 镜像名
eg:docker pull ubuntu # 默认会拉取最新版本，但是可以添加版本说明
eg:docker pull ubuntu:23.10
5:运行镜像
docker run -it --rm ubuntu
docker run -d (后台)
-i 交互
-t 分配伪终端 tty
-it 一般一起使用
-p 端口映射 7860(宿主机):7860(docker分配)
-P docker随即分配
--name=test1 Container name
删除某个或者某几个镜像
docker rmi id或者name

6.查看容器运行情况
docker ps -alns
-a：列出当前正在运行+历史运行过的
-l:显示最近创建的容器
-n num:显示最近num个创建的容器
docker ps -n 3
ctrl+p
ctrl+q
-q:静默模式，只显示容器编号
7.容器的启停
启动已停止的容器
docker start ID/name
docker restart ID/name
docker stop ID/name
docker kill ID/name
docker rm ID/name
-f
docker rm -f $(docker ps -a -q)
8.容器的重新进入
关于后台运行 -d
docker run -d redis #启动redis
docker ps #查看进程
docker exec -it ID /bin/bash #重新进入
exit #退出但不结束
docker ps #查看进程

若使用 attach 重新进入再exit则会结束
docker attach ID
exit
docker ps
拷贝文件到主机
docker cp 356157101b65:/root/a.txt /home/justin/cs




什么是docker虚悬镜像？
docker system df


```

#### 2.项目实战

```latex
sequenceiq/hadoop-docker
https://blog.csdn.net/qq_31142553/article/details/96652775

docker cp /home/justin/hadoop/jar_files/hadoop-mapreduce-examples-2.6.0.jar 441813d4f91f:/usr/local/hadoop-2.6.0
https://blog.csdn.net/weixin_42037651/article/details/125483218
```

