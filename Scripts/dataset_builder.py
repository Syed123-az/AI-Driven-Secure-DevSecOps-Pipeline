import csv
import re

def extract_features(text):
    payload_length = len(text)
    special_char_count = len(re.findall(r'[^a-zA-Z0-9\s]', text))

    sql_keywords = ['select', 'drop', 'insert', 'delete', 'update', 'or', 'and']
    sql_flag = int(any(k in text.lower() for k in sql_keywords))

    failed_login_flag = int("failed" in text.lower() or "invalid" in text.lower())

    return payload_length, special_char_count, sql_flag, failed_login_flag


rows = []

# NORMAL LOGS
with open('../dataset/normal_logs.txt') as f:
    for line in f:
        text = line.strip()
        if text:
            features = extract_features(text)
            rows.append([text, *features, 0])

# MALICIOUS LOGS
with open('../dataset/melicious_logs.txt') as f:
    for line in f:
        text = line.strip()
        if text:
            features = extract_features(text)
            rows.append([text, *features, 1])

# SAVE CSV
with open('../dataset/dataset.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([
        "payload",
        "payload_length",
        "special_char_count",
        "sql_flag",
        "failed_login_flag",
        "label"
    ])
    writer.writerows(rows)

print("Dataset created successfully!")