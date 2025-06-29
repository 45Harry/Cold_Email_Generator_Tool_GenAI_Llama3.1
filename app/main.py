import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm,portifolio,clean_text):

    st.title("Cold Mail Generator")
    url_input = st.text_input("Enter a URL:",value="https://careers.nike.com/nike-stores-franchise-partner-manager/job/R-64538")
    submit_button = st.button("Submit")


    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portifolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = job.get('skills',[])
                links = portifolio.query_links(skills)
                email = llm.write_mail(job,links)
                st.code(email,language='markdown')
        except Exception as e:
            st.error(f'An Error Occured: {e}')


if __name__ == '__main__':
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout='wide',page_title='Cold Email Generator',page_icon=" ")
    create_streamlit_app(chain,portfolio,clean_text )
