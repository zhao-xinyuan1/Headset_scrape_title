import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from tqdm import tqdm
tqdm.pandas()
from random import randint
from time import sleep

Headset_keyword = ['Headset','buds','Buds','pods','Pods','Headphone','Earphone','ヘッドセット','耳机',
                   'auriculares','耳機','auricolare','Головной телефон','耳麥式麥克風','Kopfhörer']

def Add_description(query):
    # target url
    url = 'https://www.google.com/search?q=' + query + '&ie=utf-8&oe=utf-8'
    # making requests instance
    sleep(randint(1,2))
    try:
        reqs = requests.get(url)
    except:
        print("---Request error---")
        return 2
    # using the BeautifulSoup module
    soup = BeautifulSoup(reqs.text, 'html.parser')

    # soup.find.all( h3 ) to grab 
    # all major headings of our search result,
    heading_object=soup.find_all( 'h3' )

    # Iterate through the object 
    # and print it as a string.
    heading_title = [info.getText() for info in heading_object]
    print(heading_title)
    if not len(heading_title):
        print("---Google blocked search---")
    for headset_keyword in Headset_keyword:
        if any(headset_keyword in s for s in heading_title):
            return 1
    return 0

#df = pd.read_csv('C:\\Users\\Xinyuan Zhao\\source\\repos\\Headset_device_list\\Headset_device_list\\removed_prefix_suffix.csv',index_col=0,skiprows = [i for i in range(1,600)])
#print('------ Description Filter:--------')
#df['headset_description'] = df['MIC'].progress_apply(Add_description)

#df.to_csv('C:\\Users\\Xinyuan Zhao\\source\\repos\\Headset_device_list\\Headset_device_list\\removed_prefix_suffix_beta.csv')
print(Add_description('Neckband'))