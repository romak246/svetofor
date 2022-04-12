import time

red_time = 10
red_yellow_time = 3
green_time = 10
green_yellow_time = 3

def svetofor(red_time, red_yellow_time,green_time, green_yellow_time):
    a = 'Горит красный'
    b = 'Горит красный и желтый'
    c = 'Горит зеленый'
    d = 'Горит зеленый и желтый'
    for i in range(red_time+red_yellow_time+green_time+green_yellow_time):
        if i<red_time:
         print(a, i)

        elif i>=red_time and i<red_time+red_yellow_time:
          print(b, i)

        elif i>=red_time+red_yellow_time and i<red_time+red_yellow_time+green_time:
         print(c, i)

        elif i>=red_time+red_yellow_time:
         print(d, i)
        time.sleep(1)
    svetofor(red_time, red_yellow_time,green_time, green_yellow_time)

svetofor(red_time, red_yellow_time,green_time, green_yellow_time)




