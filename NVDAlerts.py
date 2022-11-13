import nvdlib
# import subprocess
import pymsgbox
import datetime
import time
import sys



# Gets the new CVEs every hour and sends a msg box alert GUI. 
def nvdnewcve():
    end = datetime.datetime.now() # Gets the current time
    start = end - datetime.timedelta(days=1) # Sets start to past 24 hours
    
    # queries the NVD for reports of new CVEs in the last 24hrs / uses the API key so you can only request once every 0.6 seconds
    r = nvdlib.searchCVE(pubStartDate=start, pubEndDate=end, key='564b9d30-b4a3-4769-9e5e-0648382d1b56') 
    for newCVE in r:
        noti= pymsgbox.alert(text=f"New CVE found: {newCVE.id, str(newCVE.score[0])}")
        time.sleep(3600)  # Sends an alert every hour for CVEs of the day
        return noti  # Returns the function / sends the alert
    sys.exit()


# this is where you can integrate the CTk window with subprocess which is
# cross-plat on Linux, Mac, and Windows instead of Win10Toast that is strictly Windows
#def popalrt(popalert):
    #subprocess.Popen()    # CTk window
    #return   # Returns the Popen module and pops it open when the button is clicked

nvdnewcve()