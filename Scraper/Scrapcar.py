import requests
import time
import fbchat


from bs4 import BeautifulSoup
ua = "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
username = "xxxx"
password = "xxxx"
client = fbchat.Client(username, password, ua)
friends = client.searchForUsers("xxxx xxx")
friend = friends[0]

url = "https://www.car.gr/classifieds/cars/?condition=used&make=15&make=155&make=192&make=198&make=205&make=22&make=242&make=248&make=34&make=59&make=646&make=9&mileage-from=%3E3000&mileage-to=%3C200000&offer_type=sale&onlyprice=1&pg=1&price-from=%3E1000&price-to=%3C2000&price=%3E50&registration-from=1997&registration-to=2021&rg=1&rg=2&rg=3&significant_damage=f&sort=dm"

first = 0
timecounter = 0
while True:
    counter = 0
    if (first == 0):
        first = 1
        timecounter = 0
    if (timecounter == 100):
        client = fbchat.Client(username, password, ua)
        timecounter = 0
        
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    substring = "classifieds/cars/view/"
    for a in soup.find_all('a', href=True):
        string = a['href']
        found = 0
        
        if substring in string.strip('\n '):

            file1 = open('cars.txt', 'r')
            Lines = file1.readlines()
            for line in Lines:
                if (line.strip('\n') == string):
                    found=1
            file1.close() 

            if (found == 0):
                sent = client.sendMessage("www.car.gr"+string, thread_id=friend.uid)
                if sent:
                    print("Message sent successfully!")
                else:
                    print("no")
                    
                counter = counter + 1
                print (string)
                file_object = open('cars.txt', 'a')
                file_object.write(string)
                file_object.write('\n')
                file_object.close()
    print("Found "+str(counter)+" new cars!")
    timecounter = timecounter + 1
    found = 0
    counter = 0
    time.sleep(300)
