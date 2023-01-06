import yagmail 

password = ""
with open("/home/pi/.local/share/.email_password", "r") as f:
    password = f.read()

yag = yagmail.SMTP('aslater.raspi@gmail.com', password)

yag.send(to="annakate.slater@gmail.com",
        subject="pi connection",
        contents="hello from the pi!",
        attachments="/home/pi/file_to_join.txt")
print("sent the email!")

