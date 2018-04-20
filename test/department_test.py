from dingding_api.department import DingDepartment

depart = DingDepartment()
users_detail = depart.get_department_users_detail(1)
for u in users_detail:
    print(u)