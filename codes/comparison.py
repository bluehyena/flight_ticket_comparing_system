from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from bs4 import BeautifulSoup

from datetime import date, timedelta

def check_domestic(domestic_type: str) -> str:
    if domestic_type in ["CJU","PUS","USN","KWJ","RSU","TAE","YNY","GMP","ICN"]:
        return "domestic"
    else:
        return ""

def get_domestic_ow_url(Departure_airport, Arrive_airport, Adult_num, Child_num, Infant_num, Departure_date) -> str:
    return "https://flight.naver.com/flights/results/domestic?trip=OW&fareType=YC&scity1={}&ecity1={}&adult={}&child={}&infant={}&sdate1={}".format(Departure_airport, Arrive_airport, Adult_num, Child_num, Infant_num, Departure_date)

def get_international_ow_url(Departure_airport, Arrive_airport, Adult_num, Child_num, Infant_num, Departure_date) -> str:
    return "https://flight.naver.com/flights/v2/results?trip=OW&scity1={}&ecity1={}&adult={}&child={}&infant={}&sdate1={}&fareType=Y".format(Departure_airport, Arrive_airport, Adult_num, Child_num, Infant_num, Departure_date)

def ow_compare(inputdata: list) -> list:
    arrival_airport = inputdata[0]
    reservation = inputdata[1]

    start_year = int(inputdata[2])
    start_month = int(inputdata[3])
    start_date = int(inputdata[4])

    end_year = int(inputdata[5])
    end_month = int(inputdata[6])
    end_date = int(inputdata[7])

    infant_num = int(inputdata[8].replace("명", ""))
    child_num = int(inputdata[9].replace("명", ""))
    adult_num = int(inputdata[10].replace("명", ""))

    # Example URL : https://flight.naver.com/flights/results/domestic?trip=OW&fareType=YC&scity1=GMP&ecity1=USN&adult=1&child=1&infant=1&sdate1=2021.11.06.

    # Variables for Algorithm
    domestic_departure_airport = "GMP"
    international_departure_airport = "ICN,%20GMP"
    flight_tickets = []
    ticket_prices = []

    start_day = date(start_year, start_month, start_date)
    end_day = date(end_year, end_month, end_date)
    delta = end_day - start_day

    browser = webdriver.Chrome('../chromedriver.exe')
    browser.maximize_window()

    try:
        for i in range(delta.days + 1):
            
            # Ticket_Lists = [Company, Infomation, Class, Date, Price]
            
            day = start_day + timedelta(days=i)
            str_day = str(day)
            str_day.replace("-",".")
            
            # Check domestic and make URL
            if check_domestic(arrival_airport) == "domestic":
                url = get_domestic_ow_url(domestic_departure_airport, arrival_airport, adult_num, child_num, infant_num, str_day + ".")

                browser.get(url)
                sort = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[3]/div[1]/a")))
                sort.click()
                price_sort = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[3]/div[1]/div/ul/li[1]")
                price_sort.click()

                soup = BeautifulSoup(browser.page_source, "html.parser")
                
                flight_companies = soup.find_all("span", attrs={"class":"h_tit_result ng-binding"})
                flight_infos = soup.find_all("div", attrs={"class":"route_info_box"})
                flight_seats = soup.find_all("div", attrs={"class":"txt_seat ng-binding"})
                flight_prices = soup.find_all("span", attrs={"class":"txt_pay ng-binding"})
                
                for flight_company, flight_info, flight_seat, flight_price in zip(flight_companies, flight_infos, flight_seats, flight_prices):
                    list_for_append = []
                    list_for_append.append(flight_company.text)
                    list_for_append.append(flight_info.text)
                    list_for_append.append(flight_seat.text)
                    list_for_append.append(str(day))
                    flight_price = flight_price.text
                    flight_price = flight_price.replace(",","")
                    list_for_append.append(int(flight_price))
                    list_for_append.append(url)
                    flight_tickets.append(list_for_append)

            else:
                url = get_international_ow_url(international_departure_airport, arrival_airport, adult_num, child_num, infant_num, str_day + ".")

                browser.get(url)
                sort = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[3]/div[1]/a")))
                sort.click()
                price_sort = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[3]/div[1]/div/ul/li[1]")
                price_sort.click()

                soup = BeautifulSoup(browser.page_source, "html.parser")
                
                flight_companies = soup.find_all("span", attrs={"class":"h_tit_result ng-binding"})
                flight_infos = soup.find_all("div", attrs={"class":"route_info_box"})
                flight_seats = soup.find_all("a", attrs={"class":"btn_pay_terms btn_pay_terms_v2 ng-binding"})
                flight_prices = soup.find_all("span", attrs={"class":"txt_pay ng-binding"})
                
                for flight_company, flight_info, flight_seat, flight_price in zip(flight_companies, flight_infos, flight_seats, flight_prices):
                    list_for_append = []
                    list_for_append.append(flight_company.text)
                    list_for_append.append(flight_info.text)
                    list_for_append.append(flight_seat.text)
                    list_for_append.append(str(day))
                    flight_price = flight_price.text
                    flight_price = flight_price.replace(",","")
                    list_for_append.append(int(flight_price))
                    list_for_append.append(url)
                    flight_tickets.append(list_for_append)

    finally:
        sorted_flight_tickets = sorted(flight_tickets, key=lambda ticket: ticket[4])
        return sorted_flight_tickets
        browser.quit()

def rt_compare(inputdata: list) -> str:
    arrival_airport = inputdata[0]
    reservation = inputdata[1]

    start_year = int(inputdata[2])
    start_month = int(inputdata[3])
    start_date = int(inputdata[4])

    end_year = int(inputdata[5])
    end_month = int(inputdata[6])
    end_date = int(inputdata[7])

    infant_num = int(inputdata[9].replace("명", ""))
    child_num = int(inputdata[10].replace("명", ""))
    adult_num = int(inputdata[11].replace("명", ""))

    period = int(inputdata[8])

    # Example URL : https://flight.naver.com/flights/results/domestic?trip=OW&fareType=YC&scity1=GMP&ecity1=USN&adult=1&child=1&infant=1&sdate1=2021.11.06.

    # Variables for Algorithm
    domestic_departure_airport = "GMP"
    international_departure_airport = "ICN,%20GMP"
    flight_tickets_departure = ["<가는날 항공권 입니다>"]
    flight_tickets_return = ["<오는날 항공권 입니다>"]
    ticket_prices = []

    start_day = date(start_year, start_month, start_date)
    end_day = date(end_year, end_month, end_date)
    delta = end_day - start_day

    browser = webdriver.Chrome('../chromedriver.exe')
    browser.maximize_window()

    # 왕복
    try:
        for i in range(delta.days + 1):        
                
            # Ticket_Lists = [Company, Infomation, Class, Date, Price]       
            day = start_day + timedelta(days=i)
            str_day = str(day)
            str_day.replace("-",".")
                
            str_period_date = str(day)
            str_period_date.replace("-",".")

            # Check domestic and make URL
            if check_domestic(arrival_airport) == "domestic":
                url_departure = get_domestic_ow_url(domestic_departure_airport, arrival_airport, adult_num, child_num, infant_num, str_day + ".")
                url_return = get_domestic_ow_url(arrival_airport, domestic_departure_airport, adult_num, child_num, infant_num, str_period_date + ".")
                
                # 가는날
                browser.get(url_departure)
                sort = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[3]/div[1]/a")))
                sort.click()
                price_sort = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[3]/div[1]/div/ul/li[1]")
                price_sort.click()

                soup = BeautifulSoup(browser.page_source, "html.parser")

                flight_companies = soup.find_all("span", attrs={"class":"h_tit_result ng-binding"})
                flight_infos = soup.find_all("div", attrs={"class":"route_info_box"})
                flight_seats = soup.find_all("div", attrs={"class":"txt_seat ng-binding"})
                flight_prices = soup.find_all("span", attrs={"class":"txt_pay ng-binding"})
                        
                for flight_company, flight_info, flight_seat, flight_price in zip(flight_companies, flight_infos, flight_seats, flight_prices):
                    list_for_append = []
                    list_for_append.append(flight_company.text)
                    list_for_append.append(flight_info.text)
                    list_for_append.append(flight_seat.text)
                    list_for_append.append(str(day))
                    flight_price = flight_price.text
                    flight_price = flight_price.replace(",","")
                    list_for_append.append(int(flight_price))
                    list_for_append.append(url_departure)
                    flight_tickets_departure.append(list_for_append)

                # 오는날

                browser.get(url_return)
                sort = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[3]/div[1]/a")))
                sort.click()
                price_sort = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[3]/div[1]/div/ul/li[1]")
                price_sort.click()

                soup = BeautifulSoup(browser.page_source, "lxml")

                flight_companies = soup.find_all("span", attrs={"class":"h_tit_result ng-binding"})
                flight_infos = soup.find_all("div", attrs={"class":"route_info_box"})
                flight_seats = soup.find_all("div", attrs={"class":"txt_seat ng-binding"})
                flight_prices = soup.find_all("span", attrs={"class":"txt_pay ng-binding"})
                        
                for flight_company, flight_info, flight_seat, flight_price in zip(flight_companies, flight_infos, flight_seats, flight_prices):
                    list_for_append = []
                    list_for_append.append(flight_company.text)
                    list_for_append.append(flight_info.text)
                    list_for_append.append(flight_seat.text)
                    list_for_append.append(str(day))
                    flight_price = flight_price.text
                    flight_price = flight_price.replace(",","")
                    list_for_append.append(int(flight_price))
                    list_for_append.append(url_return)
                    flight_tickets_return.append(list_for_append)
            else:
                url_departure = get_international_ow_url(international_departure_airport, arrival_airport, adult_num, child_num, infant_num, str_day + ".")
                url_return = get_international_ow_url(international_departure_airport, arrival_airport, adult_num, child_num, infant_num, str_period_date + ".")

                # 가는날
                browser.get(url_departure)
                sort = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[3]/div[1]/a")))
                sort.click()
                price_sort = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[3]/div[1]/div/ul/li[1]")
                price_sort.click()

                soup = BeautifulSoup(browser.page_source, "lxml")

                flight_companies = soup.find_all("span", attrs={"class":"h_tit_result ng-binding"})
                flight_infos = soup.find_all("div", attrs={"class":"route_info_box"})
                flight_seats = soup.find_all("a", attrs={"class":"btn_pay_terms btn_pay_terms_v2 ng-binding"})
                flight_prices = soup.find_all("span", attrs={"class":"txt_pay ng-binding"})
                        
                for flight_company, flight_info, flight_seat, flight_price in zip(flight_companies, flight_infos, flight_seats, flight_prices):
                    list_for_append = []
                    list_for_append.append(flight_company.text)
                    list_for_append.append(flight_info.text)
                    list_for_append.append(flight_seat.text)
                    list_for_append.append(str(day))
                    flight_price = flight_price.text
                    flight_price = flight_price.replace(",","")
                    list_for_append.append(int(flight_price))
                    list_for_append.append(url_departure)
                    flight_tickets_departure.append(list_for_append)

                # 오는날

                browser.get(url_return)
                sort = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[3]/div[1]/a")))
                sort.click()
                price_sort = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[3]/div[1]/div/ul/li[1]")
                price_sort.click()

                soup = BeautifulSoup(browser.page_source, "lxml")

                flight_companies = soup.find_all("span", attrs={"class":"h_tit_result ng-binding"})
                flight_infos = soup.find_all("div", attrs={"class":"route_info_box"})
                flight_seats = soup.find_all("a", attrs={"class":"btn_pay_terms btn_pay_terms_v2 ng-binding"})
                flight_prices = soup.find_all("span", attrs={"class":"txt_pay ng-binding"})
                        
                for flight_company, flight_info, flight_seat, flight_price in zip(flight_companies, flight_infos, flight_seats, flight_prices):
                    list_for_append = []
                    list_for_append.append(flight_company.text)
                    list_for_append.append(flight_info.text)
                    list_for_append.append(flight_seat.text)
                    list_for_append.append(str(day))
                    flight_price = flight_price.text
                    flight_price = flight_price.replace(",","")
                    list_for_append.append(int(flight_price))
                    list_for_append.append(url_return)
                    flight_tickets_return.append(list_for_append)    
    finally:
        
        sorted_ticket_list = []
        sorted_flight_tickets_departure = sorted(flight_tickets_departure, key=lambda ticket: ticket[4])
        sorted_ticket_list.append(sorted_flight_tickets_departure)
        sorted_flight_tickets_return = sorted(flight_tickets_return, key=lambda ticket: ticket[4])
        sorted_ticket_list.append(sorted_flight_tickets_return)
        return sorted_ticket_list
        browser.quit()

