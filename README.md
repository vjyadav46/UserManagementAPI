Hi Novium,

Thank you for giving me the opportunity to be considered for a role at Novium. I am genuinely excited about the possibility of joining your esteemed organization and contributing with my automation expertise, particularly in Java-based automation frameworks.

As part of your assignment, I explored and implemented automation using Python, including configuration with Allure for reporting and Requests for API testing. Although my primary experience lies in Java, I took this assignment as a valuable opportunity to expand my skill set into Python-based test automation. I made use of tools like Gemini and GitHub Copilot within IntelliJ IDEA to assist in understanding errors and refining the code.

Here’s a brief summary of the technical work I completed:

Wrote automated test scripts in Python using PyTest

Implemented Allure reporting for test visualization

Configured Requests library for REST API automation

Debugged issues and improved scripts using AI tools for better productivity and learning

I gave my best effort in understanding the requirements and delivering a working solution, despite Python being relatively new to me. This demonstrates not only my adaptability but also my willingness and capability to quickly learn new technologies when needed.

I truly appreciate the chance to work on this assignment and hope it reflects my passion for automation and continuous learning. I believe that if I get the opportunity to join Novium, I can bring both technical value and a growth mindset that aligns with your team’s goals.


here is what i used int the code

# REST API Test Automation using Pytest and Allure
This repository contains an automated API test suite designed to validate the CRUD (Create, Read, Update, Delete) functionality of the User Management API provided by `fakerestapi.azurewebsites.net`.
The framework is built with **Python** and leverages powerful libraries such as **Pytest** for test execution, **Requests** for HTTP interactions, and **Allure** for generating detailed, interactive test reports.

## 📋 Table of Contents
* [Features](#-features)
* [Prerequisites](#-prerequisites)
* [Setup and Installation](#-setup-and-installation)
* [Running the Tests](#-running-the-tests)
* [Viewing the Allure Report](#-viewing-the-allure-report)
* [Project Structure](#-project-structure)

* **End-to-End Workflow Testing**: A single test case validates the entire user lifecycle: creating a user, retrieving them, updating their details, and finally, deleting them.
* **Detailed HTML Reporting**: Generates interactive Allure reports that provide a clear step-by-step breakdown of test execution.
* **Request & Response Logging**: Automatically attaches full request and response data (headers, body, status code) to the report for easy debugging.
* **Automatic Cleanup**: Uses a `finally` block to ensure test data (the created user) is deleted after the test run, even if assertions fail.
* **Structured & Scalable**: Built with `pytest`, making it easy to add more test cases and scale the framework.

 **Prerequisites**
Before you begin, ensure you have the following installed on your system:
1.  **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
2.  **pip** (Python's package installer, usually comes with Python)
3.  **Allure Commandline**: A separate tool required to generate the HTML report.
    * Follow the official installation guide for your operating system: [Installing Allure Commandline](https://allurereport.org/docs/getting-started-installation/)

 Setup and Installation
Follow these steps to set up the project locally.

1.  **Create a `requirements.txt` file:**
    Create a file named `requirements.txt` in the root of the project and add the following lines:
    ```
    pytest
    requests
    allure-pytest
    ```

2.  **Install the dependencies:**
    Run the following command in your terminal to install all the required Python packages.
    pip install -r requirements.txt

## ▶️ Running the Tests

To execute the automated tests, run the following command from the project's root directory:
pytest --alluredir=allure-results

* `pytest`: This command invokes the Pytest test runner.
* `--alluredir=allure-results`: This flag tells Pytest to collect Allure report data and store it in a directory named `allure-results`.

After running, you will see the test execution output in your terminal and a new `allure-results` directory will be created.

## 📊 Viewing the Allure Report

The raw data in the `allure-results` folder needs to be processed by the Allure Commandline tool to generate the HTML report.

1.  **Generate and serve the report:**
    Run this command in your terminal:
   allure serve allure-results
  

2.  **View in browser:**
    This command will start a local web server and automatically open the interactive Allure report in your default web browser. You can explore the test suite, view each step, and inspect the attached request/response data.



## 📂 Project Structure

The project follows a simple and intuitive structure.
.
├── allure-results/         # Contains raw Allure report data (auto-generated)
├── test_user_workflow.py   # The main test file containing the API test case
└── requirements.txt        # Lists the Python dependencies for the project
