# Blog Generation Using LLAMA2

This project is a web application that allows users to generate blog posts based on specified topics and styles using the LLAMA2 model. It leverages `streamlit` for the user interface and `CTransformers` for model deployment.

## Project Overview

The application allows users to:

- Enter a topic for the blog.
- Specify the number of words for the blog post.
- Choose the style of the blog writing.
- Generate a blog post based on the provided inputs using the LLAMA2 model.

## Requirements

To run this project, you'll need to install the following Python packages:

- `sentence-transformers`: For working with transformer models.
- `uvicorn`: ASGI server for serving the Streamlit app.
- `ctransformers`: For loading and using transformer models efficiently.
- `langchain`: For building language models and processing text.
- `python-box`: For configuration management.
- `streamlit`: For creating the interactive web application.

You can install the required packages using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt

**## Conceptual Understanding**

### `app.py`

The `app.py` script sets up a Streamlit web application that interacts with the LLAMA2 model. Here's a conceptual breakdown of the code:

#### Imports and Setup

- **`streamlit as st`**: Imports Streamlit, which is used to build the web interface for the application.
- **`langchain.prompts.PromptTemplate`**: Imports the `PromptTemplate` class for creating templates for the LLAMA2 model prompts.
- **`langchain.llms.CTransformers`**: Imports `CTransformers` to load and use the LLAMA2 model efficiently.

#### Model Initialization

- **`getLLamaresponse(input_text, no_words, blog_style)`**: This function initializes the LLAMA2 model using `CTransformers` and generates a blog post based on user inputs. It configures the model with parameters like `max_new_tokens` (maximum number of tokens the model can generate) and `temperature` (controls randomness in the model's responses).

- **`PromptTemplate`**: Defines a prompt template that formats the input variables (blog style, topic, and word count) into a string that the LLAMA2 model can process.

- **`llm(prompt.format(...))`**: Generates a response from the LLAMA2 model based on the formatted prompt. This response is the generated blog post.

#### Streamlit Interface

- **`st.set_page_config`**: Configures the Streamlit page with a title, icon, and layout settings.

#### Input Fields

- **`st.text_input("Enter the Blog Topic")`**: Allows the user to enter the topic of the blog.
- **`st.text_input('No of Words')`**: Lets the user specify the number of words for the blog post.
- **`st.selectbox('Writing the blog for', ...)`**: Provides a dropdown menu for selecting the blog style.
- **`st.button("Generate")`**: A button that triggers the blog generation when clicked.

- **`st.write(getLLamaresponse(...))`**: Displays the generated blog post on the web interface once the user clicks the "Generate" button.


