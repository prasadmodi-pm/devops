import pandas as pd
data = pd.read_excel("hardware.xlsx")
department = data['Group'].unique()

print("----------------------------------------------------------------------------")
print("list of Department where hardware hosted")
print("----------------------------------------------------------------------------")

print(department)

print("----------------------------------------------------------------------------")
print("list of all the applications for each department")
print("----------------------------------------------------------------------------")

application_list = data.groupby(['Group','Application']).size()
print(application_list)

print("----------------------------------------------------------------------------")
print("calculate the number of CPUs and memory used by each department.")
print("----------------------------------------------------------------------------")

dept_cpu_mem = data.groupby(['Group', 'CPU cores', 'RAM (MB)']).size()
print(dept_cpu_mem)

print("----------------------------------------------------------------------------")
print("calculate the number of CPUs and memory used by each application.")
print("----------------------------------------------------------------------------")

app_cpu_mem = data.groupby(['Application', 'CPU cores', 'RAM (MB)']).size()
print(app_cpu_mem)

print("----------------------------------------------------------------------------")
print("calculate the number of CPUs and memory used in each of the data centers.")
print("----------------------------------------------------------------------------")

data_centers_cpu_mem = data.groupby(['Site', 'CPU cores', 'RAM (MB)']).size()
print(data_centers_cpu_mem)