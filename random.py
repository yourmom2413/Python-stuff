import time

def good_day():
    print ("That sounds like you had a great day! ")
    shutdown()

def bad_day():
    print ("That sounds like you had a bad day. :( ")
    time.sleep(3)
    print ("That is terrible hope your day gets better!")
    shutdown()

def fine_day():
    print ("That sounds like a very mild day. Hope it gets more exiting!")
    shutdown()

def okay_day():
    print ("Your such a boring person try again!!!")
    shutdown()

def shutdown():
    print("closing in: 5 seconds")
    time.sleep(1)
    print("4 seconds")
    time.sleep(1)
    print("3 seconds")
    time.sleep(1)
    print("2 seconds")
    time.sleep(1)
    print("1 seconds")
    time.sleep(1)
    print("closing")
    time.sleep(1)
    quit()


Name = input("What is your name: ")

Answer = input ("hello, " + Name +  " how was your day? Good, Bad, Fine, Okay or Ok: ").lower()
if Answer == "good":
    input ("Why was it good? ")
    good_day()
elif Answer == "bad":
    input ("Why was it bad? ")
    bad_day()
elif Answer == "fine":
    input ("Why was it fine? ")
    fine_day()

elif Answer == "okay" or Answer == "ok":
    input ("Why was your day okay? ")
    okay_day()



