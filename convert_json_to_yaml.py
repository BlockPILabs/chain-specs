#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import yaml

def set_None():
    # 遍历当前目录下的所有子目录
    for root, dirs, files in os.walk('.'):
        # 检查是否存在 DisableMethod.json 文件
        if 'DisableMethod.json' in files:
            json_path = os.path.join(root, 'DisableMethod.json')
            # 读取 JSON 文件 然后设置为空内容
            with open(json_path, 'w', encoding='utf-8') as f:
                try:
                    f.write('[]')
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON in {json_path}: {e}")
                    continue


def convert_json_to_yaml():
    # 遍历当前目录下的所有子目录
    for root, dirs, files in os.walk('.'):
        # 检查是否存在 DisableMethod.json 文件
        if 'DisableMethod.json' in files:
            json_path = os.path.join(root, 'DisableMethod.json')
            yaml_path = os.path.join(root, 'DisableMethod.yaml')

            print(f"Processing {json_path}")

            # 读取 JSON 文件
            with open(json_path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON in {json_path}: {e}")
                    continue

            # 转换为 YAML 格式
            yaml_content = "#\n"
            yaml_content += "default: # 等级(所有等级,其它等级没有配置方法时取这里方法配置)\n"

            # 添加每个禁用方法
            for method in data:
                yaml_content += f"  \"{method}\":\n"

            # 写入 YAML 文件
            with open(yaml_path, 'w', encoding='utf-8') as f:
                f.write(yaml_content)

            print(f"Converted {json_path} to {yaml_path}")

if __name__ == "__main__":
    # convert_json_to_yaml()
    set_None()
    print("completed.")