#  Database config here. All values here are used in every query, so change it at your own risk
c = {'host': '127.0.0.1', 'user': 'root', 'password': 'root', 'database': 'night_count'}
table = "nightcount"
log_name = "general.log"
messages = {
    "con"     : f"Success: Connected to database",
    "fall"    : f"Exception: connection fell down",
    "close"   : f"Info:      exited",
    "start"   : f"Success:   launched"}
#  print(log_messages['connect'])
#  print(f"insert into {dbconfig['table']} values (aboba)")
