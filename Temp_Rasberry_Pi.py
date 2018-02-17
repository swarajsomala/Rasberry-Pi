from gpiozero import CPUTemperature
from time import sleep,strftime,time

cpu = CPUTemperature()
file_Name = strftime("%d_%m_%y_%H_%M")

with open("/home/pi/" + file_Name + ".csv","w") as log:
    try:
        while True:
            temp = cpu.temperature
            log.write("{0}:{1}\n".format(strftime("%y-%m-%d %H:%M:%S"),str(temp)))
          #  print(cpu.temperature)
    except :
            log.close()
            print("\n Stopped Reading the values \n")
