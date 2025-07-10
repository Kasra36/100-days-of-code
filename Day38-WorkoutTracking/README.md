🏋️ Day 38 – Workout Tracking with Nutritionix & Sheety

This project demonstrates how to build a workout tracking tool using two external APIs: **Nutritionix** and **Sheety**.


📌 What This Code Does

The app allows the user to:

1. **Enter natural language exercise input** (e.g., “I ran 3km and did 20 pushups”).
2. **Parse that input using the Nutritionix API**, which returns detailed information about each activity (like duration and calories burned).
3. **Log the workout data to a Google Sheet** using the Sheety API.

Note: All sensitive information (API keys, tokens) is stored securely using **environment variables** loaded from a `.env` file.


🧰 Modules Used

- `requests` – For making HTTP requests to Nutritionix and Sheety.
- `datetime` – For getting the current date and time.
- `os` – To load environment variables securely.
- `dotenv` – To read the `.env` file and load variables into the environment.


📸 Screenshot

![Workout Tracker Screenshot](images/screenshot.png)

