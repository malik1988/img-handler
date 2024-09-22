# 请使用Python 3.7
# encoding: utf-8
import os
import time
import asyncio
import aiohttp
from logger import logger

basepath = os.path.abspath(os.path.dirname(__file__))  # 当前模块文件的根目录


def setup_down_path(target):
    '''设置图片下载后的保存位置，所有图片放在同一个目录下'''
    down_path = os.path.join(basepath, 'download',target)
    if not os.path.isdir(down_path):
        os.makedirs(down_path,exist_ok=True)
        logger.info('Create download path {}'.format(down_path))
    return down_path


def get_links():
    '''获取所有图片的下载链接'''
    with open(os.path.join(basepath, 'download.txt'),encoding='utf-8') as f:  # 图片名都保存在这个文件中，每行一个图片名
        target = f.readline().replace('\n','')
        return target, f.readlines()


async def download_one(session, image):
    logger.info('Downloading No.{} [{}]'.format(
        image['linkno'], image['link']))
    t0 = time.time()

    async with session.get(image['link']) as response:
        # Binary Response Content: access the response body as bytes, for non-text requests
        image_content = await response.read()

    filename = f"{image['linkno']}{os.path.splitext(image['link'])[1]}"
    with open(os.path.join(image['path'], filename), 'wb') as f:
        f.write(image_content)

    t1 = time.time()
    logger.info('Task No.{} [{}] runs {:.2f} seconds.'.format(
        image['linkno'], image['link'], t1 - t0))


async def download_many():
    target, links = get_links()
    save_path = setup_down_path(target)

    tasks = []  # 保存所有任务的列表
    async with aiohttp.ClientSession() as session:  # aiohttp建议整个应用只创建一个session，不能为每个请求创建一个seesion
        for linkno, link in enumerate(links, 1):
            image = {
                'path': save_path,
                'linkno': linkno,  # 图片序号，方便日志输出时，正在下载哪一张
                'link': link.replace('\n','')
            }
            # asyncio.create_task()是Python 3.7新加的，否则使用asyncio.ensure_future()
            task = asyncio.create_task(download_one(session, image))
            tasks.append(task)
        results = await asyncio.gather(*tasks)
        return (len(results),save_path)

if __name__ == '__main__':
    t0 = time.time()
    count,save_path = asyncio.run(download_many())
    msg = '{} flags downloaded in {:.2f} seconds.'
    logger.info(msg.format(count, time.time() - t0))
    from img_merger import merge
    merge(save_path)
