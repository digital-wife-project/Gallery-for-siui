import json

def json_changer(project_name:str,launch_command):
    # JSON文件的路径
    file_path = './config/local_project'

    # 读取现有的JSON文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
    # 将JSON数据加载到字典中
        data = json.load(file)
    
        # 向字典中添加新项
        data.update(new_data)

        # 将更新后的字典写回JSON文件
    with open(file_path, 'w', encoding='utf-8') as file:
        # 将字典转换为JSON格式的字符串，并写入文件
        json.dump(data, file, ensure_ascii=False, indent=4)
    print("新项已添加到JSON文件。")



# 要添加的新项
new_data = {
    "new_key": "新值"
}

