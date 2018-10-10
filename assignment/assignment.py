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

print("----------------------------------------------------------------------------")
print("###############  Assignment 2 ##############################################")
print("----------------------------------------------------------------------------")


container = data['Container size'].unique()
print(container)

print("----------------------------------------------------------------------------")
print("Count by Container Size")
print("----------------------------------------------------------------------------")

container_count = data.groupby(['Group', 'Container size']).size()
print(container_count)

a = list(container_count)

count = 365 * 24 * 7

print("---------------------------------------------------------------------------------------------------------------")
print("current cost by container size and Ec2 instance price for RHEL")
print("2XL per hour $ 0.4628 , ", "L per hour $ 0.1432 , ", "M per hour $ 0.1016 , ", "S per hour $ 0.0808 , ",\
      "XL per hour $ 0.2264")
print("---------------------------------------------------------------------------------------------------------------")

print("Cost 2XL = ", a[0] * count * 0.4628, " Cost L = ", a[1] * count * 0.1432, " Cost M = ", a[2] * count * 0.1016,\
      "Cost S = ", a[3] * count * 0.0808, "Cost XL = ", a[4] * count * 0.2264)

print("---------------------------------------------------------------------------------------------------------------")
print("Forecast cost after 1, 2 and 3 years by Department and Ec2 instance price for RHEL")
print("2XL per hour $ 0.4628 , ", "L per hour $ 0.1432 , ", "M per hour $ 0.1016 , ", "S per hour $ 0.0808 , ",\
      "XL per hour $ 0.2264")
print("---------------------------------------------------------------------------------------------------------------")

print("Engineering Cost after 1 years with 10 % increase = ", (a[0] * count * 0.4628 + a[1] * count * 0.1432 \
    + a[2] * count * 0.1016 + a[3] * count * 0.0808 + a[4] * count * 0.2264 * (1 + 10)))

print("Engineering Cost after 2 years with 25 % increase = ", (a[0] * count * 0.4628 + a[1] * count * 0.1432 \
    + a[2] * count * 0.1016 + a[3] * count * 0.0808 + a[4] * count * 0.2264 * (1 + 25)))

print("Engineering Cost after 3 years with 40 % increase = ", (a[0] * count * 0.4628 + a[1] * count * 0.1432 \
    + a[2] * count * 0.1016 + a[3] * count * 0.0808 + a[4] * count * 0.2264 * (1 + 40)))

print("--------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------")

print("Engineering Canada Cost after 1 years with 10 % increase = ", (a[5] * count * 0.1432 + a[6] * count * 0.1016 \
    + a[7] * count * 0.0808 * (1 + 10)))

print("Engineering Canada Cost after 2 years with 25 % increase = ", (a[5] * count * 0.1432 + a[6] * count * 0.1016 \
    + a[7] * count * 0.0808 * (1 + 25)))

print("Engineering Canada Cost after 3 years with 40 % increase = ", (a[8] * count * 0.1016 + a[6] * count * 0.1016 \
    + a[7] * count * 0.0808 * (1 + 40)))

print("----------------------------------------------------------------------------")
print("----------------------------------------------------------------------------")

print("Marketing Cost after 1 years with 10 % increase = ", ((a[8] * count * 0.1432 + a[9] * count * 0.0808) \
    * (1 + 10)))

print("Marketing Cost after 2 years with 25 % increase = ", ((a[8] * count * 0.1432 + a[9] * count * 0.0808) \
    * (1 + 25)))

print("Marketing Cost after 3 years with 40 % increase = ", ((a[8] * count * 0.1432 + a[9] * count * 0.0808) \
    * (1 + 40)))

print("----------------------------------------------------------------------------")
print("----------------------------------------------------------------------------")


print("Sales Cost after 1 years with 80 % decrease = ", (((a[10] * count * 0.1432 + a[11] * count * 0.1016) \
    + a[12] * count * 0.0808 + a[13] * count * 0.2264) / 100) * 20)

print("Sales Cost after 2 years with 100 % decrease = ", (((a[10] * count * 0.1432 + a[11] * count * 0.1016) \
    + a[12] * count * 0.0808 + a[13] * count * 0.2264) / 100) * 0)

