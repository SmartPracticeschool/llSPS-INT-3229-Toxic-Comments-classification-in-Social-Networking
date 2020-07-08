from selenium import webdriver
import time
driver = webdriver.Chrome('chromedriver')
def start():
    driver.get(r"file:///C:\Users\DELL\Desktop\AI\toxic\toxic.html")
	
def inputtxt():
    while 1 :
        try:
            el = driver.find_element_by_id("p1").text
            while el=='.':
                el = driver.find_element_by_id("p1").text
            elem = driver.find_element_by_id("p1")
            driver.execute_script("arguments[0].textContent = arguments[1];",elem, ".")
            inputs = driver.find_element_by_id("tb")
            txt=inputs.get_attribute('value')
            break;
        except:
            time.sleep(0.1)
            continue
    return txt

def outputtxt(x,txt):
	if x=='1':
		elem = driver.find_element_by_id("tox")
		driver.execute_script("arguments[0].textContent = arguments[1];",elem,txt+'%')
		width="arguments[0].setAttribute('style','width:"+txt+"%; color:#00FFFF')"
		driver.execute_script(width, elem)
	elif x=='2':
		elem = driver.find_element_by_id("st")
		driver.execute_script("arguments[0].textContent = arguments[1];",elem,txt+'%')
		width="arguments[0].setAttribute('style','width:"+txt+"%; color:#00FFFF')"
		driver.execute_script(width, elem)
	elif x=='3':
		elem = driver.find_element_by_id("ob")
		driver.execute_script("arguments[0].textContent = arguments[1];",elem,txt+'%')
		width="arguments[0].setAttribute('style','width:"+txt+"%; color:#00FFFF')"
		driver.execute_script(width, elem)
	elif x=='4':
		elem = driver.find_element_by_id("thd")
		driver.execute_script("arguments[0].textContent = arguments[1];",elem,txt+'%')
		width="arguments[0].setAttribute('style','width:"+txt+"%; color:#00FFFF')"
		driver.execute_script(width, elem)
	elif x=='5':
		elem = driver.find_element_by_id("in")
		driver.execute_script("arguments[0].textContent = arguments[1];",elem,txt+'%')
		width="arguments[0].setAttribute('style','width:"+txt+"%; color:#00FFFF')"
		driver.execute_script(width, elem)
	else:
		if x=='6':
			elem = driver.find_element_by_id("hate")
			driver.execute_script("arguments[0].textContent = arguments[1];",elem,txt+'%')
			width="arguments[0].setAttribute('style','width:"+txt+"%; color:#00FFFF')"
			driver.execute_script(width, elem)
	
