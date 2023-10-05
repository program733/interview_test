#A company offers employees the facility to book their office space one day in advance. Employee registers their expected entry and exit times on the portal, before coming to the office. Given the data for the next day, find out how many minimum chairs will be required to serve all the employees for that particular day. The chairs can be reused across employees during the day. E.g. Employees log in and logout: 9:00 - 12:30 10:00 - 12:00 14:00 - 18:00 20:00 - 21:00

#Ex:-

time_stamps = [{900, 1230}, {1000, 1200}, {1400, 1800}, {1410, 1700}, {1405, 1800},{2000, 2100}]
# Chairs required: 2 (1st and 2nd users are present simultaneously to require a chair)

chair_count = 1

for i in range(1,len(time_stamps)):
    print(time_stamps[i])
    val = list(time_stamps[i])
    if val[0] < list(time_stamps[i-1])[1]:
        chair_count+=1

print(chair_count)

