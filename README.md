# Automated Email Sender

This is a Python script that automates the process of sending personalized emails by reading recipient data from an Excel file (`.xlsx`).

The script is ideal for sending mass personalized communications, such as monthly reports, event invitations, or notifications, without manual work.

## Features

- **Reads data from Excel:** Uses the `openpyxl` library to read recipient information (names, email addresses, and subjects).
- **Personalized messages:** Automatically generates a custom email body for each recipient based on the data in the Excel file.
- **Email automation:** Connects to an SMTP server (like Gmail) to send emails securely.

## Prerequisites

- **Python 3.x**
- **A Gmail account** with **Two-Factor Authentication** enabled and an **App Password** created for the script.
- **An Excel file (`.xlsx`)** named `recipients.xlsx` with the following columns: `nombre`, `email`, and `asunto`.

## Installation

1.  Clone this repository or download the script files.
2.  Install the required Python library:

    ```bash
    pip install openpyxl
    ```

## How to use

1.  **Prepare your Excel file:** Make sure your `recipients.xlsx` file is in the same directory as the script, and that its columns are correctly named.

2.  **Configure the script:** Open the `send_reports.py` file and update the following variables with your details:

    ```python
    # Your Gmail account and App Password
    sender_email = "your_email@gmail.com"
    app_password = "your_app_password" # Use the App Password, not your regular password
    ```

3.  **Run the script:** Execute the script from your terminal.

    ```bash
    python send_reports.py
    ```

The script will read the data, create the personalized messages, and send an email to each recipient listed in the Excel file.