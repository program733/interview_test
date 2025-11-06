import datetime;


user_input=input("Enter the time of the day (YYYY-MM-DD HH:MM): ")
times = datetime.datetime.strptime(user_input, "%Y-%m-%d %H:%M")
current_time=times.hour
print(times)
print(current_time)
if ((current_time>= 4)and (current_time < 12)):
    print("Its morning now")
elif ((current_time>= 12)and (current_time < 16)):
    print("Its Afternoon now")
elif ((current_time >= 16) and (current_time < 24)):
    print("Its Evening now")
else :
    print("Its a midnight time")

