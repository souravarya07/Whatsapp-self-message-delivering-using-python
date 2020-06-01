from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
name = input('Enter the name of user or group: ')
msg = input('Enter the message: ')
count = int(input('Enter the count: '))
input("Enter anything after scanning the QR code")

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

#the class name for message box will be different for different person using the whatsapp-web.
#Steps to find the class Name:
#1. Open the whatsApp-Web once in your Machine.
#2. Open the random chatbox of anyone, and over at the space where we type our message.
#3. Right click on the message box and look for inspect.
#4. You'll find the class_name for the message box in the inspect tool
#5. Change it accordingly.
msg_box = driver.find_element_by_class_name('_1Plpp')

for i in range(count):
    msg_box.send_keys(msg)
    #Same steps to be followed to find the class name for send button.
    button = driver.find_element_by_class_name('_35EW6')
    button.click()
