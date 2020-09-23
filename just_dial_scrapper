from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_pid(plink):
    #plink = 'https://www.justdial.com/OnePlus-7T-RAM-8-GB-256-GB-Glacier-Blue/pid-174504318?city=Kharagpur&ncatid=11281356'
    index1 = plink.find('pid-')
    index2 = plink[index1+4:].find('?')
    return plink[index1+4:][:index2]
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
requests1=requests.get('https://www.justdial.com/Shop-Online',headers=headers)
soup1 = BeautifulSoup(requests1.content, 'html5lib')
product_id=[]
Price=[]
Brand_name=[]
Description=[]
Product_name=[]
urls=[]
product_info_list=[]
for x in soup1.find_all('a',{'class':'nav_menu'})[:200]:
    url1=x['href']
    requests2=requests.get(url1,headers=headers)
    soup2 = BeautifulSoup(requests2.content, 'html5lib')
    for z in soup2.find_all('div',{'class':'shopbox'}):
        price=z.find('span',{'class':'dt_price'}).string
        Price.append(price)
        url2=z.a['href']
        print(url2)
        urls.append(url2)
        pid=get_pid(url2)
        product_id.append(pid)
        requests3=requests.get(url2,headers=headers)
        soup3 = BeautifulSoup(requests3.content, 'html5lib')
        product_name=soup3.find('span',{'class':'fn'}).string
        Product_name.append(product_name)
        
        flag=True
        product_info=''
        for x in range(0,len(soup3.find_all('td')),2):
            if soup3.find_all('td')[x].string=='Brand Name':
                Brand_name.append(soup3.find_all('td')[x+1].string)
                flag=False
            else:
                
                try:
                    key = ''
                    key += soup3.find_all('td')[x].string
                except:
                    key = ''
                try:
                    val = ''
                    val+= soup3.find_all('td')[x+1].string
                except:
                    val = ''
                if key and val:
                    product_info+= key +':'+val +' || '
        product_info_list.append(product_info)
        if flag==True:
            Brand_name.append('')
        df = pd.DataFrame({'Product name':Product_name,"Brand_name":Brand_name,'Productid':product_id,'Price Rupees':Price,'URL':urls,'Prodcut info':product_info_list})
