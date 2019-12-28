from common.util.mysql_connect import MysqlConnect

SQL_QUERY_ACCOUNT_FROM_SYS_USER = 'select account,gender from sys_user;'

db_sql = MysqlConnect()
sys_user_accounts_and_genders = db_sql.query(SQL_QUERY_ACCOUNT_FROM_SYS_USER)
sys_user_accounts = []
sys_user_genders = []
for i in range(len(sys_user_accounts_and_genders)):
    sys_user_accounts.append(sys_user_accounts_and_genders[i][0])
    sys_user_genders.append(sys_user_accounts_and_genders[i][1])
print(sys_user_accounts)
print(sys_user_genders)



