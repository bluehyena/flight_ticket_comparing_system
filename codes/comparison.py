from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from bs4 import BeautifulSoup

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
reservation = True
search_period = 7
domestic_departure_airport = "GMP"
international_departure_airport = "ICN,%20GMP"
arrival_airport = "USN"
adult_num = 1
child_num = 0 
infant_num = 0

departure_date_year = 2020
departure_date_month = 11
departure_date_date = 21

return_date_year = 2020
return_date_month = 3
return_date_date = 1

# Example URL : https://flight.naver.com/flights/results/domestic?trip=OW&fareType=YC&scity1=GMP&ecity1=USN&adult=1&child=1&infant=1&sdate1=2021.11.06.

# Variables for Algorithm

flight_tickets = []

#################
#################
### Functions ###
#################
#################

browser = webdriver.Chrome('./chromedriver.exe')
browser.maximize_window()

try:
    for date in range(search_period):
        url = get_domestic_ow_url(domestic_departure_airport, arrival_airport, adult_num, child_num, infant_num,str(departure_date_year) + "." + str(departure_date_month) + "." + str(departure_date_date + date))
        browser.get(url)
        sort = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[3]/div[1]/a")))
        sort.click()
        price_sort = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[3]/div[1]/div/ul/li[1]")
        price_sort.click()

        soup = BeautifulSoup(browser.page_source, "lxml")
        tickets = soup.find_all("li", attrs={"class":"trip_result_item ng-scope"})
        
        flight_tickets.append(str(departure_date_year) + "." + str(departure_date_month) + "." + str(departure_date_date + date))
        
        for ticket in tickets:
            flight_tickets.append(ticket.text)
    
    for flight_ticket in flight_tickets:
        print(flight_ticket)

finally:
    browser.quit()

