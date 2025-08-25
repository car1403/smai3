import streamlit as st
from langchain.agents import initialize_agent, AgentType
from langchain_community.agent_toolkits.load_tools import load_tools

from MyLCH import getOpenAI, progressBar

st.markdown("Page1")
st.sidebar.markdown("Clicked Page1")

text = st.text_area(label="질문입력:",   placeholder="질문을 입력 하세요")

if st.button("SEND"):
    if text:
        st.info(text)
        openllm = getOpenAI()
        tools = load_tools(['wikipedia'], llm=openllm)
        agent = initialize_agent(
            tools,
            openllm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=False
        )
        my_bar = progressBar()
        st.info(agent.run(text))
        my_bar.empty()

    else:
        st.info("질문을 입력하세요")