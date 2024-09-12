import streamlit as st
from bs4 import BeautifulSoup
import datetime

st.title("Company name finder")
st.text("Find the name of the company from its BRSR XBRL")
xbrl = st.file_uploader("Choose XBRL",type="xml")
# with open(xbrl,'rb') as brsrFile:
soup = BeautifulSoup(xbrl,'xml')

compName = soup.find("NameOfTheCompany").text
currentYear = datetime.datetime.strptime(soup.find("DateOfEndOfFinancialYear").text,"%Y-%m-%d").year
prevYear = datetime.datetime.strptime(soup.find("DateOfEndOfPreviousYear").text,"%Y-%m-%d").year
prevPrevYear = datetime.datetime.strptime(soup.find("DateOfEndOfPriorToPreviousYear").text,"%Y-%m-%d").year

st.write("Name - **{}**".format(compName))
st.write("Current year - **{}**".format(currentYear))
