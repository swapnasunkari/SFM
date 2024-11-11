from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import donation,register
import os
import mysql.connector
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib 
from datetime import datetime
from django.contrib import messages 
import random

def projectindex(request):
      return render(request,'projectindex.html')

def projectlogin(request):
    return render(request,'projectlogin.html')

def projectreg(request):
    return render(request,'projectreg.html')

def projectabout(request):
    return render(request,'projectabout.html')
def index(request):
     return render(request,'index.html')
def projectdonar(request):
     return render(request, 'projectdonar.html')
def adminlogin(request):
    return render(request,'adminlogin.html')
def adminlogin(request):
    return render(request,'adminlogin.html')
def adminregedit(request):
    return render(request,'adminregedit.html')
def donations(request):
    return render(request,'donations.html')
def admindashboard(request):
    return render(request,'admindashboard.html')
def projectnewdonation(request):
    return render(request,'projectnewdonation.html')
def projectdonation(request):
    return render(request,'projectdonation.html')
def donations(request):
    return render(request,'donations.html')
def projectedit(request):
    return render(request,'projectedit.html')
def adminreg(request):
    return render(request,'adminreg.html')
def deleteproduct(request):
    return render(request,'deleteproduct.html')
def header(request):
    return render(request,'header.html')
def design(request):
    return render(request,'design.html')


def projectdonar(request):
    print('in donor')
    if(request.method=="POST"):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="donordatabase"
        )
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        foodType=request.POST['foodType']
        quantity=request.POST['quantity']
        uploadtime=request.POST['uploadtime']
        address=request.POST['address']
        mycursor = conn.cursor()
        print("insert into donorform(name,phone,email,foodType,quantity,uploadtime,address) values('"+name+"','"+phone+"','"+email+"','"+foodType+"','"+quantity+"','"+uploadtime+"','"+address+"')")
        mycursor.execute("insert into donorform(name,phone,email,foodType,quantity,uploadtime,address) values('"+name+"','"+phone+"','"+email+"','"+foodType+"','"+quantity+"','"+uploadtime+"','"+address+"')")
        conn.commit()    
        return render(request,'index.html')
    else:
        return render(request,'projectdonar.html')


def adminlogin(request):
    print('in adminlogin')
    if(request.method=="POST"):
        conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="donordatabase"
        )
        le=request.POST['le']
        lp=request.POST['lp']
        mycursor=conn.cursor()
        mycursor.execute("insert into adminlogin(le,lp)values('"+le+"','"+lp+"')")
        conn.commit()
        return render(request,'projectindex.html')
    else:
        return render(request,'adminlogin.html')
    
def projectlogin(request):
        print('in projectlogin')
        if(request.method=="POST"):
             conn=mysql.connector.connect(
                  host="localhost",
                  user="root",
                  password="",
                  database="donordatabase"
             )
             em=request.POST['em']
             pwd=request.POST['pwd']
             mycursor=conn.cursor()
             mycursor.execute("select * from registers where email='"+em+"' and password='"+pwd+"'and isactive=1")
             result=mycursor.fetchone()
             if(result!=None):
                request.session['em']=em
                return redirect('donations')
             else:
                return render(request,"projectlogin.html",{"status":"invalid credentials"})
        else:
            return render(request,"projectlogin.html",{"status":"invalid credentials"})

'''return render(request,'donations.html')
        else:
             return render(request,'projectlogin.html')'''

def handle_uploaded_file(uploaded_file):
    # Define the directory where you want to save the uploaded files
    upload_dir = 'media'
    
    # Create the upload directory if it doesn't exist
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    
    # Generate a unique file name (you can modify this as needed)
    file_name = os.path.join(upload_dir, uploaded_file.name)
    
    # Open the destination file and save the uploaded file data into it
    with open(file_name, 'wb+') as destination:
        for chunk in uploaded_file.chunks():
            destination.write(chunk)
    
    # Return the path to the saved file
    return file_name

def projectreg(request):
        print('in project reg')
        if(request.method=="POST"):        
            uploaded_file = request.FILES['myfile']
            saved_file_path = handle_uploaded_file(uploaded_file)
            s=saved_file_path.split("\\")
            print(s[1])
         
            conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="donordatabase"
            )
            print('in project reg1')
            if('myfile'  in request.FILES):
                uploaded_file = request.FILES['myfile']
                saved_file_path = handle_uploaded_file(uploaded_file)
            else:
                uploaded_file = 'no file'
                saved_file_path = "no file"
            print('in project reg2')
            
            orgname=request.POST['org']
            phnnum=request.POST['phnnum']
            hno=request.POST['hno']
            locality=request.POST['loc']
            district=request.POST['dist']
            state=request.POST['st']
            email=request.POST['em']
            password=request.POST['pwd']
            document=saved_file_path
            mycursor=conn.cursor()
            print('in project reg2')
            s=saved_file_path.split("\\")[1]
            print("insert into register(orgname,phnnum,hno,locality,district,state,email,password,uploadedfile) values('"+orgname+"','"+phnnum+"','"+hno+"','"+locality+"','"+district+"','"+state+"','"+email+"','"+password+"','"+s+"')")
            mycursor.execute("insert into registers(orgname,phnnum,hno,locality,district,state,email,password,uploadedfile) values('"+orgname+"','"+phnnum+"','"+hno+"','"+locality+"','"+district+"','"+state+"','"+email+"','"+password+"','"+s+"')")
            conn.commit()
            return render(request,'projectlogin.html')
        else:
            return render(request,'projectreg.html')
        

def projectdonation(request):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="donordatabase"        
        )
    mycursor = conn.cursor()
    mycursor.execute("select * from donorform")
    result=mycursor.fetchall()
    donations=[]
    
    if(result!=None):
        for x in result:
            d=donation()
            d.sid=x[0]
            d.name=x[1]
            d.phone=x[2]
            d.email=x[3]
            d.foodType=x[4]
            d.quantity=x[5]
            d.uploadtime=x[6]
            d.address=x[7]
            donations.append(d)
        return render(request,'projectdonation.html',{"donations":donations})
    else:
        return render(request,'projectdonation.html')
def projectedit(request,sid):
    if(request.method=="POST"):
        print('in post')
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        foodType=request.POST['foodType']
        quantity=request.POST['quantity']
        uploadtime=request.POST['uploadtime']
        address=request.POST['address']
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="donordatabase"        
            )
        mycursor = conn.cursor()
        print("update donorform SET name='"+name+"',phone="+phone+",email="+email+",foodType="+foodType+",quantity="+quantity+",uploadtime="+uploadtime+",address="+address+" where sid="+sid)
        mycursor.execute("update donorform SET name='"+name+"',phone="+phone+",email='"+email+"',foodType='"+foodType+"',quantity="+quantity+",uploadtime='"+uploadtime+"',address='"+address+"' where sid="+sid)
        conn.commit()
        return redirect('projectdonation')
    
    else:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="donordatabase"        
            )
        mycursor = conn.cursor()
        mycursor.execute("select * from donorform where sid="+sid)
        result=mycursor.fetchone()
        d=donation()
        if(result!=None):
            d.sid=result[0]
            d.name=result[1]
            d.phone=result[2]
            d.email=result[3]
            d.foodType=result[4]
            d.quantity=result[5]
            d.uploadtime=result[6]
            d.address=result[7]
        return render(request,'projectedit.html',{"d":d})
        
def deletedonation(request,sid):    
    print('in delete')
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="donordatabase"        
        )
    mycursor = conn.cursor()
    mycursor.execute("delete from donorform where sid="+sid)
    conn.commit()
    return redirect('projectdonation')



def donations(request):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="donordatabase"        
        )
    mycursor = conn.cursor()
    mycursor.execute("select * from donorform")
    result=mycursor.fetchall()
    donations=[]
    
    if(result!=None):
        print(result)
        return render(request,'donations.html',{"donations":result})
    else:
        return render(request,'projectdonation.html')

    
def projectnewdonation(request):  
    if(request.method=="POST"):
        print('in post')
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        foodType=request.POST['foodType']
        quantity=request.POST['quantity']
        uploadtime=request.POST['uploadtime']
        address=request.POST['address']
        conn = mysql.connector.connect(
            host="localhost",
            user="root",    
            password="",
            database="donordatabase"        
            )
        mycursor = conn.cursor()
        mycursor.execute( "insert into donorform(name,phone,email,foodType,quantity,uploadtime,address) values('"+name+"','"+phone+"','"+email+"','"+foodType+"','"+quantity+"','"+uploadtime+"','"+address+"')")
        conn.commit()
        return redirect('projectdonation')
    
    else:
        return render(request,'projectnewdonation.html')
    
def adminlogin(request):
        print('in adminlogin')
        if(request.method=="POST"):
             conn=mysql.connector.connect(
                  host="localhost",
                  user="root",
                  password="",
                  database="donordatabase"
             )
             email=request.POST['email']
             password=request.POST['password']
             mycursor=conn.cursor()
             mycursor.execute("select * from adminlogin where email='"+email+"' and password='"+password+"'")
             result=mycursor.fetchone()
             if(result!=None):
                request.session['email']=email
                return redirect('admindashboard')
             else:
                print('invalid credentials')
                return render(request,"adminlogin.html",{"status":"invalid credentials"})
        else:
            return render(request,"adminlogin.html",{"status":"invalid credentials"})
        

        
def adminreg(request):
    conn = mysql.connector.connect(
    
        host="localhost",
        user="root",
        password="",
        database="donordatabase"        
        )
    mycursor = conn.cursor()
    mycursor.execute("select * from registers")
    result=mycursor.fetchall()
    registers=[]    
    if(result!=None):
        return render(request,'adminreg.html',{"registers":result})
    else:
        return render(request,'adminreg.html')
        
def adminregedit(request,sid):
        print('in post')
        if(request.method=="POST"):        
            uploaded_file = request.FILES['myfile']
            saved_file_path = handle_uploaded_file(uploaded_file)
            s=[]
            print('in project reg1')
            if('myfile'  in request.FILES):
                uploaded_file = request.FILES['myfile']
                saved_file_path = handle_uploaded_file(uploaded_file)
                s=saved_file_path.split("\\")
                print(s[1])
            else:
                uploaded_file = 'no file'
                saved_file_path = "no file"
            
            print('in project reg2')
            orgname=request.POST['org']
            phnnum=request.POST['phone']
            hno=request.POST['hno']
            locality=request.POST['loc']
            district=request.POST['dist']
            state=request.POST['st']
            email=request.POST['em']
            password=request.POST['pwd']
            
            document=saved_file_path
            conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="donordatabase"        
            )
 
            mycursor = conn.cursor()
            mycursor.execute("update registers SET uploadedfile='"+s[1]+"',orgname='"+orgname+"',phnnum='"+str(phnnum)+"',hno='"+hno+"',locality='"+locality+"',district='"+district+"',state='"+state+"',email='"+email+"',password='"+password+"'  where sid="+sid)
            conn.commit()
            return redirect('adminreg')
        else:
            conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="donordatabase"        
            )
        mycursor = conn.cursor()
        mycursor.execute("select * from registers where sid='"+str(sid)+"'")
        result=mycursor.fetchone()
        r=register()
        if(result!=None):
            r.sid=result[0]
            r.orgname=result[1]
            r.phnnum=result[2]
            r.hno=result[3]
            r.locality=result[4]
            r.district=result[5]
            r.state=result[6]
            r.email=result[7]
            r.password=result[8]
            r.uploadedfile=result[9]            
        return render(request,'adminregedit.html',{"r":r})
        
def adminregdelete(request,sid):    
    print('in delete')
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="donordatabase"        
        )
    mycursor = conn.cursor()
    mycursor.execute("delete from registers where sid="+sid)
    conn.commit()
    return redirect('adminreg')

def forget(request):
    return render(request,'forget.html')

def adminactive(request,sid):
    print('in active')
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="donordatabase"        
        )
    mycursor = conn.cursor()
    mycursor.execute("update registers set isactive=1 WHERE sid='"+str(sid)+"'")
    conn.commit()
    return redirect('adminreg')


def adminactive(request,sid):
    print('in active')
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="donordatabase"        
        )
    mycursor = conn.cursor()
    mycursor.execute("update registers set isactive=1 WHERE sid='"+str(sid)+"'")
    conn.commit()
    return redirect('adminreg')

def forgotpassword(request):
    if request.method == 'POST':
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="donordatabase"
        )
        mycursor = conn.cursor()
        # retrieve post details
        email = request.POST['email']
        mycursor.execute("SELECT password FROM registers WHERE email='" + email + "'")
        result = mycursor.fetchone()
        pwd = str(result[0])
        if result is not None:
            # SMTP server configuration
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587
            smtp_username = 'mohammadabdulbasith123@gmail.com'
            # For App Password, enable 2-step verification, then create an app password
            smtp_password = 'fkvheyrqbxahctoe'
            # Email content
            subject = 'Password recovery'
            body = 'This is a Password recovery email sent from Surplus Food Management. ' \
                   'Your password as per registration is: ' + pwd
            sender_email = 'mohammadabdulbasith123@gmail.com'
            receiver_email = email
            # Create a message
            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = receiver_email
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))
            # Connect to SMTP server and send the email
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.sendmail(sender_email, receiver_email, message.as_string())
            message = "Password sent to the given email ID"
            return render(request, 'projectlogin.html',{'alert_message': message})
        else:
            message = "Please enter the correct email ID"
            return render(request, 'forgotpassword.html', {'alert_message': message})
    else:
        return render(request, 'forgotpassword.html')
    


def donordetails(request):   
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="donordatabase"
    )
    mycursor = conn.cursor()
    mycursor.execute("SELECT sid,name,foodType,quantity FROM donorform")
    result = mycursor.fetchall()
    print('hi')
    if result:
        print(result)
        return render(request, 'donordetails.html', {'projectdonor': result})            
    else:           
        return render(request, 'donordetails.html')
            
def logout(request):
    try:
        if ('email' in request.session):
             del request.session["email"]
    except KeyError:
        pass
    return render(request,'adminlogin.html')


def admindashboard(request):
     if ('email' not in request.session):
        return redirect('adminlogin') 
     return render(request,"admindashboard.html")

'''def outofpage(request):
    try:
        if('email' in request.session):
            del request.session["email"]
    except KeyError:
        pass
    return render(request,'projectlogin.html')

def donations(request):
    if('email' not in request.session):
        return redirect('projectlogin')
    return render(request,'donations.html')'''


def orphanrequest(request,donorid):
     # SMTP server configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'mohammadabdulbasith123@gmail.com'
    # For App Password, enable 2-step verification, then create an app password
    smtp_password = 'fkvheyrqbxahctoe'
    # Email contentytf
    subject = 'Donation Request'
    body = 'Dear Sir, We request to deliver the donation of the donar id ' \
            'Donar Id  : ' + str(donorid)
    sender_email = 'mohammadabdulbasith123@gmail.com'
    receiver_email = "sumathikannri2003@gmail.com"
    # Create a message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = "sumathikannuri2003@gmail.com"
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    # Connect to SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print('mail sent')
    return redirect('donations')
