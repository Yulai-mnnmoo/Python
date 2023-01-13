# Python包管理工具pip的常见使用方法

## 1.简介 

​	Python之所以简单好用，得益于的插件包，需要用到就是包管理工具pip，pip主要是用于安装 PyPI 上的软件包，可以替代 easy_install 工具。 

一般安装了Python后会自带安装pip工具，是否安装可以通过命令行输入pip。 

## 2.pip安装 

如果你安装的Python 2 >=2.7.9 或者Python 3 >=3.4 那么Python自带了pip,所以不用安装，配置下它的环境就可以了

注：如果同时装了Python2与Python3，直接使用pip可能会出现报错，由于本人是就是装了两个版本，操作时加上Python版本区分，如

Python2下的自我更新操作：

python2 -m pip install -U pip

Python3下的自我更新操作：

pip3 install -U pip        #python3下直接pip3使用，但是pip2就使用不了，可能是我默认Python3了。



## 3.pip的一些使用 

### 1）pip的自我更新

$ pip install -U pip

### 2）安装 PyPI软件包 

$ pip install SomePackage            # 最新版本 

$ pip install SomePackage==1.0.4      # 特定的版本 

$ pip install 'SomePackage>=1.0.4'    # 最低版本 

### 3）卸载安装包 

$ pip uninstall SomePackage 

### 4）查看列出已安装的软件包

$ pip list 

###  5）更新软件包 

$ pip install --upgrade six 

### 6）查看软件包的详细信息 

$ pip show six 

### 7）搜素软件包 

$ pip search "query" 

### 8）显示当前已经通过pip安装的包及版本号

$ pip freeze  

