from importList import *

def scrapeAndStoreDataInBinary():
    CARRIER_INFO = dict()
    with open("shippingInfo.pkl","wb") as shippingLog:
            for country in countryList:
                CARRIER_INFO[country] = {}
                countryDropDown.select_by_visible_text(country)
                time.sleep(2)
                print(f"Processing {country}\n")
                li_tags = driver.find_elements(By.CLASS_NAME,'logisticListItem')
                for li in li_tags:
                    try:
                        ObjectLoader.until(EC.presence_of_element_located((By.CLASS_NAME,"ng-binding")))
                    finally:
                        spans = li.find_elements(By.CLASS_NAME,'ng-binding')
                        span_values = [s.get_attribute("innerHTML") for s in spans]
                        carrierName = span_values[0] 
                        carrierShippingRate = span_values[4]
                        carrierShippingTime = span_values[6]
                        CARRIER_INFO[country][carrierName] = {}
                        CARRIER_INFO[country][carrierName]['totalShippingRate'] = processRange(carrierShippingRate) 
                        CARRIER_INFO[country][carrierName]['averageShippingTime'] = processRange(carrierShippingTime)
            pickle.dump(CARRIER_INFO,shippingLog)

                    

chrome_options = Options()
chrome_options.add_argument('--headless') 
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=chrome_options)
url = "https://cjdropshipping.com/product/fashionable-knitted-creative-mid-calf-animal-socks-p-1598856686205415424.html"
driver.get(url)
ObjectLoader = WebDriverWait(driver,30)
try:
    ObjectLoader.until(EC.presence_of_element_located((By.ID, "country-list-sele")))
finally:
    countryDropDown= Select(driver.find_element(By.ID, "country-list-sele"))
    try:
        ObjectLoader.until(EC. presence_of_element_located((By.TAG_NAME, "option")))   
    finally:
        time.sleep(3)
        scrapeAndStoreDataInBinary()



        
        




