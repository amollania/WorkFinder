from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

driver.implicitly_wait(3)
driver.get('https://jp.indeed.com/')

# Keyword input
driver.find_element_by_id('text-input-what').send_keys('python')

# Location input
driver.find_element_by_id('text-input-where').send_keys('茨城県 つくば市')

# Button Action
# driver.find_element_by_class_name('icl-Button').click()
driver.find_element_by_id('text-input-where').send_keys(Keys.ENTER)
driver.implicitly_wait(2)
# driver.find_element_by_xpath('//*[@id="whatWhere"]/div/div/form/div[3]/button').click()


# PopUp Window Exit Click
try:
    driver.find_elements_by_id('popover-foreground')
    driver.find_element_by_class_name('icl-Icon icl-Icon--sm  icl-Icon--black close').click()
except:
    pass


# Page Catch
driver.implicitly_wait(2)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
soup = soup.find(id ='resultsCol')

print('List Catch Complate')

f = open('japan_list.txt', 'w', encoding='UTF8')
f.write(str(soup))

f.close()
