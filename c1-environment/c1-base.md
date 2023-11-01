# 基础环境准备
在进行对应的 ai 开发工作前，需要对开发环境进行准备，准备的内容包含:  
1. nvidia 驱动  
1. cuda - cuda-toolkit  
1. cudnn - 基于 cuda 的深度学习 GPU 加速库，被较多的框架依赖，具体内容为一系列的头文件，以及针对对应平台编译的 .lib 或 .so 文件  

备注:  
1. 本章节主要为在 win10 下的配置操作  
1. linux 的配置操作整体思路和该章节类似，但是在部分地方略有不同，会在本章节的末尾做说明  

## 环境准备的对应关系
为了更方便理解在环境准备阶段所作的内容，这里绘制了一张环境结构图解，作为参考:  
![env-struc.png](/c1-environment/env-struc.png)

## nvidia 驱动
1. 首先确认自身设备的 GPU 型号  
1. 在 nvidia 官网按照型号手动搜索对应的驱动: https://www.nvidia.cn/geforce/drivers  
1. 驱动安装后，在命令行中执行 `nvidia-smi` 即可查看对应的驱动信息  

作为参考:
MX150 显卡在 win10 下安装完 545.92 版本的驱动后，执行 `nvidia-smi`，显示信息如下:  
![mx150.png](/c1-environment/mx150.png)

## cuda
1. 先在 cuda 版本与驱动版本对应表中确认可安装的 cuda 版本: https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html#cuda-major-component-versions  
1. 再到 cuda 的下载页面下载安装指定的 cuda: https://developer.nvidia.com/cuda-toolkit-archive  

安装后的一些检查:  
1. cuda 安装后在命令行执行 `nvcc --version` 可查看对应的 cuda 版本  
1. 在 win10 环境下默认安装流程中 cuda 会安装在 `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA` 路径下  

## cudnn
1. 依据上述安装的 cuda 版本，确认需要下载的 cudnn 版本: https://developer.nvidia.com/rdp/cudnn-archive  
1. 下载 cudnn 时需要在 nvidia 对应的官网上登陆账号(没有账号的话可以使用邮箱注册一个)  
1. 下载的内容为一个压缩包，解压后里面有 `bin` `include` `lib` 三个目录(linux 环境则只有 `include` `lib` 两个目录)  

将 `bin` `include` `lib` 文件夹中的文件复制到 cuda 的安装路径同名文件夹即可，如图:  
![cudnn-win10.png](/c1-environment/cudnn-win10.png)

## linux 环境的一些问题
本章节中的操作均为在 win10 下的操作为准，在 linux 环境下有以下不同之处:  
### 驱动安装部分  
在 linux 环境下对驱动的安装需要使用如下方式:  
安装前的准备工作： 
1. 卸载旧有的 nvidia 驱动 `apt-get remove --purge nvidia*`  
1. 安装可能需要的依赖 `apt-get install dkms build-essential linux-headers-generic`  
1. 编辑(若文件不存在则创建)文件 `/etc/modprobe.d/blacklist-nouveau.conf`，添加以下内容，将 nouveau 驱动加入黑名单:  
```conf
blacklist nouveau
blacklist lbm-nouveau
options nouveau modeset=0
alias nouveau off
alias lbm-nouveau off
```
编辑后执行 `update-initramfs -u`，并重启电脑，重启后执行 `lsmod | grep nouveau` 若没有输出则表明禁用 nouveau 驱动成功  

驱动安装，这里以下载的 `NVIDIA-Linux-x86_64-545.23.06.run` 为例： 
1. 执行
```sh
chmod u+x NVIDIA-Linux-x86_64-545.23.06.run
./NVIDIA-Linux-x86_64-545.23.06.run
```
进行驱动安装  
1. 安装完成后进行重启，并在重启后执行 `nvidia-smi` 检查驱动是否安装成功，作为参考 P40 显卡在 ubuntu22 下安装完 545.23.06 版本的驱动后，执行 `nvidia-smi`，显示信息如下:   
![p40.png](/c1-environment/p40.png)

### cudnn 安装部分
1. 在 https://developer.nvidia.com/rdp/cudnn-archive 下载需要的 cudnn  
1. 下载时选择 Tar 包的方式，解压 Tar 包并按照如下操作复制到对应的目录即可:  
```bash
# 这里以 8.9.5.30 为例子
tar -xvf cudnn-linux-x86_64-8.9.5.30_cuda12-archive.tar.xz

cp cudnn-*-archive/include/cudnn*.h /usr/local/cuda/include 
cp -P cudnn-*-archive/lib/libcudnn* /usr/local/cuda/lib64 
chmod a+r /usr/local/cuda/include/cudnn*.h /usr/local/cuda/lib64/libcudnn*
```
