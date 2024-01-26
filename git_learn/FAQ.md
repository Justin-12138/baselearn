# 常见error

#### 1.22: Connection timed out

```latex
git clone git@github.com:id/repo.git

Cloning into 'learnjs'...
ssh: connect to host github.com port 22: Connection timed out
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

具体原因我也说不清楚，起初按照[baselearn](https://github.com/Justin-12138/baselearn/tree/main/base_env)中的环境配置不会又任何问题，但是在使用一段时间之后，出现上述报错

此时可以在.ssh中添加config文件的方法来解决上述问题

config文件内容如下

```latex
Host github.com
Hostname ssh.github.com
Port 443
```

编辑后的.ssh文件夹

```latex
lz@justin:~/.ssh$ ls
config  id_rsa  id_rsa.pub  known_hosts  known_hosts.old
lz@justin:~/.ssh$ cat config
Host github.com
Hostname ssh.github.com
Port 443
```

