[python中的全局变量,出现referenced before assignment的解决方案](http://zhouzaibao.iteye.com/blog/559381)

### jupyter增加内核
[jupyter 添加内核](https://www.cnblogs.com/Jeffiy/p/4861528.html)
本例的Jupyter安装在Python3下，以增加Python2内核为例。
首先确认在Python3下已安装了内核：
ipython kernel install --user
#or
python3 -m ipykernel install --user
然后确保Python2下安装了ipykernel
sudo pip2 install -U ipykernel
然后运行如下命令：
python2 -m ipykernel install --user
至此，运行jupyter notebook你将看到如下所示：