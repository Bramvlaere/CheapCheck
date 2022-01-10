from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import requests 
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import statistics
from tkinter import *
from tkinter import simpledialog
from tkinter import ttk
from PIL import ImageTk,Image
import tkinter as tk


from pathlib import Path

# from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage





#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
options = webdriver.ChromeOptions()
options.add_argument("headless")
#driver = webdriver.Chrome(executable_path='/Users/vanlaere/Documents/sideprojects/CheapChecker/chromedriver', chrome_options=options)
                            
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
y=0
def click():
    usr_url=entry_1.get()
    #url="https://www.amazon.com/s?k="+usr_url

    #shopindex=['https://www.amazon.com/s?k=','https://www.bjs.com/search/','https://www.walmart.com/search?q=','https://www.samsclub.com/s/']
    shopindex=['https://www.target.com/s?searchTerm=','https://www.fairwaymarket.com/sm/delivery/rsid/183/results?q=']

    def getitemlinks(item):
        user_link_index=[]
        for i in range(len(shopindex)):
            shopindex[i]=shopindex[i]+usr_url
            user_link_index.append(shopindex[i])
        print(user_link_index)
        return user_link_index

    user_link_index=getitemlinks(usr_url)
    value=0
    def gettabs(user_link_index):
        for i, value in enumerate(user_link_index):
                    driver.get(value)
                    #when it is the last cycle we don't need another window
                    driver.execute_script("window.open('');")
                    driver.switch_to.window(driver.window_handles[i+1])
                    #time.sleep(3) #to make sure nothing goes to fast can be excluded once finalisation of script

    gettabs(user_link_index)

    #take the right product

    def fairwaygetproducts():
        driver.switch_to.window(driver.window_handles[1])
        fairway_list=driver.find_elements_by_class_name('ColListing-sc-lcurnl.kYBrWq')
        print(fairway_list,len(fairway_list))
        price_l=[]
        for product in fairway_list:
            value=0
            value=product.find_element_by_class_name('Image-sc-1dk4b58.eFWKwZ.ProductCardImage-sc-hbeh8u.cbSHZe')#for the title
            #print(f'this is product numnber{value.text}')
            product_description=value.get_attribute("alt")
            try:
                price=product.find_element_by_class_name('ProductCardPrice-sc-zgh1l1.dfxUih')
            except:
                price=product.find_element_by_class_name('ProductCardPricing-sc-4r7vrc.dziBkm')
            price=price.text[1:5]
            try:
                price_l.append(float(price))
            except:
                price_l.append(0)
            print(f'These are all the items I found at Fairway for {usr_url} :{product_description} for a price of : ${price}')
        average_p=statistics.mean(price_l)
        mode=statistics.mode(price_l)
        median=statistics.median(price_l)
        print('#'*25)
        print(f'The average price of {usr_url} at fairway is {average_p}\n')
        print('_'*25)
        print(f'The most common price asked for {usr_url} is {mode}\n')
        print('_'*25)
        print(f'The Median for the prices for {usr_url} is {median}\n')
        print('_'*25)
        print(f'The cheapest price for {usr_url} is {min(price_l)>0}\n')
        print('fairway prices',price_l)
        print('#'*25)

        
            #work with mean to find the average price 

    fairwaygetproducts()

    def targetgetproducts():
        driver.switch_to.window(driver.window_handles[0])
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") 
        target_list=driver.find_elements_by_class_name('Col-sc-favj32-0.epICLY.h-padding-a-none.h-display-flex')#
        price_l=[]
        c=95.0
        for i,product in enumerate(target_list):
            res=0
            productinfo=product.text.split('\n')
            #try:
            res=[x for x in productinfo if '$' in x]
            try:
                price=float(res[0][1:])
            except:
                price=0
            product_description=productinfo[0]
            price_l.append(price)
            productinfo=[]
            canvas.create_text(208.0,c,anchor="nw",text=f"{usr_url} at Target :{product_description}: ${price}'",fill="#192A3E",font=("Poppins Small", 11 * -1))
            c+=20
            
            #print(f'These are all the items I found at Target for {usr_url} : Product :{product_description} for a price of : ${price}')
        average_p=statistics.mean(price_l)
        mode=statistics.mode(price_l)
        median=statistics.median(price_l)
        price_l=[x for x in price_l if x is not 0]
        print('#'*25)
        print(f'The average price of {usr_url} at Target is {average_p}\n')
        print('_'*25)
        print(f'The most common price asked for {usr_url} is {mode}\n')
        print('_'*25)
        print(f'The Median for the prices for {usr_url} is {median}\n')
        print('_'*25)
        print(f'The cheapest price for {usr_url} is {min(price_l)} \n')
        print('#'*25)

        print(price_l)
    targetgetproducts()

    def walmartgetproducts():
        driver.switch_to.window(driver.window_handles[2])
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") 



    walmartgetproducts()

    

    '''def selectproductitems():
        driver.switch_to.window(driver.window_handles[1])
        fairway_products=driver.find_element_by_class_name('Image-sc-1dk4b58.eFWKwZ.ProductCardImage-sc-hbeh8u.cbSHZe')
        print(fairway_products.get_attribute("alt"))



        #ProductCardTitle-sc-ye20s3.iLdpjY

        



        for product in fairway_products:
        print(product.text)
            title=product.find_elements_by_xpath('//*[@id="pageMain"]/div/div/div/div/section[1]/section[1]/div[2]/div[1]/article/span')
            image=product.find_elements_by_xpath('.//*[@id="pageMain"]/div/div/div/div/section[1]/section[1]/div[2]/div[1]/article/div[2]')
            price=product.find_elements_by_xpath('.//*[@id="pageMain"]/div/div/div/div/section[1]/section[1]/div[2]/div[1]/article/div[6]/span[1]/span')
            #print(f'I have found these items\n Title:{title}\n Image:{image}\n Price:{price}')
        

    selectproductitems()
    '''

    #ColListing-sc-lcurnl kYBrWq <- class
    #//*[@id="pageMain"]/div/div/div/div/section[1]/section[1]/div[2]/div[1]/article/div[6]   <price
    #//*[@id="pageMain"]/div/div/div/div/section[1]/section[1]/div[2]/div[1]/article/span   <title
    #//*[@id="pageMain"]/div/div/div/div/section[1]/section[1]/div[2]/div[1]/article/div[2] <image








OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("CheapChecker")

window.geometry("983x581")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 581,
    width = 983,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    983.0,
    581.0,
    fill="#E5E5E5",
    outline="")

canvas.create_rectangle(
    194.0,
    39.0,
    638.0,
    567.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    656.0,
    39.0,
    972.0,
    297.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    656.0,
    309.0,
    972.0,
    567.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    175.0,
    581.0,
    fill="#2ED47A",
    outline=""),
    

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    579.0,
    15.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=175.0,
    y=0.0,
    width=808.0,
    height=28.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    87.0,
    41.0,
    image=image_image_1
)

canvas.create_text(
    208.0,
    55.0,
    anchor="nw",
    text="These prices were found",
    fill="#192A3E",
    font=("Poppins Medium", 11 * -1)
)

canvas.create_text(
    39.0,
    91.0,
    anchor="nw",
    text="Shopping Cart",
    fill="#FFFFFF",
    font=("Poppins Medium", 11 * -1)
)

canvas.create_text(
    674.0,
    55.0,
    anchor="nw",
    text="This data was found based the price",
    fill="#192A3E",
    font=("Poppins Medium", 11 * -1)
)

canvas.create_rectangle(
    656.0,
    91.0,
    972.0,
    92.0,
    fill="#EBEFF2",
    outline="")

canvas.create_text(
    674.0,
    325.0,
    anchor="nw",
    text="This is more data",
    fill="#192A3E",
    font=("Poppins Medium", 11 * -1)
)

canvas.create_rectangle(
    656.0,
    361.0,
    972.0,
    362.0,
    fill="#EBEFF2",
    outline="")

canvas.create_rectangle(
    194.0,
    91.0,
    638.0,
    92.0,
    fill="#EBEFF2",
    outline="")

canvas.create_rectangle(
    0.0,
    81.0,
    175.0,
    82.0,
    fill="#EBEFF2",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=click,
    relief="flat"
)
button_1.place(
    x=869.58984375,
    y=0.13671875,
    width=113.34823608398438,
    height=29.5546875
)



window.resizable(False, False)
window.mainloop()


