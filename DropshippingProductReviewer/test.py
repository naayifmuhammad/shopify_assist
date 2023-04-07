import pickle
with open('shippingInfo.pkl','rb') as file:
    car = pickle.load(file)
    print(car['Austria']['CJPacket Ordinary']['averageShippingTime'][1])