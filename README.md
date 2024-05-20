# AppCatcher - Discovering SAAS Applications By Monitoring Email Metadata

## Introduction
AppCatcher is a tool that helps you discover and inventory the SaaS applications used within your organization. It intelligently analyzes Gmail email metadata using an LLM (GPT-4o), determining if an email represents a tool used by your team or a marketing email, and then enriches the data using the Clearbit API. 

```AppCatcher does not access the content of your emails, only the metadata.```

Every SAAS app discovered is sent to the URL webhook configured that can be integrated with other security systems such as SOAR, SIEM applications etc. or other security pipelines.

## How it Works

1. **Gmail Metadata Acquisition:** AppCatcher leverages the Gmail API to retrieve email metadata, including sender, recipient, subject, and timestamps. 
2. **AI-Powered Analysis:** OpenAI's GPT-4o model analyzes the email metadata, categorizing emails as potential SaaS tool usage or marketing/non-tool related emails.
3. **Company Enrichment:** If an email is identified as potential tool usage, Clearbit's API is used to gather detailed company information about the sender, including company name, logo, domain, and description.
4. **Webhook Integration:** The combined analysis from OpenAI and Clearbit is sent to a user-defined webhook URL. This allows for seamless integration with other systems or custom analysis pipelines.

## Features

* **Privacy-Focused:** Analyzes email metadata only, ensuring the confidentiality of email content.
* **Automated SaaS Discovery:**  Identifies SaaS applications used within your organization without manual effort.
* **AI-Driven Classification:**  Leverages GPT-4's advanced language processing to accurately categorize emails.
* **Comprehensive Company Information:**  Integrates with Clearbit to provide detailed information about identified SaaS providers.
* **Flexible Webhook Integration:** Send the analyzed data to any webhook URL for further processing or visualization.
* **Cron Job Integration:** The `entrypoint.py` script can be scheduled as a cron job to continuously monitor your Gmail inbox for new SaaS application usage.
* **Centralized Configuration:** All API keys, the webhook URL, and other settings are managed through a `config.json` file.

## Getting Started

### Prerequisites

* Python 3.7+
* OpenAI API Key
* Clearbit API Key
* Gmail API Credentials (see instructions below)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AashiqRamachandran/app-catcher
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Gmail API Credentials:**
    * Follow the instructions in the [Gmail API Quickstart](https://developers.google.com/gmail/api/quickstart/python) to create a project, enable the Gmail API, and download the credentials file (`credentials.json`). This should be a service account and a credentials file.

4. **Configure `config.json`:**
    * Create a file named `config.json` in the project directory.
    * Add the following information to the file, replacing the placeholders with your actual values:
    ```json
    {
      "openai_api_key": "YOUR_OPENAI_API_KEY",
      "clearbit_api_key": "YOUR_CLEARBIT_API_KEY",
      "webhook_url": "YOUR_WEBHOOK_URL",
      "webhook_method": "Webhook Method (GET/ POST/ PUT/ PATCH)",
      "webhook_headers": "Webhook Headers (JSON)",
      "gmail_credentials_file": "credentials.json file path of gmail service account",
      "lookback_time": "Number of hours to look back for new emails"
    }
    ```

### Usage

1.  **Run the script:**
    ```bash
    python entrypoint.py
    ```

2.  **Schedule as a Cron Job:**
    * Configure a cron job to execute `entrypoint.py` regularly (e.g., every hour) to continuously monitor your Gmail inbox.

## System Design
```
+-----------------------------------+
|           config.json             |
+-----------------------------------+
            |
            v
+---------------------+         +---------------------+
|  Gmail Metadata     |         |      Clearbit       |
|       API           +-------->+       API           |
|  (email_entrypoint) |         |   (clearbit.py)     |
+---------------------+         +---------------------+
            |                           |
            v                           v
+---------------------------------------------+
|         AI Analysis (OpenAI API)            |
|              + (aianalysis.py)              |
+---------------------------------------------+
            |
            v
+---------------------------------------------+
|            Webhook Integration              |
|          (requests in entrypoint.py)        |
+---------------------------------------------+
```

## Contributing

Contributions are welcome! Feel free to open issues, submit pull requests, or suggest improvements.

## License

This project is licensed under the MIT License. 

