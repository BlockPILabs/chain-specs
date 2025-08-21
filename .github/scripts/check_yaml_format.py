#!/usr/bin/env python3
"""
YAML格式检查脚本
"""
import sys
import os
import glob
import yaml


def check_yaml_files():
    """检查YAML文件格式 """
    # 查找所有YAML文件
    yaml_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.yaml') or file.endswith('.yml'):
                yaml_files.append(os.path.join(root, file))
    
    print(f"Checking {len(yaml_files)} YAML files...")
    
    # 检查每个YAML文件
    errors = []
    exit_code = 0
    
    for file_path in yaml_files:
        try:
            with open(file_path, 'r') as f:
                yaml.safe_load(f)
            print(f"✓ {file_path}")
        except Exception as e:
            print(f"✗ {file_path}: {str(e)}")
            errors.append((file_path, str(e)))
            exit_code = 1
    
    # 报告结果
    if exit_code:
        print('\nYAML format check failed:')
        for file_path, error in errors:
            print(f'  {file_path}: {error}')
    
    return exit_code


def main():
    """主函数"""
    exit_code = check_yaml_files()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()