import os
import random
import time
import smtplib
from email.mime.text import MIMEText

# Hostfile location
hostfile_location = ""
hostfile_name = "hosts"

# Email setup for unique passcode
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.connect('smtp.gmail.com', 465)
s.starttls
s.login('websiteblockerext@gmail.com', 'websiteblockerext')


# Start Website Blocker process
def website_blocker():

    print("\nWelcome to your website blocker utility!\n")
    downtime_length = downtime()
    print(f"\nYour unique unlock code will be emailed to "
          f"\"websiteblockerext@gmail.com\" in {downtime_length} hours.")
    append_hostfile()
    start_timer(downtime_length)


# Request and enter how many hours websites are to be blocked
def downtime():
    return validateDowntimeHours(input("Please enter how many hours "
                                       "(between 1 and 8) you want to block "
                                       "websites for: "))


# Validate downtime hour value that has been requested
def validateDowntimeHours(hours):
    try:
        if int(hours) not in range(1, 9):
            print("\nYour entry is not valid.")
            return downtime()
        else:
            return int(hours)
    except ValueError:
        print("\nYour entry is not valid.")
        return downtime()


# Add websites to be blocked to hostfile and specify unreachable IP
def append_hostfile():
    update_hostfile = open(f"{hostfile_location}test_hostfile.txt", 'a')
    update_hostfile.write("\n \t127.0.0.1\t\twww.facebook.com")


# Start timer based on downtime time entered
def start_timer(downtime):
    timer = 0
    timer = downtime * 10  # Currently set to seconds for speed of testing
    time.sleep(timer)
    generateUnlockKey()


# Create unique passcode and pass to send email function
def generateUnlockKey():
    randomID = ""
    randomID = generate_random_id()
    generateEmail(randomID)
    unlock(randomID)


# Generate random ID
def generate_random_id():
    id = ""
    for n in range(5):
        id = id + str(random.randint(0, 9))
    return id


# Create email and send unique passcode to user
def generateEmail(randomID):
    msg = MIMEText(randomID)
    msg['Subject'] = "Unique Unblocking Code"
    msg['From'] = "websiteblockerext@gmail.com"
    msg['To'] = "websiteblockerext@gmail.com"
    s.sendmail('websiteblockerext@gmail.com', 'websiteblockerext@gmail.com',
               msg.as_string())


# User enters unique passcode that has been sent to email address
def unlock(rID):
    validateRandomID(input("\nPlease enter the unlock code made up of 5 "
                           "digits you should have received by email: "), rID)
    revert_hostfile()


# Validate unique passcode that has been entered
def validateRandomID(randID, rID):
    try:
        if (int(randID) in range(00000, 100000) and
           len(randID) == 5 and randID == rID):
            return randID
        else:
            print("\nYour unlock code is not valid.")
            return unlock(rID)
    except ValueError:
        print("\nYour unlock code is not valid.")
        return unlock(rID)


# Revert hostfile to original
def revert_hostfile():
    with open(f"{hostfile_location}test_hostfile.txt", 'r') as hostfile:
        revert_hostfile = hostfile.readlines()
    with open(f"{hostfile_location}test_hostfile.txt", 'w') as hostfile:
        for n in revert_hostfile:
            if "www.facebook.com" not in n:
                hostfile.write(n)
    with open(f"{hostfile_location}test_hostfile.txt", 'r+') as f:
        lines = f.readlines()
        lines[-1] = lines[-1].strip()
        f.seek(0)
        f.writelines(lines)
        f.truncate()


if __name__ == '__main__':
    website_blocker()
    # generate_random_id()
    # revert_hostfile()
    # generateEmail('1111')
    # generateEmail(generate_random_id())
    # validateRandomID("0")
    # downtime()
