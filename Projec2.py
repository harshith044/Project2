##Project2:Web Scrapper using BeautifulSoup and requests

import requests
from bs4 import BeautifulSoup

oyo_url="https://www.oyorooms.com/hotels-in-anna-nagar-chennai/"

req=requests.get(oyo_url)
content=req.content

soup= BeautifulSoup(content,"html.parser")
all_hotels=soup.find_all("div",{"class":"hotelCardListing"})
scraped_info_list=[]

for hotel in all hotels:
    hotel_dict={}
    hotel_dict["name"]=hotel.find("h3",{"class":"listingHotelDscription_hotelName"}).text
    hotel_dict["address"]=hotel.find("span",{"itemprop":"streetAddress"}).text
    hotel_dict["price"]=hotel.find("span",{"class":"listingPrice__finalPrice"}).text
    #try...except
    try:
        hotel_rating=hotel.find("span",{"class":"hotelRating__ratingsummary"}).text
    concept AttributeError:
        pass

    parent_amenities_element=hote.find("div",{"class":"amenityWrapper"})

    amenities_list=[]
    for amenity in parent_amenities_element.find_all("div",{"class":"amenityWrapper__amenity"}):
        amenities_list.append("span",{"class":"d-body-smd-textEllipsis"}).text.strip()

        hotel_dict["amenities"]=','.join(amenities_list[:-1])
        scraped_info_list.append(hotel_dict)

    #print(hotel_name,hotel_address,hotel_price,hotel_rating)

dataFrame=pandas.DataFrame[scrapped_info_list)
dataFrame.to_csv("Oyo.csv")
