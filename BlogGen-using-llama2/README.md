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

