# 🤗🤗 HuggingFace QA + Docker

# Description

This project is a simple Question and Answer model that implements a pre-trained pytorch HuggingFace model. The model makes use of a sample training dataset, and only using contexts with topics about `Premiere League`. The user may send a sample question about Premiere League, and the model will give out the best possible rendering of the original question, as well as give out the best possible answer to the question.

![Screen Shot 2022-10-23 at 10.00.41 PM.png](%F0%9F%A4%97%F0%9F%A4%97%20HuggingFace%20QA%20+%20Docker%209950a685341641b89b8a127be28422a5/Screen_Shot_2022-10-23_at_10.00.41_PM.png)

---

# Overview

1. Create QAEmbedder class that `gets the model` from pre-trained model, and `gets the embeddings` given a set of questions
    
    See code for more details
    
2. Create QASearcher class that sets the context, as well as handles the answer to the original and best question
3. Create FastAPI application
    - This manages which endpoint sets the context, and handles the QA portion
4. Creating Dockerfile for Docker image
5. Testing the app using the pre-created test scripts

---

# Running the Service

## VirtualEnv and Dependencies Installation

Before running the API, create a virtual environment and install the dependencies in the **requirements.txt** file. 

```bash
$ virtualenv huggingface
$ source huggingface/bin/activate
(huggingface)$ pip3 install -r path/to/requirements.txt
```

## Create Docker Image

[Docker](https://docs.docker.com/desktop/install/mac-install/) must also be installed in the machine

Run this to build an image, and run the container

```bash
docker build . -t qamodel &&\
  docker run -p 8000:8000 qamodel
```

## Testing

When the service is already running, test it using the `test_set_context.py` and `test_get_answer.py` scripts.

### test_set_context.py

```bash
(huggingface)$ python3 test_set_context.py
```

![Screen Shot 2022-10-23 at 10.16.37 PM.png](%F0%9F%A4%97%F0%9F%A4%97%20HuggingFace%20QA%20+%20Docker%209950a685341641b89b8a127be28422a5/Screen_Shot_2022-10-23_at_10.16.37_PM.png)

### test_get_answer.py

```bash
(huggingface)$ python3 test_get_answer.py
```

![Screen Shot 2022-10-23 at 10.00.41 PM.png](%F0%9F%A4%97%F0%9F%A4%97%20HuggingFace%20QA%20+%20Docker%209950a685341641b89b8a127be28422a5/Screen_Shot_2022-10-23_at_10.00.41_PM.png)

# References

[Build a Q&A App with PyTorch](https://towardsdatascience.com/build-a-q-a-app-with-pytorch-cb599480e29)