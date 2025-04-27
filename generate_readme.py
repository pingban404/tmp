import os
import re

def get_py_files_info():
    """获取所有Python文件的信息"""
    files_info = []
    for file in os.listdir('.'):
        if file.endswith('.py') and file != 'generate_readme.py':
            with open(file, 'r', encoding='utf-8') as f:
                first_line = f.readline().strip()
                # 提取注释内容
                comment = re.sub(r'^#\s*', '', first_line) if first_line.startswith('#') else ''
                files_info.append({
                    'name': file,
                    'description': comment
                })
    return files_info

def generate_markdown():
    """生成Markdown内容"""
    # 读取现有的README内容
    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            existing_content = f.read()
    except FileNotFoundError:
        existing_content = "# 仓库简介\n这是一个python笔记临时仓库，\n\n"

    # 生成文件列表部分
    files_info = get_py_files_info()
    markdown = existing_content.rstrip() + "\n\n## Python 文件列表\n\n"
    markdown += "| 文件名 | 描述 |\n"
    markdown += "|--------|------|\n"
    
    for file_info in files_info:
        markdown += f"| {file_info['name']} | {file_info['description']} |\n"
    
    return markdown

if __name__ == "__main__":
    markdown_content = generate_markdown()
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(markdown_content) 