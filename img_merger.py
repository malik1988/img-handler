import os
from pathlib import Path
from 图片拼接工具 import *


def merge(dir):

    sufix = [".png", ".jpg", ".jpeg",
             ".bmp", ".ico", ".tga", ".tiff"]
    in_files = [Path(os.path.join(dir, x)) for x in os.listdir(dir)]
    files = [x for x in in_files if x.suffix.lower() in sufix]
    files.sort(key=lambda item: int(item.stem))

    result = os.path.basename(dir)
    first_img = openWithRotateFromExif(files[0])
    mergeVertical(files, width=first_img.size[0]).save(
        os.path.join(dir, f'merg-{result}.jpg'), optimize=True, quality=92, progressive=True, subsampling=1)


if __name__ == '__main__':
    root='download'
    for dir in os.listdir(root):
        path=os.path.join(root,dir)
        if os.path.isdir(path):
            merge(path)
