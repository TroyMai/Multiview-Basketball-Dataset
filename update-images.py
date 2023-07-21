import os
import re
import shutil


image_paths = []
# 遍历当前目录下的所有md文件
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.md'):
            md_file_path = os.path.join(root, file)

            # 打开md文件并查找图片路径
            with open(md_file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                pattern = r'!\[.*?\]\((.*?)\)'
                image_paths+=re.findall(pattern, content)

# 遍历图片路径，删除asset文件夹中不包含在md文件中的图片
for image_path in os.listdir('assets'):
    print("./assets/"+image_path)
    if "./assets/"+image_path not in image_paths:
        image_path = os.path.join('assets', image_path)
        os.remove(image_path)
        print('删除图片：', image_path)