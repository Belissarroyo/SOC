# SOC Lab: Automating Security Workflows with Python Dictionaries

siem_logs = {
    'user_001': {'username': 'belissa', 'status': 'active', 'failed_attempts': 1},
    'user_002': {'username': 'juani', 'status': 'locked', 'failed_attempts': 15},
    'user_003': {'username': 'skyler', 'status': 'active', 'failed_attempts': 0},
    'user_004': {
        'username': 'elvis',
        'status': 'active'  # 'failed_attempts' key missing
    }
}

# Task 1: Account Locker - flag brute-force targets (> 5 failed attempts)
for user_id, data in siem_logs.items():
    failed_attempts = data.get('failed_attempts', 0)  # safe: no KeyError for user_004
    if failed_attempts > 5:
        data['status'] = 'locked'
        username = data['username']
        print(f"[CRITICAL] Account locked for user: {username}")

# Task 2: Malformed Entry handling - check for missing keys

required_fields = ['username', 'status', 'failed_attempts']
for user_id, data in siem_logs.items():
    missing_field =[]
    for field in required_fields:
        if field not in data:
            missing_field.append(field)
    if missing_field:
        print(f"[WARNING] Malformed entry for user_id: {user_id}"
        print(f"[missing fields as missing field]")
        if "failed_attempts" in missing_field:
            print(f"[WARNING] Missing 'failed_attempts' for user_id: {user_id}")

        else:
            print(f"[Ok] valid entry for user_id: {user_id}")
