import argparse
import re
import cv2  #OpenCV包
import numpy as np


def read_binary_file_uint8():
    """
    从命令行读取二进制文件路径并打开文件
    
    Returns:
        file: ndarray 存储的二进制文件数据
    """
    parser = argparse.ArgumentParser(description='读取二进制文件路径')
    parser.add_argument('-f', '--file', type=str, required=True, help='二进制文件路径')
    
    args = parser.parse_args()
    
    try:
        file_obj = open(args.file, 'rb')
        data = np.fromfile(file_obj, dtype=np.uint8)
        file_obj.close()
        return data
    except FileNotFoundError:
        print(f"错误: 找不到文件 '{args.file}'")
        return None
    except Exception as e:
        print(f"打开文件时发生错误: {str(e)}")
        return None


def read_file_all():
    """
    命令行读取文件所有内容
    Returns:
        file: 文件路径
    """
    parser = argparse.ArgumentParser(description='读取二进制文件路径')
    parser.add_argument('-f', '--file', type=str, required=True, help='二进制文件路径')
    
    args = parser.parse_args()
    
    return args.file

def show_img(img_obj):
        """
        显示图像
        Args:
            img_obj: ndarray 存储的图像数据
        """
        cv2.imshow('Raw Image', img_obj)
        cv2.waitKey(0)
        cv2.destroyAllWindows()