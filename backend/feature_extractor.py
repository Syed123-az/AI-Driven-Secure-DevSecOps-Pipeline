import re

SQL_KEYWORDS = ["select", "drop", "insert", "delete", "update", "or", "and"]

def extract_features(payload):
    payload_lower = payload.lower()

    payload_length = len(payload)
    special_char_count = len(re.findall(r'[^a-zA-Z0-9\s]', payload))

    sql_flag = 1 if any(k in payload_lower for k in SQL_KEYWORDS) else 0
    failed_login_flag = 1 if "failed" in payload_lower else 0

    return [[payload_length, special_char_count, sql_flag, failed_login_flag]]