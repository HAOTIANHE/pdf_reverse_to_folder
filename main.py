import fitz
import os
import cv2 # 加载OpenCV
import matplotlib.pyplot as plt # 加载Matplotlib.pyplot存进plt

def mkdir(path):
    folder=os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
    else:
        pass

def pdf2img(pdfpath,imgpath,dpi_num):
    pdf=fitz.open(pdfpath)
    name=pdf.name
    name = name.replace('pdfs/', '').replace('.pdf', '')
    for pg in range(0, pdf.page_count):
        page = pdf[pg]      
        pix = page.get_pixmap(dpi=dpi_num)
        # 开始写图像
        mkdir(imgpath )
        pix.save(imgpath  + '/' + str(pg + 1) + ".png")

        img = cv2.imread(imgpath  + '/' + str(pg + 1) + ".png") # 读取/加载 图片

        img_flip_along_x = cv2.flip(img, 1) # 把围绕X轴翻转的图像存进img_flip_along_x
        # plt.imshow(img_flip_along_x) # 显示img_flip_along_x图像
        cv2.imwrite(imgpath  + '_r/' + str(pg + 1) + "_r.png", img_flip_along_x)
        
    pdf.close()

pdfpath='./尺码镜面打印2.pdf'
imgpath='./img'
dpinum=300


import shutil

folder_path = "./img_r"
#如果没有文件夹就创建文件夹
if not os.path.exists(imgpath):
    os.mkdir(imgpath)
    print('创建文件夹 '+imgpath+' 成功')
else:
    print('文件夹 '+imgpath+' 已存在')
if not os.path.exists(folder_path):
    os.mkdir(folder_path)
    print('创建文件夹 '+folder_path+' 成功')
else:
    print('文件夹 '+folder_path+' 已存在')

# 删除文件夹下的所有文件
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print(f"Failed to delete {file_path}. Reason: {e}")




pdf2img(pdfpath,imgpath,dpinum)

# import zipfile
# import os

# def zipdir(path, ziph):
#     # ziph 是 zipfile.ZipFile() 对象
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             ziph.write(os.path.join(root, file))

# if __name__ == '__main__':
#     # 指定要打包的文件夹路径
#     dir_to_zip = './img_r'
#     zip_file_name = 'img_r.zip'
#     zip_file_path = os.path.join(dir_to_zip, zip_file_name)

#     # 创建 ZipFile 对象并添加文件
#     zipf = zipfile.ZipFile(zip_file_path, "w", zipfile.ZIP_DEFLATED, allowZip64=True)
#     zipdir(dir_to_zip, zipf)
#     zipf.close()

#     print('打包完成！')

