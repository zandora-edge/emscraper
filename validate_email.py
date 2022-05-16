import re

regex = '^[a-z 0-9]+[\._]?[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,}$'

#r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,3})+'
 
valid_emails=[]
invalid_emails=[]
 
# Validate Emails
def validate(email):
    if (re.fullmatch(regex, email)):
        valid_emails.append(email)
    else:
        invalid_emails.append(email)
        
# Print Valid and Invalid Emails
def display():
    print('\n',"VALID EMAILS",'\n')
    print(type(valid_emails),len(valid_emails),'\n')
    print(*valid_emails, sep="\n")
    print('\n',"INVALID EMAILS",'\n')
    print(type(invalid_emails),len(invalid_emails),'\n')
    print(*invalid_emails, sep="\n")
    
# Write Valid Emails to txt File
def write_valid_emails():
     with open("Valid_Emails.txt", 'w') as output:
        for x in valid_emails:
            output.write(str(x) + '\n')
                
# Write Invalid Emails to txt File
def write_invalid_emails():
    with open("Invalid_Emails.txt", 'w') as output:
        for x in invalid_emails:
            output.write(str(x) + '\n')

        
