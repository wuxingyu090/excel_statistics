import os
from pathlib import Path

# 获取当前脚本文件所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))


class OsPathClass:
    def __init__(self, input_file=None, output_file=None, data_file=None):
        self.input_file = input_file
        self.output_file = output_file
        self.data_file = data_file

    def input_path(self):
        if self.input_file is not None:
            # 构建文件路径
            path = current_dir + '/../../input/' + self.input_file
            input_path = str(Path(path))
            return input_path
        else:
            raise FileNotFoundError("input_file can't None!")

    def output_path(self):
        if self.output_file is not None:
            # 构建文件路径
            path = current_dir + '/../../output/' + self.output_file
            output_path = str(Path(path))
            return output_path
        else:
            raise FileNotFoundError("output_file can't None!")

    def data_path(self):
        if self.data_file is not None:
            # 构建文件路径
            path = current_dir + '/../../' + self.data_file
            data_path = str(Path(path))
            return data_path
        else:
            raise FileNotFoundError("data_file can't None!")
