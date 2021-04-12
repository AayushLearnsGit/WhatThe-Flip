import pickle, smtplib, time

print("Hello!")
print("Please provide the required credentials i.e. email-id and password to get the setup done.")
print("\nNOTE:\n=====")
print("""\
I know you may worry on giving the sensitive things like email-password.
Be assured (and even check the source code, that I am not keeping track
of any kind of information. It is completely on your local machine.
--
To make things run smoothly we will need...
• Your Email and Password (from which the emails will be sent)
• Target Email (where the notifications will come)

[Both email can be the same]""")

while True:
    my_email = input("Your-Email: ")
    my_pass = input("Your-Password: ")

    print("[CHECKING CREDENTIALS]")
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        try:
            smtp.login(my_email, my_pass)
        except:
            print("""Email & Password were not matched...
            If you have double checked both of them...
            ---
            Please check that you have an Email from Gmail and 'LESS SECURE APPS' is turned on.
            Try again...
            """)
            input("[Press any key]")
            continue
    print("[SUCCESS]")
    print("\n")
    
    target_email = input("Target Email: ")
    print("[Saving]")
    time.sleep(3)
    print("[DONE]")

    print("""
    Next steps:
    -----------
    
    There are two files to manage.
     1. Tracking_Products.py - To add / delete products
     2. Track_them.py        - To keep an eye on tracking list (it will run forever till you hit ctrl+C)

     Enjoy!
    """)
    break


with open("config", "wb") as f:
    pickle.dump({"email":my_email, "password":my_pass, "target": target_email}, f)