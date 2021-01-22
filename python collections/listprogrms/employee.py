employees=[
    [10,"christy","dataanalyst",50000],
    [11,"jhon","ba",30000],
    [12,"sabu","dataanalyst",40000],
    [13,"tom","developer",40000],
    [14,"jhony","developer",30000],
    [15,"sabir","dataanalyst",50000],
    [16,"tino","developer",40000],
    [17,"tomis","developer",47000],
    [18,"jhonis","developer",32000],

]
#no of employee
no_of_employees=len(employees)
print("mo of employee=",no_of_employees)

#print how much salery tot
tot_amount=0
for emp in employees:
    tot_amount+=emp[3]
print("tot amount=",tot_amount)

#grp by designation
d_cnt,da_count,ba_count=0,0,0
for emp in employees:
    if emp[2]=="dataanalyst":
        da_count+=1
    elif emp[2]=="ba":
        ba_count+=1
    else:
        d_cnt+=1

print("dataan",da_count,"ba_count",ba_count,"developer count",d_cnt)


#highest salery employee

salary_list=[]
for emp in employees:
    salary_list.append(emp[3])
hig_salary=max(salary_list)
print(hig_salary)

for emp in employees:
    if emp[3]==hig_salary:
        print(emp)



#print employee name who receives lowest salery whose desg=devlpr

salary_list=[]
for emp in employees:
    salary_list.append(emp[3])

low_sal=min(salary_list)
for emp in employees:
    if(emp[2]=="developer") & (emp[3]==low_sal):
        print(emp)

