import base64
import os
import time
import sys
from subprocess import call
from validate_email import validate_email as ve
import GmailEmailLibrary
sender = GmailEmailLibrary.gmailsendemail.SendEmailUtility()

class DailyTest:
    ''' Class for running Automated tests using Appium and Robot
    Receives 2 parameters:
    os_name = The os for the test (android, ios)
    email = Email address for receiving email
     '''
    
    def __init__(self, os_name, email_address):
        self.os_name = os_name
        self.email_address = email_address
    
    def start_appium(self):
        print "****Starting Appium Server... ****\n"
        try:
            os.system('appium&')
        except:
            print "Unexpected error:", sys.exc_info()
        else:
            time.sleep(10)
            
    def start_avd(self):
        if self.os_name == "android":
            print "****Starting Android emulator... ****\n"
            try:
                os.system('/Users/HaydeML/Library/Android/sdk/tools/emulator -avd Nexus_5X_API_23 &')
            except:
                print "Unexpected error:", sys.exc_info()
            else:
                time.sleep(30)
        else:
            print "****Starting iOS emulator... ****\n"
    
    def run_tests(self):
        print "****Running tests... ****\n"
        #time.sleep(10)
        if self.os_name == "android":          
            try:
                os.chdir("/Users/HaydeML/Documents/Rever/AppiumScripts")
                call(["robot","TestReverAndroid.robot"])
            except:
                print "Unexpected error:", sys.exc_info()
            else:
                print "****Waiting****"
                time.sleep(10)
        elif self.os_name == "ios":            
            try:
                os.chdir("/Users/HaydeML/Documents/Rever/AppiumScripts")
                call(["robot","TestRever.Robot"])
            except:
                print "Unexpected error:", sys.exc_info()
            else:
                print "****Waiting****"
                time.sleep(10)
            
    def send_mail(self):
        print "Sending email to "+ self.email_address+"...\n"
        email_subject = 'Results ' + self.os_name + ' ' + time.strftime("%d:%m:%Y")
        email_body = 'Hi There, \n Please find attached the report for ' + self.os_name + ' tests performed on ' + time.strftime("%d:%m:%Y")
        email_attachment = '/Users/HaydeML/Documents/Rever/AppiumScripts/report.html'
        
        try:
            sender.send_mail_with_attachment("correo","pwd", self.email_address, email_subject, email_body, email_attachment)
        except:
            print "Unexpected error:", sys.exc_info()            
        
            
if __name__ == '__main__':
    
    values = sys.argv # Get parameter from command line
    if ve(values[2]) and values[1] == "android" or values[1] == "ios":
        try:
            test=DailyTest(values[1],values[2]) # Use parameter for creating object
    
            test.start_appium() # Starting appium server
            test.start_avd() # If android, run emulator if iOS do nothing
            test.run_tests() # Run tests from robot framework
            test.send_mail() # Send email with report
        except:
            print "Unexpected error:", sys.exc_info()
    else:
        print "****Either the OS or the email is wrong, please check...****\n"
    
    
    
    
            
            
    
            
    

