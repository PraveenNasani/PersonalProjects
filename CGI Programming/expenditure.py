#!C:\Users\admin\AppData\Local\Programs\Python\Python38-32\python.exe
import cgi
import csv
import smtplib
send_mail=smtplib.SMTP('smtp.gmail.com',587)
from_add='nasanipraveenkumar@gmail.com'
password=''
form = cgi.FieldStorage()
# Get data from fields
print("Content-type:text/html\r\n\r\n")
print('<html>')
name = form.getvalue('name')
email = form.getvalue('email')
amount = form.getvalue('amount')
reason = form.getvalue('reason')
a=[name,email,amount,(reason,amount)]
newlist=[]
limit=5000

with open(r'C:\Users\admin\Desktop\example.csv','r') as example1:
    reader=csv.reader(example1)
    for i in reader:
        newlist.append(i)
#print(newlist)
for i in newlist:
    if i[1] == a[1]:
        i[3]=i[3]+str(a[3])
        i[2]=int(i[2])+int(a[2])
        #print('Total amount spent : {i[2]}')
        #print('<html>')
       # print('<body>')
        print('<h2>Hello %s,You are an existing user</h2>'%a[0])
        if i[2]<limit:
            print('<h2>Till now you have spent Rs%s and you can spend upto %s</h2>'%(i[2],limit-int(i[2])))
        else:
            msg='Your monthly expenditure has crossed limit(5000)'+'Your total expenditure is %s for these particuars'%i[2]+i[3]
            print('<h2>Your Monthly expenditure limit has crossed,Please check your mail for particulars </h2>')
            send_mail.starttls()
            send_mail.login(from_add,password)
            #print('Login Successful')
            send_mail.sendmail(from_add,email,msg)

       #print('</body>')
       # print('</html>')
        break
else:
    newlist.append(a)
    print('<h2>Hello %s,Welcome to my app </h2>'%a[0])
    print('<h2>You are a new user,keep using our App</h2>')
    print('<h2>Your monthly expenditure limit is Rs 5000</h2>')
    if limit-int(a[2])<0:
        print('<h2>Your Monthly expenditure limit has crossed,Please check your mail for particulars </h2>')
    else:
        print('<h2>Till now you have spent Rs%s and you can spend upto %s </h2>'%(a[2],limit-int(a[2])))
    #print('Hello %s,Welcome to my app'%(name))

print('</html>')    
with open(r'C:\Users\admin\Desktop\example.csv','w',newline='') as example:
    writer=csv.writer(example)
    for i in newlist:
        writer.writerows([i])



