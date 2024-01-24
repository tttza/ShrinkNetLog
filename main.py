import json
import argparse

def remove_bytes_from_json(file_path):

    # JSONファイルを読み込む
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    new_events = []
    for x in data['events']:
        keys = x.keys()
        if 'params' in keys:
            if 'bytes' in x['params']:
                del x['params']['bytes']
        new_events.append(x)

    data['events'] = new_events

    # 修正されたデータを新しいファイルに保存
    new_file_path = file_path.replace('.json', '_modified.json')
    with open(new_file_path, 'w', encoding='utf-8', newline='\n') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    return new_file_path

def main():
    parser = argparse.ArgumentParser(description="Process a JSON file.")
    parser.add_argument("file_path", help="Path to the JSON file")
    args = parser.parse_args()

    new_file_path = remove_bytes_from_json(args.file_path)
    print(f"Modified file saved as {new_file_path}")

if __name__ == "__main__":
    main()

# # 使用例
# file_path = r"edge-net-export-log.json"
# new_file_path = remove_bytes_from_json(file_path)
# print(f"Modified file saved as {new_file_path}")
