import get_conn
import Tracker
import time, os
import mail_sender


conn = get_conn.connect()
query = 'SELECT * FROM tracking'


if not os.path.exists("./config"):
    raise NotADirectoryError("""
    
    Please provide your Credentials i.e Email & Passwrod before
    starting tracking:
    --
    • Run setup.py
    --
    Then you are good to go.
    """)

print("[STARTED TRACKING]")


while True:
    results = conn.execute(query).fetchall()
    for row in results:
        ID = row[0]
        title = row[1]
        last_price = int(row[2])
        url = row[3]
        
        curr_price = Tracker.checkfor_this(url).last_price
        print(f"Last price: {last_price} | Curr price: {curr_price}")
        if last_price > curr_price:
            mail_sender.send_email(title, url, last_price, curr_price)
            conn.execute(f'DELETE FROM tracking WHERE ID = {ID}')
            conn.commit()
            print("Product List updated")
    time.sleep(10)

