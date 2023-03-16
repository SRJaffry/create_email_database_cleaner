import re
fhandle = open('mbox-short.txt')

email_list = list()
for line in fhandle:

    line.rsplit()
    line_str = line.split()
    for s in line_str:
        
        # Checking if the String has '@' which is necessary for string
        if '@' in s:
            loc_at = s.find('@')
            
            #checking if the domain name is present in the string
            dot_loc = s.find('.', loc_at)
            if dot_loc>0:
                # remove some special characters like '<', '>', ';'
                cleanString = re.sub('[<, >,;]','', s)                    
                email_list.append(cleanString)
            else:
                print(s)

# Writing the email addresses to the file now
f = open('email_DB.txt', 'w')
for email in email_list:
    f.write(email + '\n')
f.close()