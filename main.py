from selenium import webdriver
import random

while True:

	driver = webdriver.Firefox()
	driver.get('http://www.porngifs.xyz/')

	#handle=driver.window_handles
	#print(handle)
	driver.switch_to.window(driver.window_handles[1])
	driver.close()

	driver.switch_to.window(driver.window_handles[0])

	elements = driver.find_elements_by_tag_name('iframe')

	click = random.choice(elements)
	if "jads" in click.get_attribute("src"): 
		click.click()
		driver.close()

	driver.switch_to.window(driver.window_handles[0])
	driver.close()