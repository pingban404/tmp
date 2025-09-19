import numpy as np
    

def raw_4ch_noremosic(image):
    raw_data= np.zeros((image.shape[0]//4, image.shape[1]//4, 16), dtype=np.uint8)
    raw_data[::,::,0]= image[::4,::4]
    raw_data[::,::,1]= image[::4,1::4]
    raw_data[::,::,2]= image[::4,2::4]
    raw_data[::,::,3]= image[::4,3::4]
    raw_data[::,::,4]= image[1::4,::4]
    raw_data[::,::,5]= image[1::4,1::4]
    raw_data[::,::,6]= image[1::4,2::4]
    raw_data[::,::,7]= image[1::4,3::4]
    raw_data[::,::,8]= image[2::4,::4]
    raw_data[::,::,9]= image[2::4,1::4]
    raw_data[::,::,10]= image[2::4,2::4]
    raw_data[::,::,11]= image[2::4,3::4]
    raw_data[::,::,12]= image[3::4,::4]
    raw_data[::,::,13]= image[3::4,1::4]
    raw_data[::,::,14]= image[3::4,2::4]
    raw_data[::,::,15]= image[3::4,3::4]

    # 0通道提取
    mosaic_0 = np.zeros((2 * raw_data.shape[0], 2 * raw_data.shape[1]), dtype=np.uint8)
    mosaic_0[0::2, 0::2] = raw_data[::,::,0]  
    mosaic_0[0::2, 1::2] = raw_data[::,::,1]  
    mosaic_0[1::2, 0::2] = raw_data[::,::,4]  
    mosaic_0[1::2, 1::2] = raw_data[::,::,5]  

    # 1通道提取
    mosaic_1 = np.zeros((2 * raw_data.shape[0], 2 * raw_data.shape[1]), dtype=np.uint8)
    mosaic_1[0::2, 0::2] = raw_data[::,::,2]  
    mosaic_1[0::2, 1::2] = raw_data[::,::,3]  
    mosaic_1[1::2, 0::2] = raw_data[::,::,6]  
    mosaic_1[1::2, 1::2] = raw_data[::,::,7]  

    # 2通道提取
    mosaic_2 = np.zeros((2 * raw_data.shape[0], 2 * raw_data.shape[1]), dtype=np.uint8)
    mosaic_2[0::2, 0::2] = raw_data[::,::,8]  
    mosaic_2[0::2, 1::2] = raw_data[::,::,9]  
    mosaic_2[1::2, 0::2] = raw_data[::,::,12]  
    mosaic_2[1::2, 1::2] = raw_data[::,::,13]  

    # 3通道提取
    mosaic_3 = np.zeros((2 * raw_data.shape[0], 2 * raw_data.shape[1]), dtype=np.uint8)
    mosaic_3[0::2, 0::2] = raw_data[::,::,10]  
    mosaic_3[0::2, 1::2] = raw_data[::,::,11]  
    mosaic_3[1::2, 0::2] = raw_data[::,::,14]  
    mosaic_3[1::2, 1::2] = raw_data[::,::,15]  

    mosaic=np.stack((mosaic_0, mosaic_1, mosaic_2, mosaic_3),axis=-1)
    return mosaic

def simple_test():
    """
    简单测试，验证通道分割逻辑
    """
    # 创建一个简单的4x4测试图像
    simple_image = np.array([
        [255, 255, 0, 0,255,255,0,0], 
        [255, 255, 0, 0,255,255,0,0], 
        [0, 0, 255, 255,0,0,255,255], 
        [0, 0, 255, 255,0,0,255,255],
        [255, 255, 0, 0,255,255,0,0], 
        [255, 255, 0, 0,255,255,0,0], 
        [0, 0, 255, 255,0,0,255,255], 
        [0, 0, 255, 255,0,0,255,255],
        [255, 255, 0, 0,255,255,0,0], 
        [255, 255, 0, 0,255,255,0,0], 
        [0, 0, 255, 255,0,0,255,255],
        [0, 0, 255, 255,0,0,255,255],
        [255, 255, 0, 0,255,255,0,0],
        [255, 255, 0, 0,255,255,0,0],
        [0, 0, 255, 255,0,0,255,255],
        [0, 0, 255, 255,0,0,255,255],
    ], dtype=np.uint8)
    print(simple_image.shape)
    for i in range(4):
        print(f'通道{i}:\n{raw_4ch_noremosic(simple_image)[::,::,i]}')

    
 

if __name__ == "__main__":
    simple_test()
