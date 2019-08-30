"""
# @Time    : 2019/8/29 19:33
# @Author  : 谢超
# @File    : do_log.py
# @Function: 
"""

import logging
from logging.handlers import RotatingFileHandler  # 按文件大小滚动备份
import colorlog  # 控制台日志输入颜色
import time
import datetime
import os

from Common import contants

if not os.path.exists(contants.log_storage_file): os.mkdir(contants.log_storage_file)  # 如果不存在这个test_result文件夹，就自动创建一个

log_colors_config = {
    'WARNING': 'yellow',
    'ERROR': 'yellow',
    'CRITICAL': 'yellow',
}


class MyLog:
    def __init__(self, log_name):
        self.log_name = log_name

    def get_file_sorted(self, file_path):
        """最后修改时间顺序升序排列 os.path.getmtime()->获取文件最后修改时间"""
        dir_list = os.listdir(file_path)
        if not dir_list:
            return
        else:
            dir_list = sorted(dir_list, key=lambda x: os.path.getmtime(os.path.join(file_path, x)))
            return dir_list

    def TimeStampToTime(self, timestamp):
        """格式化时间"""
        timeStruct = time.localtime(timestamp)
        return str(time.strftime('%Y-%m-%d', timeStruct))

    def handle_logs(self):
        """处理日志过期天数和文件数量"""
        dir_list = ['Logs']  # 要删除文件的目录名
        for dir in dir_list:
            dirPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '\\' + dir  # 拼接删除目录完整路径
            file_list = self.get_file_sorted(dirPath)  # 返回按修改时间排序的文件list
            if file_list:  # 目录下没有日志文件
                for i in file_list:
                    file_path = os.path.join(dirPath, i)  # 拼接文件的完整路径
                    t_list = self.TimeStampToTime(os.path.getctime(file_path)).split('-')
                    now_list = self.TimeStampToTime(time.time()).split('-')
                    t = datetime.datetime(int(t_list[0]), int(t_list[1]),
                                          int(t_list[2]))  # 将时间转换成datetime.datetime 类型
                    now = datetime.datetime(int(now_list[0]), int(now_list[1]), int(now_list[2]))
                    if (now - t).days > 6:  # 创建时间大于6天的文件删除
                        self.delete_logs(file_path)
                if len(file_list) > 4:  # 限制目录下记录文件数量
                    file_list = file_list[0:-4]
                    for i in file_list:
                        file_path = os.path.join(dirPath, i)
                        print(file_path)
                        self.delete_logs(file_path)

    def delete_logs(self, file_path):
        try:
            os.remove(file_path)
        except PermissionError as e:
            self.my_log().warning('删除日志文件失败：{}'.format(e))

    def my_log(self):
        logger = logging.getLogger(self.log_name)
        logger.setLevel("DEBUG")

        formatter_fh = logging.Formatter(
            '%(asctime)s - %(name)s -  %(filename)s : %(lineno)d - %(levelname)s - %(message)s')

        formatter_ch = colorlog.ColoredFormatter(
            '%(log_color) s%(asctime)s - %(name)s - %(filename)s : %(lineno)d - %(levelname)s- %(message)s',
            log_colors=log_colors_config)  # 日志输出格式

        self.handle_logs()

        # 创建一个FileHandler，用于写到本地
        fh = RotatingFileHandler(filename=contants.log_file, mode='a', maxBytes=1024 * 1024 * 5, backupCount=5,
                                 encoding='utf-8')  # 使用RotatingFileHandler类，滚动备份日志
        fh.setLevel("DEBUG")
        fh.setFormatter(formatter_fh)
        logger.addHandler(fh)
        # logger.removeFilter(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = colorlog.StreamHandler()
        ch.setLevel("DEBUG")
        ch.setFormatter(formatter_ch)
        logger.addHandler(ch)
        # logger.removeHandler(ch)

        return logger


if __name__ == "__main__":
    log = MyLog(__name__).my_log()
    log.debug("---测试开始----")
    log.info("操作步骤")
    log.warning("----测试结束----")
    log.error("----测试错误----")
