## 这里用来记录每天遇到的问题

### 20180806

问题描述：安装hue的时候
sudo make apps  
/bin/bash: mvn: command not found
昨天还能通过，今天就报错，问题比较诡异。查了一下，这个问题很简单：
原理是：sudo在启动时，会启动默认的环境变量来代替本用户的环境变量，所以出现了上面的问题。
sudo启动的默认环境变量位置： /etc/sudoers中的
Defaults secure_path = /sbin:/bin:/usr/sbin:/usr/bin:/home/hue/dependency/apache-maven-2.2.1/bin

加入后，重新执行sudo make apps命令，过关！
[ref](http://blog.sina.com.cn/s/blog_40d46ec20101f97l.html)