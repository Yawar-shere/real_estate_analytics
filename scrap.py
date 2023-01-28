from bs4 import BeautifulSoup
import requests
import json

# send request to the page and parse

# global dictionary for all the data
all_data = {"ads":[]}
# all_data1 = []
# variable for all the ads
last_index = -1

# extracts funtion to extract all the relevant data
def extract_data(lis):
    global last_index
    for index, li in enumerate(lis, last_index+1):
        # data dict for only one page
        data = {}

        # URL
        a_tag = li.find('a', class_="_7ac32433", href=True)
        
        # price
        price = li.find('span', class_="f343d9ce").text

        # try and catch for priority
        try:
            if li.find('div', class_="d1f22cbb").text:
                priority = li.find('div', class_="d1f22cbb").text
        except AttributeError:
            priority = "Normal"
        
        # try and catch for number of pictures
        try:
            if li.find('span', class_="_78f72f87").text:
                no_pic = li.find('span', class_="_78f72f87").text
        except AttributeError:
            no_pic = "No pictures available"

        # location
        location = li.find('div', class_="_162e6469").text
        
        # bedrooms, bathrooms and area of the land
        bnb = li.findAll('span', class_="_984949e5")

        bedBathandArea = {}

        # ittrate over the whole span to find the relevant data 
        for i in bnb:
            if i["aria-label"]  == "Beds":
                bedBathandArea["Beds"] = i.text
            elif i["aria-label"]  == "Baths":
                bedBathandArea["Baths"] = i.text
            elif i["aria-label"]  == "Area":
                bedBathandArea["Area"] = i.span.text


        # title of the ad
        title = li.find('h2', class_='c0df3811').text
        
        # added when
        added = li.find('div', class_='_08b01580').span.text

        # communication
        communicate = [li.find('button', class_="_5b77d672 da62f2ae _8d1154ff").text, li.find('button', class_="_85d9f2e2 a8197536 a8375d37").text]
        
        # append to dictionary
        data["ad#"] = index
        data["URL"] = a_tag['href']
        data["Price"] = price
        data["Priority"] = priority
        data["No. of pictures"] = no_pic
        data["Location"] = location
        data["Title"] = title
        data["Added"] = added
        data["Means"] = communicate
        data["BedBathandArea"] = bedBathandArea

        all_data["ads"].insert(index, data)
        # all_data1.insert(index, data)
        # print(all_data1)
    # updating the last index 
    last_index = index
    return all_data

# itrating over all the pages
for i in range(1, 7):
    html_text = requests.get(f'https://www.zameen.com/Homes/Karachi_Gadap_Town_Saima_Arabian_Villas-8856-{i}.html').text
    soup = BeautifulSoup(html_text, 'lxml')
    div = soup.find('ul', class_="_357a9937")
    lis = div.findAll('li', class_="ef447dde")
    extracted_data = extract_data(lis)


# writing over the json file
with open("data1.json", 'w', encoding='utf-8') as f:
    json.dump(extracted_data, f, ensure_ascii=False, indent=4)