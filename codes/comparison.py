from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from bs4 import BeautifulSoup

from datetime import date, timedelta

import csv

def check_domestic(domestic_boolean: bool) -> str:
    if domestic_boolean == True:
        return "domestic"
    else:
        return ""

def check_reservation(reservation_boolean: bool) -> str:
    if reservation_boolean == True:
        return "OW"
    else:
        return "RT"

def get_domestic_ow_url(Departure_airport, Arrive_airport, Adult_num, Child_num, Infant_num, Departure_date) -> str:
    return "https://flight.naver.com/flights/results/domestic?trip=OW&fareType=YC&scity1={}&ecity1={}&adult={}&child={}&infant={}&sdate1={}".format(Departure_airport, Arrive_airport, Adult_num, Child_num, Infant_num, Departure_date)

def get_domestic_rt_url(Departure_airport, Arrive_airport, Adult_num, Child_num, Infant_num, Departure_date, Return_date) -> str:
    return "https://flight.naver.com/flights/results/domestic?trip=RT&fareType=YC&scity1={}&ecity1={}&adult={}&child={}&infant={}&sdate1={}&date2={}".format(Departure_airport, Arrive_airport, Adult_num, Child_num, Infant_num, Departure_date, Return_date)

def get_international_ow_url(Departure_airport, Arrive_airport, Adult_num, Child_num, Infant_num, Departure_date) -> str:
    return "https://flight.naver.com/v2/flights/results?trip=OWfareType=YC&scity1={}&ecity1={}&adult={}&child={}&infant={}&sdate1={}".format(Departure_airport, Arrive_airport, Adult_num, Child_num, Infant_num, Departure_date)

def get_international_rt_url(Departure_airport, Arrive_airport, Adult_num, Child_num, Infant_num, Departure_date, Return_date) -> str:
    return "https://flight.naver.com/v2/flights/results?trip=RT&fareType=YC&scity1={}&ecity1={}&adult={}&child={}&infant={}&sdate1={}&date2={}".format(Departure_airport, Arrive_airport, Adult_num, Child_num, Infant_num, Departure_date, Return_date)


# User Input

"""

받아야 하는 값
1. 왕복,편도
2. 서치할 기간 (시작일, 끝나는일) -> 년,월,일을 각각 따로 받아야함
3. 인원수

"""

reservation = True
arrival_airport = "USN"
adult_num = 1
child_num = 0 
infant_num = 0

start_year = 2020
start_month = 11
start_date = 30

end_year = 2020
end_month = 12
end_date = 1

# Example URL : https://flight.naver.com/flights/results/domestic?trip=OW&fareType=YC&scity1=GMP&ecity1=USN&adult=1&child=1&infant=1&sdate1=2021.11.06.

# Variables for Algorithm
domestic_departure_airport = "GMP"
international_departure_airport = "ICN,%20GMP"
flight_tickets = []
ticket_prices = []

start_day = date(start_year, start_month, start_date)
end_day = date(end_year, end_month, end_date)
delta = end_day - start_day

ticket_num = 0

extender = ".csv"
filename = "flight_ticket_lists"

#################
#################
### Functions ###
#################
#################

browser = webdriver.Chrome('./chromedriver.exe')
browser.maximize_window()

f = open(filename + extender, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

# Check for Period
try:
    for i in range(delta.days + 1):
        # 티켓 리스트 = [항공사, 정보, 좌석등급, 날짜, 가격]
        day = start_day + timedelta(days=i)
        str_day = str(day)
        str_day.replace("-",".")
        
        url = get_domestic_ow_url(domestic_departure_airport, arrival_airport, adult_num, child_num, infant_num, str_day + ".")
        
        browser.get(url)
        sort = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[3]/div[1]/a")))
        sort.click()
        price_sort = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[3]/div[1]/div/ul/li[1]")
        price_sort.click()

        soup = BeautifulSoup(browser.page_source, "lxml")
        
        # tickets = soup.find_all("li", attrs={"class":"trip_result_item ng-scope"})
        
        flight_companies = soup.find_all("span", attrs={"class":"h_tit_result ng-binding"})
        flight_infos = soup.find_all("div", attrs={"class":"route_info_box"})
        flight_seats = soup.find_all("span", attrs={"class":"sp_flight ico_seat"})
        flight_prices = soup.find_all("span", attrs={"class":"txt_pay ng-binding"})

        # flight_tickets.append(str_day)
        
        for flight_company, flight_info, flight_seat, flight_price in zip(flight_companies, flight_infos, flight_seats, flight_prices):
            list_for_append = []
            list_for_append.append(flight_company.text)
            list_for_append.append(flight_info.text)
            list_for_append.append(flight_seat.text)
            list_for_append.append(str(day))
            flight_price = flight_price.text
            flight_price = flight_price.replace(",","")
            list_for_append.append(int(flight_price))
            flight_tickets.append(list_for_append)

finally:
    sorted_flight_tickets = sorted(flight_tickets, key=lambda ticket: ticket[4])
    for sorted_flight_ticket in sorted_flight_tickets:
        print(sorted_flight_ticket)
    browser.quit()

