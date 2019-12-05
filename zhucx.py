from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import string
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
import time
import os


options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
options.add_argument("'lang=zh_CN.UTF-8'")
#chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(options =options)
driver.get('https://business.facebook.com/')
#点击创建
driver.find_element_by_id('u_0_1m').click()
#定位输入框
driver.find_element_by_xpath('//*[@id="facebook"]/body/div[4]/div[2]/div/div/div/div/div/div/div[2]/div[2]/label/input').click()
salt = ''.join(random.sample(string.ascii_letters + string.digits, 4))
sss = string.capwords(salt)
#输入东西
driver.find_element_by_xpath('//*[@id="facebook"]/body/div[4]/div[2]/div/div/div/div/div/div/div[2]/div[2]/label/input').send_keys(sss)
cf = ConfigParser()
cf.read("youxiang.cfg",encoding="utf-8")
eee = cf.get('youxiang',"yx")
driver.find_element_by_xpath('//*[@id="facebook"]/body/div[4]/div[2]/div/div/div/div/div/div/div[2]/div[4]/label/input').send_keys(eee)
time.sleep(4)
#点击继续按钮
driver.find_element_by_xpath('//*[@id="facebook"]/body/div[4]/div[2]/div/div/div/div/div/div/div[2]/div[4]/label/input').send_keys(Keys.TAB)
driver.find_element_by_xpath('//*[@id="facebook"]/body/div[4]/div[2]/div/div/div/div/div/div/div[3]/span[2]/div/div/button/div/div').click()
time.sleep(3)
#下拉框 (待完善)
#driver.find_element_by_xpath('//*[@id="facebook"]/body/div[5]/div[2]/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/button/div/div/div').click(on_element=None)

#下拉框以下
sj1 = ''

for i in range(5):
    current = random.randrange(0, 5)
    if current == i:
        tmp = chr(random.randint(65, 90))
    else:
        tmp = random.randint(0, 9)
    sj1 += str(tmp)
driver.find_element_by_xpath('//*[@id="facebook"]/body/div[5]/div[2]/div/div/div/div/div/div/div[2]/div/div[3]/div/label/input').send_keys(sj1)
#随机2
sj2 = ''

for i in range(5):
    current = random.randrange(0, 5)
    if current == i:
        tmp = chr(random.randint(65, 90))
    else:
        tmp = random.randint(0, 9)
    sj2 += str(tmp)
driver.find_element_by_xpath('//*[@id="facebook"]/body/div[5]/div[2]/div/div/div/div/div/div/div[2]/div/div[4]/div/label/input').send_keys(sj2)
#随机3
sj3 = ''

for i in range(5):
    current = random.randrange(0, 5)
    if current == i:
        tmp = chr(random.randint(65, 90))
    else:
        tmp = random.randint(0, 9)
    sj3 += str(tmp)
driver.find_element_by_xpath('//*[@id="facebook"]/body/div[5]/div[2]/div/div/div/div/div/div/div[2]/div/div[5]/div[1]/label/input').send_keys(sj3)
#随机4
sj4 = ''

for i in range(8):
    current = random.randrange(0, 5)
    if current == i:
        tmp = chr(random.randint(65, 90))
    else:
        tmp = random.randint(0, 9)
    sj4 += str(tmp)
driver.find_element_by_xpath('//*[@id="facebook"]/body/div[5]/div[2]/div/div/div/div/div/div/div[2]/div/div[5]/div[2]/label/input').send_keys(sj4)
#随机5
sj5 = ''

for i in range(6):
    current = random.randrange(0, 5)
    if current == i:
        tmp = chr(random.randint(65, 90))
    else:
        tmp = random.randint(0, 9)
    sj5 += str(tmp)
driver.find_element_by_xpath('//*[@id="facebook"]/body/div[5]/div[2]/div/div/div/div/div/div/div[2]/div/div[6]/div[1]/label/input').send_keys(sj5)
#随机11位数手机号
class PhoneNOGenerator():
    # 随机生成手机号码

    def phoneNORandomGenerator(self):
        prelist=["130","131","132","133","134","135","136","137","138","139","147","150","151","152","153","155","156","157","158","159","186","187","188"]
        return random.choice(prelist)+"".join(random.choice("0123456789") for i in range(8))


if __name__ == '__main__':
    pg = PhoneNOGenerator()
    sjh =  pg.phoneNORandomGenerator()
driver.find_element_by_xpath('//*[@id="facebook"]/body/div[5]/div[2]/div/div/div/div/div/div/div[2]/div/div[6]/div[2]/label/input').send_keys(sjh)
#随机网站
sj6 = ''
for i in range(6):
    current = random.randrange(0, 5)
    if current == i:
        tmp = chr(random.randint(65, 90))
    else:
        tmp = random.randint(0, 9)
    sj6 += str(tmp)
wz = 'wwww.' + sj6 +'.com'
driver.find_element_by_xpath('//*[@id="facebook"]/body/div[5]/div[2]/div/div/div/div/div/div/div[2]/div/div[7]/div/label/input').send_keys(wz)
#退出driver
os.system("taskkill /f /im chromedriver.exe")
