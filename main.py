import time,ccxt,constants
auth_client = ccxt.phemex({
        'apiKey': constants.key,
        'secret': constants.secret,
})
def getMarket(market,side,ammount,price):
    return auth_client.create_order(market,'Limit',side,ammount,price)
def findCurrencyPrice(market):
    try:
        return auth_client.fetch_ticker(market)['last']
    except:
        return findCurrencyPrice(market)
def getLastTrade(symbol):
    try:
        return auth_client.fetch_my_trades(symbol)[-1]
    except:
        return getLastTrade(symbol)
def checkMarketOrder():
    if auth_client.has['createMarketOrder']:
        return 'yes'
    else:
        return 'no'
def getBalance():
    try:
        return auth_client.fetch_balance()
    except:
        return getBalance()
print(ccxt.__version__)
market = 'DOT'
symbol = 'sDOTUSDT'
profit = 0
print(auth_client.create_order(symbol,'Market','buy',1.5))
coins = getBalance()[market]['total']
trade = getLastTrade('DOT/USDT')
print(trade['price'])
totalCost = (trade['price']+(trade['price']*0.001))*1.5
print(totalCost)
lastVar = trade['price']
print(lastVar)
#auth_client.cancel_all_orders(symbol)
while(True):
    coins = getBalance()[market]['total']
    marketPrice = findCurrencyPrice(symbol)
    lastTrade = getLastTrade('DOT/USDT')
    ammount = 0.5
    try:
        orderPrice = getLastTrade('DOT/USDT')['price']
    except:
        orderPrice = findCurrencyPrice(symbol)
    orders = auth_client.fetch_open_orders(symbol)
    try:
        print(orders[0]['side'])
        print(orders[1]['side'])
    except:
        balance = getBalance()
        print(lastTrade['price'])
        if(lastTrade['side'] == 'buy' and lastTrade['price'] != lastVar):
            totalCost += ((lastTrade['price'] + (lastTrade['price']*0.001))/2)
            print('increased totalCost')
        if(lastTrade['side'] == 'sell' and lastTrade['price'] != lastVar):
            profit = ((marketPrice-(marketPrice*0.001))-(totalCost/coins))
            totalCost -= ((lastTrade['price'] + (lastTrade['price']*0.001))/2)
            print('decreased totalCost')
        if(profit > 10):
            print('done')
            #auth_client.create_order('sBTCUSDT','Market','buy',ammount)
        if(balance['USDT']['free']>(ammount*marketPrice) + (int((orderPrice+(orderPrice*0.00101))*1000)/float(1000))/marketPrice and balance['DOT']['free']*marketPrice>(ammount*marketPrice) + (round(orderPrice+(orderPrice*0.00101),3)/marketPrice)):
            auth_client.cancel_all_orders(symbol)
            print('creating sell limit order')
            print(getMarket(symbol,'sell',ammount,round(orderPrice+(orderPrice*0.001),3)))
            print('creaing buy limit order')
            print(getMarket(symbol,'buy',ammount,int(abs(orderPrice-(orderPrice*0.001))*1000)/float(1000)))
    print('restarting')
    print('profit: '+ str(profit))
    print('totalCost: ' + str(totalCost))
    print('coins: ' + str(coins))
    print(totalCost/coins)
    lastVar = lastTrade['price']
    time.sleep(1)



