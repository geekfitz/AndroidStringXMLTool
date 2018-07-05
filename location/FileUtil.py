# -*-coding:utf-8-*-
import os


class FileUtil(object):

    @staticmethod
    def make_dir(dir_path):
        if os.path.exists(str(dir_path)):
            pass
        else:
            os.mkdir(str(dir_path))
