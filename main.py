# BWOTSHEWCHB

# Import

import time

from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# Input

username = input()
password = input()

# Functions

def validate_xpath(xpath) :
	try :
		driver.find_element_by_xpath(xpath)
	except NoSuchElementException :
		return False
	return True

# Code

driver = webdriver.Firefox() 

driver.get("https://courses.aut.ac.ir/login/index.php")
driver.find_element_by_name("username").send_keys(username)
driver.find_element_by_name("password").send_keys(password)
driver.find_element(By.ID , "loginbtn").click()
time.sleep(3)

driver.get("https://lms.aut.ac.ir")
time.sleep(20)

classmates = set()

for page in range(0 , 2) :
	it = 1
	courses_next_button = "/html/body/app-root/div/app-users-panel/div/div[1]/p-card/div/div/div/app-users-panel-courses-list/div/p-footer/p-paginator/div/button[3]"
	while ( True ) :
		xpath_course_name = "/html/body/app-root/div/app-users-panel/div/div[1]/p-card/div/div/div/app-users-panel-courses-list/div/p-accordion/div/p-accordiontab[" + str(it) + "]/div/div[1]/a/p-header"
		xpath_course_expander = "/html/body/app-root/div/app-users-panel/div/div[1]/p-card/div/div/div/app-users-panel-courses-list/div/p-accordion/div/p-accordiontab[" + str(it) + "]/div/div[1]/a/span"
		xpath_course_users = "/html/body/app-root/div/app-users-panel/div/div[1]/p-card/div/div/div/app-users-panel-courses-list/div/p-accordion/div/p-accordiontab[" + str(it) + "]/div/div[2]/div/div[3]/button"
		if ( validate_xpath(xpath_course_expander) == False ) :
			break
		course = driver.find_element_by_xpath(xpath_course_name).text
		driver.find_element_by_xpath(xpath_course_expander).click()
		time.sleep(3)
		driver.find_element_by_xpath(xpath_course_users).click()
		time.sleep(3)
		while ( True ) :
			users_next_button = "/html/body/app-root/div/app-users-panel/div/div[2]/p-card/div/div/div/app-users-panel-course-users/div/p-footer/p-paginator/div/button[3]"
			for i in range(1 , 11) :
				xpath_name = "/html/body/app-root/div/app-users-panel/div/div[2]/p-card/div/div/div/app-users-panel-course-users/div/p-table/div/div/table/tbody/tr[" + str(i) + "]/td[1]/div"
				xpath_surename = "/html/body/app-root/div/app-users-panel/div/div[2]/p-card/div/div/div/app-users-panel-course-users/div/p-table/div/div/table/tbody/tr[" + str(i) + "]/td[2]/div"
				if ( validate_xpath(xpath_name) and validate_xpath(xpath_surename) ) :
					name = driver.find_element_by_xpath(xpath_name).text
					surename = driver.find_element_by_xpath(xpath_surename).text
					classmates.add((name.lstrip(' ') , surename.lstrip(' ') , course.lstrip(' ')))
			if ( driver.find_element_by_xpath(users_next_button).is_enabled() == False ) :
				break
			driver.find_element_by_xpath(users_next_button).click()
			time.sleep(4)
		it += 1
	if ( page == 1 ) :
		break
	driver.find_element_by_xpath(courses_next_button).click()
	time.sleep(2)

driver.quit()

input_file = open("target.txt" , "r" , encoding="utf-8")
output_file = open("classmates.txt" , "w" , encoding="utf-8")

line = input_file.readline()
line = line.split('/')

for classmate in classmates :
	name , surename , course = classmate
	for target in line :
		if ( target == name + " " + surename ) :
			output_file.write(name + " " + surename + " : " + course + "\n")

input_file.close()
output_file.close()

