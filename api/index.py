import os

from flask import Flask
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

app = Flask(__name__)

@app.route('/')
def home():
    llm = OpenAI(temperature=0.9)

    prompt = PromptTemplate(
        input_variables=["product"],
        template="What is a good name for a company that makes {product}?",
    )
    print(prompt.format(product="colorful socks"))

    chain = LLMChain(llm=llm, prompt=prompt)
    
    return llm(chain.run("colorful socks"))
