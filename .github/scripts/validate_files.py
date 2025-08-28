#!/usr/bin/env python3

import json
import yaml
import sys
import os
import argparse


def validate_json(file_path):
    """Validate JSON file format"""
    try:
        with open(file_path, 'r') as f:
            json.load(f)
        print(f"✓ {file_path} is valid JSON")
        return True
    except json.JSONDecodeError as e:
        print(f"✗ {file_path} is invalid JSON: {e}")
        return False
    except Exception as e:
        print(f"✗ Error reading {file_path}: {e}")
        return False


def validate_yaml(file_path):
    """Validate YAML file format"""
    try:
        with open(file_path, 'r') as f:
            yaml.safe_load(f)
        print(f"✓ {file_path} is valid YAML")
        return True
    except yaml.YAMLError as e:
        print(f"✗ {file_path} is invalid YAML: {e}")
        return False
    except Exception as e:
        print(f"✗ Error reading {file_path}: {e}")
        return False


def find_files(directory, extension):
    """Find all files with given extension in directory"""
    files = []
    for root, dirs, filenames in os.walk(directory):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for filename in filenames:
            if filename.endswith(extension) and not filename.startswith('.'):
                files.append(os.path.join(root, filename))
    return files


def main():
    parser = argparse.ArgumentParser(description='Validate JSON and YAML files')
    parser.add_argument('--directory', '-d', default='.', help='Directory to scan for files')
    parser.add_argument('--check-json', action='store_true', help='Check JSON files')
    parser.add_argument('--check-yaml', action='store_true', help='Check YAML files')
    parser.add_argument('--changed-files', nargs='*', help='List of changed files to validate')
    
    args = parser.parse_args()
    
    if not args.check_json and not args.check_yaml:
        args.check_json = args.check_yaml = True
    
    all_valid = True
    
    # If changed files are provided, filter them by extension
    if args.changed_files:
        json_files = [f for f in args.changed_files if f.endswith('.json')]
        yaml_files = [f for f in args.changed_files if f.endswith('.yaml') or f.endswith('.yml')]
    else:
        # Otherwise, find all files in directory
        json_files = find_files(args.directory, '.json') if args.check_json else []
        yaml_files = []
        if args.check_yaml:
            yaml_files = find_files(args.directory, '.yaml')
            yaml_files += find_files(args.directory, '.yml')
    
    if args.check_json and json_files:
        print(f"Found {len(json_files)} JSON files to validate")
        for file_path in json_files:
            if not validate_json(file_path):
                all_valid = False
    
    if args.check_yaml and yaml_files:
        print(f"Found {len(yaml_files)} YAML files to validate")
        for file_path in yaml_files:
            if not validate_yaml(file_path):
                all_valid = False
    
    if not all_valid:
        sys.exit(1)
    else:
        print("All files are valid!")


if __name__ == "__main__":
    main()