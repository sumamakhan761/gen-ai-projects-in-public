from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.tools import DuckDuckGoSearchRun

def generate_script(prompt, video_length, creativity, api_key):
    # Title generation prompt
    title_template = PromptTemplate(
        input_variables=['subject'],
        template='Please come up with a title for a YouTube video on the {subject}.'
    )
    
    # Video script generation prompt
    script_template = PromptTemplate(
        input_variables=['title', 'DuckDuckGo_Search', 'duration'],
        template='Create a script for a YouTube video based on this title: "{title}" with a duration of {duration} minutes using this search data: {DuckDuckGo_Search}.'
    )
    
    llm = ChatGroq(temperature=creativity, groq_api_key=api_key,          model="llama-3.2-90b-vision-preview",)
    
    # Creating chains
    title_chain = LLMChain(llm=llm, prompt=title_template)
    script_chain = LLMChain(llm=llm, prompt=script_template)

    search = DuckDuckGoSearchRun()
    

    title = title_chain.run(subject=prompt)
    

    search_result = search.run(prompt)
    

    script = script_chain.run(title=title, DuckDuckGo_Search=search_result, duration=video_length)
    
    return search_result, title, script