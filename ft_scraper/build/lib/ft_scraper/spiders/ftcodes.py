import os

dirpath = os.path.abspath(os.path.dirname(__file__))
filepathcodes = os.path.join(dirpath,"ftcodes.txt")
filepathtickers = os.path.join(dirpath,"tickers.txt")

with open(filepathcodes,"r") as f:
    ftcodes= [ticker.replace("\n","") for ticker in f.readlines()]

with open(filepathtickers,"r") as f:
    tickers = [ticker.replace("\n","") for ticker in f.readlines()]

url = "https://markets.ft.com/data/equities/ajax/get-historical-prices?startDate=2018%2F03%2F01&endDate=2018%2F03%2F09&symbol={0}"

urls = list()
for code in ftcodes:
    code = int(code)
    temp_url = url.format(code)
    urls.append(temp_url)
