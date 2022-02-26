#  Database config here. All values here are used in every query, so change it at your own risk
dbconfig = {'host'    : '127.0.0.1',
            'user'    : 'root',
            'password': 'root',
            'database': 'night_count'}
table = "nightcount"
log_name = "general.log"
log_messages = {"connect" : f"Success:{' ' * (12 - len('success'))} Connected to database \
{str(dbconfig['database'])} as {dbconfig['user']} on host {dbconfig['host']}",
                "con_fall": f"Exception:{' ' * (12 - len('exception'))} Database connection "
                            f"broke down",
                "close"   : f"Info:{' ' * (12 - len('Info'))} Code exited",
                "start"   : f"Success:{' ' * (12 - len('success'))} Code launched"
                }
#  print(log_messages['connect'])
#  print(f"insert into {dbconfig['table']} values (aboba)")
