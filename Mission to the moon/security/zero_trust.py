
def authenticate(token):
    if token == "MISSION_CLEARANCE_LEVEL_1":
        return "Access Granted"
    return "Access Denied"
