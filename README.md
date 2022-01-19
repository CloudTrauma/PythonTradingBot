# PythonTradingBot
Python Trading Bot that buys and sells while still making profits despite fees

Link to ccxt: https://github.com/ccxt/ccxt

To get started, do 
```python
pip install ccxt
```
You will also need a separate file to hold your keys
In my case I made a file called 
```constants.py```
and put in 
```python
key = 'api_key'
secret = 'api_secret'
```
Replace api_key with you key and the api_secret with the secret(make sure to keep the qoutes)

I use limit orders instead of market orders because I havent fixed the issue with CCXT market buys being delayed and also it leaves the exchange to fill the orders when needed instead of coding it to.

Variables to change:

```python
nod = 3
```
change the nod(number of decimal points) for the crypto currency you use

```python
fee = 0.001
```
depending on what exchange you use the fee will be different. I use Phemex which has a 0.1% fee or 0.001 fee

```python 
market = 'DOT'
```
the market is the name of the cryptocurrency you use. I am using DOT crypto in this case

```python
symbol = 'sDOTUSDT'
```
The symbol is the name of the crypto pair. In phemex the crypto pair is DOT/USDT and the s means spot while DOTUSD would be for futures or contracts

If you got any issues, just create a issue and i will try to help you
