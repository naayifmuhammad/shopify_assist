##########################  VARIABLES AND MISC    ###################################

import pickle
from pprint import pprint
from os import system as sys
FILEDIR = "shippingInfo.pkl"
PROD_PRICE = 100 #fetch price of product later
MAX_SHIPPING_DATE = 18
MAX_PERCENTAGE = 30
RRP = 30
sys('cls')
VIABLE_OPTIONS = {}
##########################  VARIABLES AND MISC END    ###################################






###################################################################################
###################### Parameter customization function ###########################

def customizeParameters():
    global RRP
    global MAX_PERCENTAGE
    global MAX_SHIPPING_DATE
    RRP = float(input("How much do you plan on selling this product for? "))
    MAX_SHIPPING_DATE = int(input("What is the maximum days a product can take to ship? :"))
    MAX_PERCENTAGE = float(input("How much can shipping cost? [Upto ___ \% of RRP]"))
###################################################################################





###################################################################################
option = input("Do you wish to customize the search parameters? [yes/no]")
customizeParameters() if option=="yes" else "Continuing with default parameters"
###################################################################################



################################## deserialize .pkl file to get data for processing.########################################
def getshippingInfo(): #deserialise the binary file to give input to the isItViable funtion..works when no arguments are given. Otherwisw there is no need for serialisation
    with open(FILEDIR,'rb') as file:
        return pickle.load(file)
############################################################################################################################



##############################  DISPLAY FUNCTIONS    ######################################
def displayCountriesOnly(results,total):
    print(f"--------------Country List [{len(results)}/{total}]--------------")
    for country in results:
        print(country,'\n')
    print("----------------------------------------")

def displayDetailed(results,total):
    print(f"\n============================\nViable Countries to ship to [{len(results)}/{total}]\n============================\n")
    for result in results:
        print("-------------------------------------------------------------------------")
        print(f"\nCountry => {result}:\nBest carriers:\n\n")
        for carrier in results[result]:
            rate = results[result][carrier]["totalShippingRate"]
            shippingTime = results[result][carrier]["averageShippingTime"]
            print(f'{carrier}\tShipping cost =>{rate}\tShipping time =>{shippingTime} "\n')
        print("\n==============================================================================================================\n")

##############################  DISPLAY FUNCTIONS END ######################################





##############################  DATA FILTERING ######################################

def isItViable(shippingInfo=getshippingInfo()):
    print("\n==========================================\nStarting operation..\n==========================================\n")
    global VIABLE_OPTIONS
    if not shippingInfo:
        return "Error : couldn't get info"
    
    for country in shippingInfo:
        VIABLE_OPTIONS[country]={}
        for carrier in shippingInfo[country]:
            if shippingInfo[country][carrier]['averageShippingTime'][1] < MAX_SHIPPING_DATE:
                #print(f"{shippingInfo[country][carrier]['averageShippingTime'][1]} < {MAX_SHIPPING_DATE}")
                if float(shippingInfo[country][carrier]['totalShippingRate'][1]) < (MAX_PERCENTAGE / 100 * RRP):
                    #print(f"{shippingInfo[country][carrier]['totalShippingRate'][1]} < {(MAX_PERCENTAGE / 100 * RRP)}")
                    VIABLE_OPTIONS[country][carrier] = shippingInfo[country][carrier]
    option = int(input("[1] Show countries only\n[2] Show viable countries with details: \nEnter your choice: "))
    displayCountriesOnly(VIABLE_OPTIONS,len(shippingInfo)) if option==1 else displayDetailed(VIABLE_OPTIONS,len(shippingInfo))
##############################  DATA FILTERING END ######################################


#starting here
isItViable()
    
