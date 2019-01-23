import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def main():
    user_name = ""
    password = ""

    driver = webdriver.Firefox(executable_path="/Users/kudouhibiki/PycharmProjects02/sample_python/geckodriver")
    driver.get("https://twitter.com/")
    driver.find_element_by_name("session[username_or_email]").send_keys(user_name)
    time.sleep(3)
    driver.find_element_by_name("session[password]").send_keys(password)
    driver.find_element_by_name("session[password]").send_keys(Keys.ENTER)
    time.sleep(3)

    driver.find_element_by_id("tweet-box-home-timeline").send_keys("python教えているけど、新発見いろいろ思い出せて楽しい！")
    time.sleep(1)
    driver.find_element_by_xpath("""//span[@class="button-text tweeting-text"]""").click()


if __name__ == "__main__":
    main()
