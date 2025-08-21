#!/usr/bin/env python3
"""
JSON格式检查脚本
"""
import sys
import os
import json


def check_json_files():
    """检查JSON文件格式"""
    # 查找所有JSON文件
    json_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.json'):
                json_files.append(os.path.join(root, file))
    
    print(f"Checking {len(json_files)} JSON files...")
    
    # 检查每个JSON文件
    exit_code = 0
    for file_path in json_files:
        try:
            with open(file_path, 'r') as f:
                json.load(f)
            print(f"✓ {file_path}")
        except Exception as e:
            print(f"✗ {file_path}: {str(e)}")
            exit_code = 1
    
    return exit_code


def main():
    """主函数"""
    exit_code = check_json_files()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()