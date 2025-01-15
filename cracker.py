import random
import numpy as np
import time

signs = "1234567890qwertyuiopasdfghjklzxcvbnmöäå"

signs_lis = [i for i in signs]


password = input("What password do you want?")
start_time = time.time()

while True:
    check_psw = np.random.choice(size=len(password), a=signs_lis, p=None, replace=True)
    concatenated_pswd = ''.join(check_psw)


    if concatenated_pswd == password:
        end_time = time.time()
        dif_time = round(end_time - start_time)

        if dif_time < 50:
            print("--------------------------------------------------------------------------------------")
            print("I just broke that shit with eeeaseeee")
            print("")
            time.sleep(2)
            print("You want to know the password huh?!")
            print("")
            time.sleep(1)
            print(concatenated_pswd)
            print("Time it took to crack:", dif_time, "sec")
            print("--------------------------------------------------------------------------------------")
        elif dif_time >= 50 and dif_time < 120:
            print("--------------------------------------------------------------------------------------")
            print("Took me longer then expected...")
            print("")
            time.sleep(2)
            print("But it does not mean you have a strong password!")
            time.sleep(2)
            print("Rather the opposite, CHANGE IT NOW!!")
            time.sleep(1)
            print("Yea, here it is:")
            print("")
            print(concatenated_pswd)
            print("Time it took to crack:", dif_time, "sec")
            print("--------------------------------------------------------------------------------------")
        else:
            print("--------------------------------------------------------------------------------------")
            print("Damn you even had the patience to wait for me to crack it, it took me:")
            print(dif_time, 'sec')
            time.sleep(2)
            print("And to the big reveal you have waited for...")
            time.sleep(0.5)
            print("Here it is:")
            time.sleep(0.5)
            print(concatenated_pswd)
        break