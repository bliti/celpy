import xlsxwriter


#dummy data
data = {
    "one": "One",
    "two": "Two",
    "three": "Three"
}


#columns keys
columns_keys = ('A','B','C')

#get the amount of keys 
#to map them to the header cells



#setup the file
workbook = xlsxwriter.Workbook('data.xls')
worksheet = workbook.add_worksheet()


for key, value in data.iteritems():
    #horribly wrong
    worksheet.write('{column}1'.format(column=columns_keys[len(data)-1]), value)

workbook.close()



#the only hard thing to do here is to match the amount of keys in the
#data dictionary to the amount of of rows we need to use.
#not really a hard issue itself :)



#plan

#break building the column names into functions
#those functions should return ready to use data structures
#loop over data structures when writing doc.