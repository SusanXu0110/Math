import re

# 设置要处理的 Markdown 文件路径
markdown_file_path = "数学workshop.md"
images_subdirectory = "./images"

# 正则表达式匹配 ![[...]] 形式的图片链接
pattern = re.compile(r"!\[\[(.*?)\]\]")


def replace_links_in_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    def replace_link(match):
        # 获取匹配到的内容
        link = match.group(1)
        # 替换内容中的空格为 %20
        link = link.replace(" ", "%20")
        # 构建新的链接格式
        return f"![]({images_subdirectory}/{link})"

    # 使用自定义替换函数
    new_content = pattern.sub(replace_link, content)

    # 保存修改
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(new_content)


# 处理单个 Markdown 文件
replace_links_in_file(markdown_file_path)
