import datetime
import pyperclip
from cover_letter_templates import generate_cover_letter, choose_cover_letter
from sheets_api import get_credentials, add_row

class JobApplication:

    def __init__(self):
        self.details = {
            "Date": datetime.datetime.today().strftime('%d-%m-%Y')
        }
        self.add_company()
        self.add_type()
        self.add_role()
        self.add_method()

    def add_company(self):
        company = input("What company did you apply to?\n>> ")
        self.details["Company"] = company

    def add_type(self):
        job_type = input(
            "Is it a Product, Engineering, Analyst, or Generalist role?\n>> ")
        self.details["Type"] = job_type

    def add_role(self):
        job_role = input("What is the job title? (Use the present particple):\n>> ")
        self.details["Role"] = job_role


    def add_method(self):
        method = input("What platform did you apply on?\n>> ")
        self.details["Method"] = method


def main():
    job          = JobApplication()
    company_name = job.details["Company"].strip()
    role         = job.details["Role"].strip()
    job_type     = job.details["Type"].strip()
    method       = job.details["Method"].strip()
    date         = job.details["Date"]

    text = choose_cover_letter(company_name, role, job_type)
    generate_cover_letter(text)
    pyperclip.copy(text)
    
    credentials = get_credentials()
    add_row(credentials, company_name, role, job_type, method, date)

    print(
        f"""

APPLICATION DETAILS:

Company Name: {company_name}
Role: {role}
LinkedIn URL: https://www.linkedin.com/in/chaitanya-desai-4602a6119/
Github URL: https://github.com/chaitanyavd
Sheets URL: https://docs.google.com/spreadsheets/d/1PZglQmVU2Wkye2cjHqGito3Lis5HVxPyNFMa-sC64Gg/edit#gid=0"

Cover Letter copied to clipboard, and can be found on the Desktop as cover_letter.txt
Application details have been added to "Careers May 2018":

        """
    )


if __name__ == "__main__":
    main()
