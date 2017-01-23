#used Class and functions for separate functioning
#Written ouput data into an excel sheet.


#PROBLEM:
# Out of the 500 urls given, few we didn't get any response, they didn't exist.
# Hence, written them as 'No response' under E-commerce.
# For others I have written as 'True' if its an E-commerce site and False if its not.
# Based on the few key words like 'Cart' , 'buy' ,'sell, 


#REQUIREMENTS:


#python : apt-get install python -> this will install the latest python version
#urllib2 : apt-get install python-urllib2 -> this module is used to get response from the site.
#xlwt : pip install xlwt -> this module is used for creating an excel sheet.


#CODING PART:
# Written separate functions in one class.
# used get_filenames function to get the output file.
# used program_headers function to print the headers in the excel file.
# main function where we are taking all the 500 links from the websites.txt file and passing it through urllib module for getting the response. If its ecommerce site, Am writing as 'True' into the sheet else 'False'
# We are not getting response from few sites as those are not existed when opened through browser and checked. Am writing 'No response' for such links.
# Am distinguishing a site whether it's an Ecommerce site or not , as considering few keywords such as: 'Cart', 'buy' , 'selling','shopping' words as these words will be mostly present in an E-commerce websites.
# Writing all these into an excel sheet as we can get the data in a tabular form.

#RUN COMMAND:
#python websites_scrape_into_file.py


