# Automated Login Script

This Python script automates the login process for a website using Selenium WebDriver with Chrome in headless mode. The script reads credentials and URLs from environment variables and schedules the login process to run every 24 hours.

## Features

- **Headless Browser**: Runs Chrome in headless mode suitable for server environments.
- **Environment Variables**: Stores sensitive data (URLs, credentials) in a `.env` file.
- **Scheduled Execution**: Uses the `schedule` library to run the login task every 24 hours.
- **Logging**: Logs important actions and errors to a file.

## Prerequisites

- Python `3.10`
- Python libraries in `requirements.txt`
- Chrome browser version `126.0.6478.182`
- ChromeDriver version `126.0.6478.182`


## Installation

### Docker

#### Clone the Repository

   ```sh
   git clone https://github.com/kup1o/auto_login.git && cd $_
   ```

#### Set Up Environment

Rename the .env_example file to .env and update it with your credentials and URLs:

```sh
cp .env_example .env
```

Edit the .env file with your details:

```env
LOGIN_URL=https://example.com/login
USERNAME=your_email@example.com
PASSWORD=your_password
SUCCESS_URL=https://example.com/success
```

#### Build Docker image and run container detached

```sh
docker compose up --build -d
```

### Manual

> [!WARNING]
> It's better to use Docker instead of manual installation, because Docker handles all required dependencies.

#### Clone the Repository

   ```sh
   git clone https://github.com/kup1o/auto_login.git && cd $_
   ```

#### Set Up Environment

Rename the .env_example file to .env and update it with your credentials and URLs:

```sh
cp .env_example .env
```

Edit the .env file with your details:

```env
LOGIN_URL=https://example.com/login
USERNAME=your_email@example.com
PASSWORD=your_password
SUCCESS_URL=https://example.com/success
```

#### Install Dependencies

Ensure you have Chrome and ChromeDriver installed.

```
# Install Google Chrome (version 126.0.6478.182)
sudo apt update
sudo apt install -y wget
wget https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_126.0.6478.182-1_amd64.deb
sudo dpkg -i google-chrome-stable_126.0.6478.182-1_amd64.deb
sudo apt install -f
sudo apt-mark hold google-chrome-stable

# Install ChromeDriver (version 126.0.6478.182)
wget https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.182/linux64/chromedriver-linux64.zip
unzip chromedriver-linux64.zip
sudo mv chromedriver-linux64/chromedriver /usr/local/bin/chromedriver
rm -r chromedriver-linux64
```

Install Python libraries using pip:

```sh
pip install -r requirements.txt
```

If you run script in a headless environment, e.g. server, then consider installing Xvfb:

```sh
sudo apt install xvfb
```

After Xvfb installation, you should run it in the background:

```sh
Xvfb :99 -screen 0 1280x800x24 &
```

> [!TIP]
> You can change the resolution to your desired one.

## Usage

Run the script using Python:

```sh
python main.py
```

The script will immediately perform the login and then schedule itself to run every 24 hours.

https://github.com/user-attachments/assets/19158eff-37b6-4185-8ffb-a4119e4658d4

## Debug

Logs: Check the `logs/login_script.log` file for detailed logs and any potential issues.

Headless Mode: If you need to see the browser window, you can disable headless mode by commenting out the `--headless` argument in the Options setup.

Debug Script: For more detailed debugging, you can use the `debug.py` script provided in this repository. This script is configured to run in a non-headless mode and includes additional logging to help troubleshoot any issues. To run the debug script, use:

```
python debug.py
```

## Contributing
Feel free to open issues or submit pull requests if you have suggestions or improvements.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any questions, please contact kup1o@pm.me
