CONSTRAINTS:
-----------

- Os - Ubuntu 
- used python 2.7.12 
- used urllib module
- instructions of set up:
	- python : apt-get install python
	- urllib2 : apt-get install python-urllib2
	- xlwt : pip install xlwt -> this module is used for creating an excel sheet [Not Mandatory]
- Program will run in the latest linux machines.



DESCRIPTION OF HOW I APPROACHED THE PROBLEM:
-------------------------------------------

- Given 500 urls to check whether they are ecommerce sites or not.
- We can decide whether a particular site is ecommerce or not, by searching for the common words usually present in e-commerce sites such as CART, BUY , SELL , SHOPPING etc.
- Hence, parsing the urls given and checking whether those words present in that page.
- If present , printing as True, else printing as False.

- We can use few methods for parsing:
	- beautiful soup
	- urllib2
	- scrapy 

- No limitations in the solution. We can use many parsing modules like urllib2, beautiful soup, scrapy, wget etc.

- Used urllib2, I can  write in beautiful soup,scrapy etc as well. But using scrapy the disadvantage is we can't able to parse the link whichdoesn't exist. Few links of the 500 urls are invalid links which doesn't exist. As we need to write all 500 urls along with True or False, its not preffered.Hence used urllib2 module to parse and writing into file.

-Out of the 500 urls given, few we didn't get any response, they didn't exist. Hence, written them as 'No response' under E-commerce.

- As told to write into a file, we can write into sheet or a normal file. I have done 2 methods and attaching both scripts and output files.
- I have did all possible ways. Writing into a sheet and writing into a file. 

- Distinguishing whether a site as e-commerce or not is calculated using few common words. As we can't distinguish by any other parameters.
Guess no improvements required.  


CODING PART:

First method: Writing into an excel file:
-----------------------------------------
	Written separate functions in one class.
	used get_filenames function to get the output file.
	used program_headers function to print the headers in the excel file.

	main function where we are taking all the 500 links from the websites.txt file and passing it through urllib module for getting the response. If its ecommerce site, Am writing as 'True' into the sheet else 'False'

Second method:
--------------
	Writing into a normal txt file in a tabular form
	

We are not getting response from few sites as those are not existed when opened through browser and checked. Am writing 'No response' for such links.

Am distinguishing a site whether it's an Ecommerce site or not , as considering few keywords such as: 'Cart', 'buy' , 'selling','shopping' words as these words will be mostly present in an E-commerce websites.

first method: [writing into an excel sheet]: Writing all these into an excel sheet as we can get the data in a tabular form.
	script: websites_scrape_into_file.py 
	output file: scraped_data_programs.xls

second method:[Writing into another text file]: Writing into a txt file in a tabular form.
	script: new_script.py
	output file: second_output.txt
	

RUN COMMAND:

first method file[ Writing into an excel sheet]: python websites_scrape_into_file.py
second method file[Writing into another text file]: python new_script.py
