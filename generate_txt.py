import os

def generate_txt_files(folder_path):
    # 支持的图片扩展名
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
    
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 获取文件的完整路径
        file_path = os.path.join(folder_path, filename)
        
        # 检查是否是文件以及是否是图片文件
        if os.path.isfile(file_path) and os.path.splitext(filename)[1].lower() in image_extensions:
            # 获取文件名（不含扩展名）和扩展名
            name, _ = os.path.splitext(filename)
            
            # 生成 .txt 文件名
            txt_filename = name + '.txt'
            txt_file_path = os.path.join(folder_path, txt_filename)
            
            # 写入内容到 .txt 文件
            with open(txt_file_path, 'w') as txt_file:
                txt_file.write('A photo of circuit diagram.')
            
            print(f'Generated: {txt_file_path}')

# 指定图片文件夹路径
folder_path = 'datasets/1+2'  # 替换为实际路径

# 调用函数
generate_txt_files(folder_path)