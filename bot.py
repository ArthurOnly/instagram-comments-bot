from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def start_driver():
    try:
        global driver
        driver = webdriver.Chrome(executable_path="C:\Program Files\webdriver/chromedriver")
    except:
        print("Webdriver not found")
        exit()

def user_login_data():
    login_with_facebook = input("Login with facebook? (y/n) ")
    if login_with_facebook.startswith('y'):
        email_username = input("Email or celphone: ")
    else:
        email_username = input("Username, celphone or email: ")
    password = input("Password: ")
    return login_with_facebook,email_username,password

def coments_data():
    comment_post = input("Post url that will recive comments: ")
    comments = input("Coments, separeted by ',': ").split(',')
    comments_interval = input("Interval between comments in seconds: ")
    repeat = input("Number of times that must be repeated(1 is minimum): ")
    return comment_post,comments,comments_interval,repeat

def login_with_facebook(email_username,password):
    driver.get('https://www.instagram.com/')
    sleep(3)

    #Go to Facebook
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[5]/button').click()
    
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(email_username)
    driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)

    #Facebook login button
    driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
    sleep(3)

def login_with_instagram(email_username,password):
    driver.get('https://www.instagram.com/')
    sleep(3)

    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(email_username)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)

    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()

def comment(comment_post,comments,comments_interval,repeat):
    driver.get(comment_post)
    sleep(4)

    comment_area_path = '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea'
    comment_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button')
    
    for i in range(int(repeat)):
        for comment in comments:
            #Detalhe importante, não da para selecionar o elemento diretamente, pois ele é dinamico, e sua referencia muda a cada interação, então sempre que for tratar
            #o textarea é preciso seleciona-lo novamente
            driver.find_element_by_xpath(comment_area_path).click()
            driver.find_element_by_xpath(comment_area_path).send_keys(comment)
            comment_button.click()
            sleep(int(comments_interval))

start_driver()
