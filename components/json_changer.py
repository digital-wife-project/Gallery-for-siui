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

def loacl_project_json_reader(project_name: str):
    # 读取现有的JSON文件内容
    json_filepath = "./config/local_project.json"
    try:
        with open(json_filepath, 'r', encoding='utf-8-sig') as file:
            # 将JSON数据加载到字典中
            data = json.load(file)
            # 使用get方法安全地获取project_name的值，如果不存在则返回None
            return data.get(project_name)
    except FileNotFoundError:
        print(f"文件 {json_filepath} 未找到。")
    except json.JSONDecodeError:
        print(f"文件 {json_filepath} 不是有效的JSON格式。")
    except Exception as e:
        print(f"读取文件时发生错误: {e}")

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


