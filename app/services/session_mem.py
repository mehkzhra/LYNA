from collections import defaultdict

# In-memory sessions {session_id: {"case_id":..., "revealed":[], "chat":[]}}
SESSIONS = defaultdict(dict)
