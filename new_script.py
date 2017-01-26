import urllib2
with open('/home/interns/kaivalya/GenFramework/juicer/spiders/whatever.txt', 'w') as file:
    file.write('-------------------------------------------------------------------------------------------------------')
    file.write('\n|\t\t\t\t\tWEBSITE\t\t\t\t\t|\t\t\t\t\tE-COMMERCE\t\t\t\t\t|')
    input_file = open('websites.txt', 'r').readlines()
    for line in input_file:
        line = line.strip('+').strip('\n')
        if 'http:' not in line:
            line = 'http://' + line

        try:
            connection = urllib2.urlopen(line)
            get_responsedata = connection.read()
            ecommerce_value =''
            if 'cart ' in get_responsedata or 'buy' in get_responsedata or 'sell' in get_responsedata or 'shopping' in get_responsedata:
                ecommerce_value = 'True'
            else:
                ecommerce_value = 'False'
            connection.close()
        except:
             ecommerce_value= 'No Response' 
        file.write('\n|\t\t\t\t%s\t\t\t\t|\t\t\t\t\t%s\t\t\t\t\t|'%(line,ecommerce_value))
    file.write('\n----------------------------------------------------------------------------------------------------')
