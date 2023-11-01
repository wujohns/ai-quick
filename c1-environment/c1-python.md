# python 环境准备
1. 目前主流的 ai 开发语言是 python  
1. 常用的 ai 开发框架是 pytorch  
1. 实际开发中我们会有多个项目，为了避免不同项目的相互干扰，这里在为指定的项目安装 pytorch 依赖之前，我们需要先搞定不同项目的python依赖隔离处理  

## 基础环境准备
在 python 的官网选择安装指定的 python 版本即可: https://www.python.org/downloads  
若已经装好的 python 且 python 的版本合适，可以跳过这一步  

## python 虚拟环境
我们采用 python 虚拟环境的策略实现对不同项目的隔离，其原理机制为:  
1. 在虚拟环境目录分开放置不同项目的依赖包  
1. 使用 `workon` 切换虚拟环境时，其会使用对应虚拟环境中的依赖    

安装步骤:  
1. `pip install virtualenv` 安装 `virtualenv`  
1. `pip install virtualenvwrapper-win`  
1. 添加环境变量 WORKON_HOME，该变量为虚拟环境放置的目录（例如 D:\Envs）  

使用:
1. 创建一个名为 `pytorch-learn` 的环境  
```bash
mkvirtualenv pytorch-learn
```

2. 查看当前虚拟环境列表
```bash
workon
```

3. 切换到名为 `pytorch-learn` 的环境  
```bash
workon pytorch-learn
```

4. 移除名为 `pytorch-learn` 的环境
```bash
rmvirtualenv pytorch-learn
```

## pytorch 的安装
在上述工作处理就绪后，我们创建一个名为 `ai-quick` 的环境
```bash
mkvirtualenv ai-quick
```

依据 pytorch 的官网，选择对应的版本，获取安装指令，进行安装，例如:  
![pytorch.png](/c1-environment/pytorch.png)

安装完成后，我们可以执行 [/c1-environment/version.py](/c1-environment/version.py) 进行确认
