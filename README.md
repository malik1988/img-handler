# 图片批量下载并合并成一个文件的工具

用于批量下载多个图片并合并。

## downloader

文件下载器，使用当前目录下`download.txt`中的所有链接下载文件，并按照编号保存。为后按照顺序合并提供方便。最后还引用了文件合并的模块，对文件进行合并。

```ini
; download.txt 内容
第一行为保存的文件夹名称
http://xxxx.jpg
http://xxxx.jpg
http://xxxx.jpg
http://xxxx.jpg

```


## aria2其实也可快速下载多个链接并重命名
使用方式如下：
`aria2c --input-file xxx.txt`

```ini
; txt 文件内容
http://xxxx.jpg
  out=aaa.jpg  
http://xxxx.jpg
  out=aaa.jpg  

```

# --- 一个图片拼接工具 ---    

**本软件能将用户输入的多张图片进行拼接, 拼接后生成一张新图片**    

*如果在使用本软件过程中有疑问 / bug, 欢迎提 [issue](https://github.com/xiaomingTang/img-handler/issues)*

windows 可执行程序见[https://github.com/xiaomingTang/img-handler/releases/tag/0.0.2](https://github.com/xiaomingTang/img-handler/releases/tag/0.0.2)    

### 使用方式
* 直接将多个图片或文件夹拖拽到.exe文件, 然后选择相应的配置就行了
* 如果图片尺寸较大/较多, 可能拼接会有些慢, 请耐心等候
* 【ctrl + C】可终止程序

### feature
* 支持【".png", ".jpg", ".jpeg", ".bmp", ".ico", ".tga", ".tiff"】后缀的文件
* 支持 瀑布流 布局 和按 文件名 排序
* 支持 水平 和 竖直 排列
* 能识别经看图软件旋转过的图片
