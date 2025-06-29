import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

from dotenv import load_dotenv
load_dotenv()
os.getenv('GROQ_API_KEY')

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0,groq_api_key= os.getenv('GROQ_API_KEY'),model_name = "llama-3.3-70b-versatile")

    def extract_jobs(self,cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """## SCRAPED TEXT FROM WEBSITE:
    {page_data}
    ### INSTRUCTION:
    The scraped text is from the career's page of a website.
    Your job is to extract the job posting and return them in JSON format containing the 
    following keys: 'role','experience','skills',and 'description'.
    Only return the valid JSON.
    ### VALID JSON (NO PREAMBLE)"""
        )
        chain_extract = prompt_extract | self.llm
        response = chain_extract.invoke(input={'page_data':cleaned_text})
        try:
            json_parser = JsonOutputParser()
            response = json_parser.parse(response.content)

        except OutputParserException:
            raise OutputParserException("Content too big. Unable to parse jobs")

        return response if isinstance(response,list) else [response]


    def write_mail(self,job,links):
        prompt_email = PromptTemplate.from_template(
            """
             ### JOB DESCRIPTION
    {job_description}
    
    ### INSTRUCTION:
    You are Harry, a Data Scientist who is looking for an internship or a job.
    You have descent experience in all the tools  like python , pandas, numpy, tensorflow, machine learning, deeplearning, etc
    Your job is to write a cold email to the HR regarding the job mentioned above describing the capability of your skills and knowledge
    in fulfilling their needs. 
    Also add the most relevant ones from the following links to showcase Your portfolio: {link_list} Don't madeup any links to show project only use project that are given in my_portfolio.csv file
    Remember you are Harry,Data Scientist Fresher.
    Do not provide a preamble. format the email like a professional
    ### EMAIL (NO PREAMBLE):
            """
        )
        chain_mail = prompt_email | self.llm
        response = chain_mail.invoke({'job_description': str(job), 'link_list':links})
        return response.content

if __name__ == '__main__':
    pass
