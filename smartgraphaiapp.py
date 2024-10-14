import streamlit as st
from scrapegraphai.graphs import SmartScraperGraph
import pandas as pd
import plotly.express as px
from io import BytesIO
import base64

st.set_page_config(layout="wide")

st.title("Advanced Web Scraping AI Agent 🕵️‍♂️")
st.caption("This app allows you to scrape a website using OpenAI API with advanced features")

# Sidebar for configurations
with st.sidebar:
    st.header("Configuration")
    openai_access_token = st.text_input("OpenAI API Key", type="password")
    model = st.radio("Select the model", ["gpt-3.5-turbo", "gpt-4"], index=0)
    max_tokens = st.slider("Max Tokens", 100, 2000, 500)
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7)

if openai_access_token:
    graph_config = {
        "llm": {
            "api_key": openai_access_token,
            "model": model,
            "max_tokens": max_tokens,
            "temperature": temperature,
        },
    }

    # Main content area
    col1, col2 = st.columns(2)

    with col1:
        url = st.text_input("Enter the URL of the website you want to scrape")
        user_prompt = st.text_area("What do you want the AI agent to scrape from the website?")

    with col2:
        output_format = st.selectbox("Select output format", ["Text", "JSON", "CSV"])
        visualize = st.checkbox("Visualize data (if applicable)")

    # Create a SmartScraperGraph object
    smart_scraper_graph = SmartScraperGraph(
        prompt=user_prompt,
        source=url,
        config=graph_config
    )

    # Scrape the website
    if st.button("Scrape"):
        with st.spinner("Scraping in progress..."):
            result = smart_scraper_graph.run()

        if output_format == "JSON":
            st.json(result)
        elif output_format == "CSV":
            df = pd.DataFrame(result)
            st.dataframe(df)
            
            # Download button for CSV
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="scraped_data.csv">Download CSV File</a>'
            st.markdown(href, unsafe_allow_html=True)

            if visualize:
                try:
                    fig = px.bar(df, x=df.columns[0], y=df.columns[1], title="Scraped Data Visualization")
                    st.plotly_chart(fig)
                except:
                    st.warning("Unable to visualize the data. Please ensure it's in a suitable format.")
        else:
            st.write(result)

        # Sentiment Analysis
        st.subheader("Sentiment Analysis")
        sentiment_prompt = f"Analyze the sentiment of the following scraped content: {result}"
        sentiment_result = SmartScraperGraph(prompt=sentiment_prompt, config=graph_config).run()
        st.write(sentiment_result)

    # Error handling
    st.error("Please enter a valid OpenAI API key, URL, and prompt.")

# Add a footer
st.markdown("---")
st.markdown("Created with ❤️ by Your Name")
