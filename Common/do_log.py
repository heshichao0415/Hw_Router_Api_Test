"""
# @Time    : 2019/8/29 19:33
# @Author  : 谢超
# @File    : do_log.py
# @Function: 
"""

import logging
# 按文件大小滚动备份
from logging.handlers import RotatingFileHandler
# 控制台日志输入颜色
import colorlog
import time
import datetime
import os

from Common import contants

# 如果不存在这个test_result文件夹，就自动创建一个
if not os.path.exists(contants.log_storage_file): os.mkdir(contants.log_storage_file)

# 报错信息设置成黄色，方便查看排查报错原因
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

        # 要删除文件的目录名
        dir_list = ['Logs']
        for dir in dir_list:

            # 拼接删除目录完整路径
            dirPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '\\' + dir

            # 返回按修改时间排序的文件list
            file_list = self.get_file_sorted(dirPath)

            # 目录下没有日志文件
            if file_list:
                for i in file_list:

                    # 拼接文件的完整路径
                    file_path = os.path.join(dirPath, i)
                    t_list = self.TimeStampToTime(os.path.getctime(file_path)).split('-')
                    now_list = self.TimeStampToTime(time.time()).split('-')

                    # 将时间转换成datetime.datetime 类型
                    t = datetime.datetime(int(t_list[0]), int(t_list[1]),
                                          int(t_list[2]))
                    now = datetime.datetime(int(now_list[0]), int(now_list[1]), int(now_list[2]))

                    # 创建时间大于6天的文件删除
                    if (now - t).days > 6:
                        self.delete_logs(file_path)

                # 限制目录下记录文件数量
                if len(file_list) > 4:
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

        # 日志输出格式
        formatter_fh = logging.Formatter(
            '%(asctime)s - %(name)s -  %(filename)s : %(lineno)d - %(levelname)s - %(message)s')
        formatter_ch = colorlog.ColoredFormatter(
            '%(log_color) s%(asctime)s - %(name)s - %(filename)s : %(lineno)d - %(levelname)s- %(message)s',
            log_colors=log_colors_config)

        self.handle_logs()

        # 创建一个FileHandler，用于写到本地
        # 使用RotatingFileHandler类，滚动备份日志
        fh = RotatingFileHandler(filename=contants.log_file, mode='a', maxBytes=1024 * 1024 * 5, backupCount=5,
                                 encoding='utf-8')
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
