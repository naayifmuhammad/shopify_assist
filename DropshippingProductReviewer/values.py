import re

def processRange(incomingRange):
     bounds=[]
     #check if it's a date range price range
     patternPriceRange = r'^\$\d+\.\d+-\d+\.\d+$'
     date_range_regex = r'(\d+)-(\d+)\s+days'   
     if re.match(patternPriceRange, incomingRange):
         # Remove the dollar sign and split the string by the hyphen
         bounds = incomingRange.replace("$", "").split("-")
         # Convert each string to float and then to integer
         bounds = [float(x) for x in bounds]
         return bounds
     elif re.match(date_range_regex,incomingRange):
         bounds = re.search(r'(\d+)-(\d+)\s+days', incomingRange)
         bounds = [int(bounds.group(1)),int(bounds.group(2))]
         return bounds
     else:
         incomingRange = incomingRange.replace("$", "")
         bounds = [0,incomingRange]
         bounds = [float(x) for x in bounds]
         return bounds



def isProductShippingViable(shippingTimes):
    pass