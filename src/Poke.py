#! /usr/bin/python
from sys import exit, stdout
import traceback
import mechanize
import time
import os
import random
from bs4 import BeautifulSoup as soup

total_pokes = 0
browser = mechanize.Browser()
browser.addheaders = [('User-agent', 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')]
browser.set_handle_robots(False)

Facebook_Username = "YOUR_USERNAME"
Facebook_Password = "YOUR_PASSWORD"

def new_random_delay_in_minutes():
        min_delay_in_minutes = 5
        max_delay_in_minutes = 30
        
        return random.randint(min_delay_in_minutes, max_delay_in_minutes)

def wait():
        delay_in_seconds = new_random_delay_in_minutes() * 60
        
        print ("Checking Again In " + str(int(delay_in_seconds / 60)) + " Minutes")
        
        while (delay_in_seconds >= 0):
                delay_in_seconds -= 1
                time.sleep(1)

def begin_checking_for_pokes():
        global total_pokes
        poke_found = False
        
        while True:
                try:
                        #Load the poke page
                        browser.open("http://m.facebook.com/pokes")
                        browser._factory.is_html = True

                        #Find all links for "Poke Back"
                        for l in browser.links(text_regex = "Poke Back"):
                                s = soup(browser.response(), 'html.parser')
                                browser.follow_link(text_regex="Poke Back",nr=0)
                                total_pokes += 1
                                poke_found = True
                                print ("Poked Back! Total Pokes: " + str(total_pokes))
                                break
                        
                except:
                        #Print error and stop
                        print ("There was some sort of error....")
                        print (traceback.format_exc())
                        exit()

                if (poke_found):
                        begin_checking_for_pokes()
                  
                #Delay
                wait()

def login_to_facebook():
        try:
                #Login
                browser.open("http://m.facebook.com/login")
                browser._factory.is_html = True
                browser.select_form(nr=0)
                browser.form['email'] = Facebook_Username
                browser.form['pass'] = Facebook_Password
                browser.submit()
        
                #Start Checking for Pokes
                begin_checking_for_pokes()
        except:
                #Print error and stop
                print ("There was some sort of error....")
                print (traceback.format_exc())
                exit()

#Start
login_to_facebook();
