# SOC Lab: Automating Security Workflows with Python Dictionaries
#Attempt to pull
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

# Task 2: Data enrichment - add 2FA flag to every account
for data in siem_logs.values():
    data['2FA_enabled'] = True

# Task 3: Final audit for Senior SOC Engineers
for user_id, details in siem_logs.items():
    username = details['username']
    status = details['status']
    mfa = details['2FA_enabled']
    print(f"Audit Complete - ID: {user_id} | "
          f"Username: {username} | "
          f"Status: {status} | 2FA: {mfa}")
