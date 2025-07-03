import qrcode

bkash_id =input("Enter your bKash ID: ")
amount=input("Enter your amount: ")
reference =input("Enter your reference no: ")

bkash_pay_url = f"https://www.bkash.com/merchantpay?merchant={bkash_id}&amount={amount}&reference={reference}"


bkash_qr = qrcode.make(bkash_pay_url)
bkash_qr.save("bkash_qr.png")
bkash_qr.show()