a=[1,2,3,4,5,6,7]
b=[x**2 for x in a] 
print(b)
b=[x**3 for x in a]
print(b)
c={x:x**2 for x in a}
print(c)
a=["aman","adarsh",1]
v=(1,2,3,4,5,"anoop")
d={"name":"adarsh","role":"python"}
f={"adarsh","django","amana"}
print(type(f))
print(type(v))
def anoop():
    def anoop2():
        print("adarsh")
    return anoop2
a=anoop()
a()  
a="anoop"
def aman():
    print(a)
aman()    
def ai():
    a="asdf"
    print(a)
ai()    
import smtplib    
# Calling SMTP    
s = smtplib.SMTP('smtp.gmail.com', 587)    
# TLS for network security    
s.starttls()    
# User email Authentication    
s.login("anoop.whiteforce@gmail.com", "anoop2000")    
# Message to be sent    
message = "Message_sender_need_to_send"    
# Sending the mail    
s.sendmail("anoop.whiteforce@gmail.com ", "anoop.whiteforce@gmail.com", message)    