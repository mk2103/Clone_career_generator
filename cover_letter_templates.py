


def engineer_cover_letter(role, company_name):
    return f"""
Hi {company_name} Team, 

My name is Chaitanya Desai, and I am very interested in the {role} role at {company_name}! 

Here's a little bit about me: 

I have been a software engineer at a startup called OURS in London for about 5 months now. I set up the OURS website using PostgreSQL, Ruby on Rails, React and Redux. I love to code and enjoy the balance of creating efficient and modular systems alongside beautiful and seamless UI/UX. Before I got into engineering: 

I have completed internships in Global Strategy and Operations at Visa, and Consulting at Ernst and Young, and have had some exposure to the payments space. I tried to start a hedge fund in NY with my mentor, which gave me invaluable networking and fundraising experience. It also gave me the chance to sharpen my skills in financial analysis and modeling, as well as insight into the challenges of starting a business. Working as an analyst at an impact fund gave me exposure to a range of early-stage startups and the operational constraints of scaling a business. Having concentrated in Data Science at USC, and completed App Academy in SF, I am proficient in Python, R, Ruby, JavaScript and SQL among other languages. I have built several projects since then: A clone of the crypto-currency exchange company coinbase; A data extraction tool integrated with Amazon Textract (an OCR Model) - which allows users to extract data from documents and structure the information into an excel-like table with custom built functions to parse the outputs.e. I love building new products and am always teaching myself new frameworks and languages. 

At USC I majored in Business Administration with concentrations in Finance and Data Science, I was also three courses short of a major in Judaism - which I forwent to work at Columbia Heights - the Hedge Fund I tried to start with my mentor. I was also a member of the USC Sidney Harman Academy for Polymathic Study. In my Junior year, I enrolled in an exchange program in Hong Kong where I studied Eastern Philosophy and Chinese Business at the Chinese University of Hong Kong.
	
I’m a hard-working, determined, and enthusiastic individual. I thrive in work environments that are constantly evolving - where process is flexible and creative solutions are the norm. I’m self-driven but also love working in teams. 

I think {company_name} is a great company with an awesome product, and I am very excited by the prospect of being a part of your team. I would love to get on a phone call to learn more about {company_name}, tell you more about myself, and see if there's a good fit. 

I appreciate your valuable time and look forward to hearing from you. 


Kind Regards, 

Chaitanya Desai 
"""

def generalist_email(company_name): 
    return f"""
Hi {company_name},


My name is Chaitanya Desai, and I am very interested in working at {company_name}!
Here's a little bit about me:

I have been a software engineer at a startup called OURS in London for about 5 months now. I set up the OURS website using PostgreSQL, Ruby on Rails, React and Redux. I love to code and enjoy the balance of creating efficient and modular systems alongside beautiful and seamless UI/UX. Before I got into engineering:

I have completed internships in Global Strategy and Operations at Visa, and Consulting at Ernst and Young, and have had some exposure to the payments space. I tried to start a hedge fund in NY with my mentor, which gave me invaluable networking and fundraising experience. It also gave me the chance to sharpen my skills in financial analysis and modeling, as well as insight into the challenges of starting a business. Working as an analyst at an impact fund gave me exposure to a range of early-stage startups and the operational constraints of scaling a business. Having concentrated in Data Science at USC, and completed App Academy in SF, I am proficient in Python, R, Ruby, JavaScript and SQL among other languages. I have built several projects since then: A clone of the crypto-currency exchange company coinbase
A data extraction tool integrated with Amazon Textract(an OCR Model) - which allows users to extract data from documents and structure the information into an excel-like table with custom built functions to parse the outputs.e. I love building new products and am always teaching myself new frameworks and languages.

At USC I majored in Business Administration with concentrations in Finance and Data Science, I was also three courses short of a major in Judaism - which I forwent to work at Columbia Heights - the Hedge Fund I tried to start with my mentor. I was also a member of the USC Sidney Harman Academy for Polymathic Study. In my Junior year, I enrolled in an exchange program in Hong Kong where I studied Eastern Philosophy and Chinese Business at the Chinese University of Hong Kong.

I’m a hard-working, determined, and enthusiastic individual. I thrive in work environments that are constantly evolving - where process is flexible and creative solutions are the norm. I’m self-driven but also love working in teams.

I think {company_name} is a great company with an awesome product, and would love to work on your team.  I believe I can wear several hats and would be open to considering any roles you may have available at the moment. 

I appreciate your valuable time and look forward to hearing from you.


Kind Regards,

Chaitanya Desai 
"""

def choose_cover_letter(company_name, role, job_type):

    print ("Job Type: ", job_type)
    print ("Company Name: ", company_name)
    print ("Role: ", role)

    if job_type == "Engineering":
        return engineer_cover_letter(role, company_name)

    elif job_type == "Product":
        return engineer_cover_letter(role, company_name)
    
    elif job_type == "Generalist": 
        return generalist_email(company_name)

    elif job_type == "Analyst": 
        return engineer_cover_letter(role, company_name)
    else: 
        return engineer_cover_letter(role, company_name)


def generate_cover_letter(text):
    file = open("/Users/chaitanyadesai/desktop/cover_letter.txt", "w")
    file.write(text)
    file.close() 


