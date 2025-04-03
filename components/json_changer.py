import json

def json_changer(json_file_path:str,project_name:str,project_path:str):
    new_data={project_name:project_path}
    # 读取现有的JSON文件内容
    with open(json_file_path, 'r', encoding='utf-8-sig') as file:
    # 将JSON数据加载到字典中
        data = json.load(file)
    
        # 向字典中添加新项
        data.update(new_data)

        # 将更新后的字典写回JSON文件
    with open(json_file_path, 'w', encoding='utf-8-sig') as file:
        # 将字典转换为JSON格式的字符串，并写入文件
        json.dump(data, file, ensure_ascii=False, indent=4)
    print("新项已添加到JSON文件。")

def loacl_project_json_reader(project_name:str):
    # 读取现有的JSON文件内容
    json_file_path="./config/local_project.json"
    with open(json_file_path, 'r', encoding='utf-8-sig') as file:
        # 将JSON数据加载到字典中
        data = json.load(file)
    if data[project_name]:
        return data[project_name]
    else:
        return None

def remote_project_json_reader(project_class:str):
    # 读取现有的JSON文件内容
    json_file_path="./config/avaliable_remote_project.json"
    with open(json_file_path, 'r', encoding='utf-8-sig') as file:
        # 将JSON数据加载到字典中
        data = json.load(file)
    if data[project_class]:
        return data[project_class]
    else:
        return None


