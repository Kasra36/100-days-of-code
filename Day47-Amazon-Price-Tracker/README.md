🛒 Day 47 – Amazon Price Tracker

This project is a simple Amazon Price Tracker built using BeautifulSoup and Requests.

📌 What This Code Does

- Fetches the product title and current price from a specific Amazon product page.
- Compares the current price with a predefined target price.
- Sends an email notification via Gmail SMTP if the price drops below the target.

🧰 Modules Used

* requests – For making HTTP requests to the product page.
* bs4 (BeautifulSoup) – For parsing the HTML and extracting product info.
* smtplib – To send the email alert.
* os – To access environment variables.
* dotenv – To load variables from the .env file.
