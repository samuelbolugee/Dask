import os
from apikey import apikey
import streamlit as st
from langchain.agents.agent_types import AgentType
from langchain.llms import OpenAI
from langchain.agents import create_csv_agent

os.environ['OPENAI_API_KEY'] = apikey

st.title("Dask - a simple app to query your CSVs!")

file = st.file_uploader("Please upload the file(s) in CSV format.", type = ['csv'], accept_multiple_files=True)

prompt = st.text_input("Your query goes here...")
final_prompt = "Considering ALL the data points in the dataset, " + prompt

llm = OpenAI(temperature = 0, model = "gpt-3.5-turbo-instruct")
agent = create_csv_agent(llm, file, verbose = True, agent_type = AgentType.ZERO_SHOT_REACT_DESCRIPTION)

if st.button("Run Query"):
    if prompt:
        response = agent.run(final_prompt)
        st.write(response)