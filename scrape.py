# Import Research Expression
import re
import numpy as np
# Import Email Validator
import validate_email

# Import Data text file
t =  open("Data.txt",'r',encoding = 'latin1')
data = t.read()
content = data.lower()

# Extracting emails from given text in content var
#result = re.findall("([\w.-]+@[\w.-]+)", content) '''Lots of errors in it'''
result = re.findall("[\w\.,]+@[\w\.,]+\.\w+", content)

print(type(result),len(result))

# Removing Duplicate Emails
# Initialising the Variables Needed
email_list = result
final_list = []

# Creating a loop to check duplicates
for x in email_list:
    if x not in final_list:
        final_list.append(x)
        
print(type(final_list),len(result))
print("Total Duplicates: ",len(result)-len(final_list))

#print(*final_list, sep= "\n")

# Validate the Scraped Email Ids
for x in final_list:
    validate_email.validate(x)
    
validate_email.display()
validate_email.write_valid_emails()
validate_email.write_invalid_emails()