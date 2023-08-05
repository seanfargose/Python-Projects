import smtplib

my_email = "fargosesean@gmail.com"
password = "sean@925"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="fargose.sean2808@gmail.com",
        msg="Subject:Hello\n\nThis is the body of the email"
    )
    