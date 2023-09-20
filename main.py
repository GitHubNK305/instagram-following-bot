import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException


SIMILAR_ACCOUNT = "helsinkidesignweek"
USERNAME = "your user name"
PASSWORD = "your password"


class InstaFollower:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 '''/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]''').click()

        # login Instagram
        time.sleep(2)
        email = self.driver.find_element(By.XPATH, '''//*[@id="loginForm"]/div/div[1]/div/label/input''')
        email.send_keys(USERNAME)

        password = self.driver.find_element(By.XPATH, '''//*[@id="loginForm"]/div/div[2]/div/label/input''')
        password.send_keys(PASSWORD)

        self.driver.find_element(By.XPATH, '''//*[@id="loginForm"]/div/div[3]/button''').click()

        time.sleep(1)
        self.driver.maximize_window()
        # something wrong with this step
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 '''/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button''').click()
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, '''//*[@id="mount_0_0_iI"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button''').click()

        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 '''/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]''').click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")

        time.sleep(3)

        self.driver.find_element(By.XPATH,
                                 '''/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a''').click()

        # time.sleep(2)
        # scrollable_popup = self.driver.find_element(By.XPATH,
        #                                             '''/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]''')
        # for i in range(5):
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_popup)
        #     time.sleep(2)

    def follow(self):
        for i in range(1, 50):
            print(f"Following {i}th person")
            time.sleep(1)
            follow_button = self.driver.find_element(By.XPATH,
                                                     f'''/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{i}]/div/div/div/div[3]/div/button''')
            try:
                follow_button.click()
                time.sleep(1)
            # except NoSuchElementException:
            #     print(f"Can't find {i}th person")
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '''/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]''')
                cancel_button.click()
            # self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follow_button)


bot = InstaFollower()

bot.login()
bot.find_followers()
bot.follow()
