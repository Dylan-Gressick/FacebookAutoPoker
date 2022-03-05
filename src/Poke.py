#! /usr/bin/python
from sys import exit, stdout
import traceback
import mechanize
import time
import os
from bs4 import BeautifulSoup as soup

#Set Globals
delay = 900
browser = mechanize.Browser()
browser.addheaders = [('User-agent', 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')]
browser.set_handle_robots(False)

Facebook_Username = "YOUR_EMAIL"
Facebook_Password = "YOUR_PASSWORD"

def wait_for_time(delay):
        while (delay >= 0):
                delay -= 1
                time.sleep(1)

def begin_checking_for_pokes():
        total_pokes = 0
        while True:
                try:
                        #Load the poke page
                        browser.open("http://m.facebook.com/pokes")
                        browser._factory.is_html = True

                        print ("Checking For Pokes")

                        #Find all links for "Poke Back"
                        for l in browser.links(text_regex = "Poke Back"):
                                print ("We Found A Poke!")
                                s = soup(browser.response(), 'html.parser')
                                browser.follow_link(text_regex="Poke Back",nr=0)
                                total_pokes += 1
                                print ("Poked Back! Total Pokes: " + str(total_pokes))

                except:
                        #Print error and stop
                        print ("There was some sort of error....")
                        print (traceback.format_exc())
                        exit()

                print ("Checking Again In 5 Mins")
                
                #Delay
                wait_for_time(delay)

def login_to_facebook():
        #Login
        browser.open("http://m.facebook.com/login")
        browser._factory.is_html = True
        browser.select_form(nr=0)
        browser.form['email'] = Facebook_Username
        browser.form['pass'] = Facebook_Password
        browser.submit()
        
        #Start Checking for Pokes
        begin_checking_for_pokes()

#Start
login_to_facebook();
