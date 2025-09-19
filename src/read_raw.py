

from ast import main
import time
from numpy import shape, size
from iofile import *

# 首先确定原图片的基本信息：数据格式，行数列数，通道数
# rows=448*3#图像的行数
# cols=448*3#图像的列数
# channels =3# 图像的通道数，灰度图为1

# img_path='./examples/0.jpg'

# # 利用numpy的fromfile函数读取raw文件，并指定数据格式
# # 读取图片
# img_array = cv2.imread(img_path)
# img = np.asarray(img_array)

# cv2.imshow(winname=' ',mat=img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 直接指定文件路径（推荐用于测试）
# file_path = './examples/lena512.raw'  # 替换为你的文件路径
# try:
#     data = np.fromfile(file_path, dtype=np.uint16)
#     print(f"读取到 {len(data)} 个 uint16 数据")
#     print(f"数据形状: {data.shape}")
#     print(f"前10个数据: {data[:10]}")
    
#     # 如果需要将数据重塑为图像
#     # 假设是512x512的图像
#     if len(data) == 512 * 512:
#         image = data.reshape(512, 512)
#         print(f"图像形状: {image.shape}")
#         print(f"图像数据类型: {image.dtype}")
        
#         # 显示图像（需要转换为8位）
#         image_8bit = (image / 256).astype(np.uint8)
#         cv2.imshow('Raw Image', image_8bit)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()
    
# except FileNotFoundError:
#     print(f"错误: 找不到文件 '{file_path}'")
# except Exception as e:
#     print(f"读取文件时发生错误: {str(e)}")

# 方法1：使用命令行参数读取文件（如果需要）
def main():
    import os
    
    folder_path = r'E:\examples\canon'
    
    # 获取文件夹中的所有图片文件
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
    
    # 循环显示每张图片
    for image_file in image_files:
        img_path = os.path.join(folder_path, image_file)
        img_array = cv2.imread(img_path)
        print(img_array.shape)
        if img_array is None:
            print(f"无法读取图片: {img_path}")
            continue

        # 显示图片
        cv2.imshow(winname='window', mat=img_array)
        
        # waitKey需要在imshow之后立即调用,否则图片无法正常显示
        # waitKey(0)表示无限等待按键
        key = cv2.waitKey(10000)
        
        # 关闭当前图片窗口
        cv2.destroyAllWindows()
        
        # 如果按ESC键则退出循环
        if key == 27:
            break


if __name__ == "__main__":
    main()