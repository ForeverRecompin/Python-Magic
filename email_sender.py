import smtplib #smtplib : Simple mail transfer protocol library.

def email_sender():
    '''
    Sends an email from person A to person B.
    Of course, person A and B need to be real.
    Their email addresses have to be real, even if they're not real...
    
    We need A's password and A's email's SMTP domain name.This script works out of the box for gmail, hotmail, outlook and yahoo.
    If, however, A's email address is a@pinkunicorn.com or something cool
    like that, the script would ask for pinkunicorn.com's SMTP domain name.
    '''
    
    sender_email, sender_password = list(input("Enter Sender's email address followed by password.\nEg. pat@gmail.com ilovecats: ").split())
    reciever_email = input("Enter reciever's email address: ")
    subject = input("Enter email-subject: ")
    body = input("Enter email-body: ")
    sender_domain = sender_email[sender_email.find('@')+1:sender_email.find('.com')]
    smpt_domain = {'gmail': 'smtp.gmail.com',
                               'outlook': 'smtp-mail.outlook.com',
                               'hotmail': 'smtp-mail.outlook.com',
                               'yahoo': 'smtp.mail.yahoo.com'}
    if sender_domain in smpt_domain:
        sender_smpt_domain = smpt_domain[sender_domain]
    else:
         sender_smpt_domain = input("Enter sender email's smpt domain name: ")    

    try:
        smtp_instance = smtplib.SMTP(sender_smpt_domain, 587)
        smtp_instance.ehlo()
        smtp_instance.starttls()
        smtp_instance.login(sender_email, sender_password)
        smtp_instance.sendmail(sender_email, reciever_email, 'Subject:' + subject + '\n' + body)
        smtp_instance.quit()
        print("Email sent successfully! :D")
    except SMTPException:
        print("Something went wrong! :(")
    
if __name__ == "__main__":
    email_sender()
