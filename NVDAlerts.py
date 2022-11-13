import nvdlib
import sys
import pymsgbox
import datetime




# Gets the new CVEs every hour and sends a msg box alert GUI. 
# Documentation for nvdlib https://nvdlib.com/en/latest/v2/CVEv2.html#searching-cves
def nvdnewcve():
    end = datetime.datetime.now() # Gets the current time
    start = end - datetime.timedelta(days=14) # Sets start to past 24 hours
    
    # queries the NVD for reports of new CVEs in the last 24hrs / uses the API key so you can only request once every 0.6 seconds
    r = nvdlib.searchCVE(pubStartDate=start, pubEndDate=end, key='564b9d30-b4a3-4769-9e5e-0648382d1b56') 
    for newCVE in r:
        noti= pymsgbox.alert(text=f"New CVE found: {newCVE.id, str(newCVE.score), str(newCVE.url)}")
        return noti 
    sys.exit()
# this is where you can integrate the CTk window with subprocess which is
# cross-plat on Linux, Mac, and Windows instead of Win10Toast that is strictly Windows
#def popalrt(popalert):
    #subprocess.Popen()    # CTk window
    #return   # Returns the Popen module and pops it open when the button is clicked
    
nvdnewcve()
