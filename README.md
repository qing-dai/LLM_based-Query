# Assignment 7
Text Generation with Language Models\
Due: Tuesday, May 21, 2024, 16:00

---

**Name:** Qing Dai

**Student ID:**  21- 742 - 366

Names of collaborators:

**Task 1, testing the API in the browser.**

With the `request body` set as 

`{
  "inputs": "Howdy!",
  "parameters": {
    "do_sample": false,
    "max_new_tokens": 40
  }
}`
we can switch the query into mode of "greedy decoding". If input 

`Howdy!`,


the output is: 

` I'm a software engineer with a passion for building scalable and maintainable systems. I've worked on a variety of projects, from mobile apps to web applications, and I'm always looking for new challenges`


**Task 2, Formatting the prompt as an instruction**

`output1: {'generated_text': " I'm a software engineer with a passion for building scalable and maintainable systems. I've worked on a variety of projects, from mobile apps to web applications, and I'm always looking for new challenges"}`

`output2: {'generated_text': 'assistant\n\nHowdy back atcha! What brings you to these here parts?'}`


**1. Observation:**

1. The model identifies the signal from the format of conversation requirement, so it then outputs in a more interactive way, as intended in a conversational setting. 
Unlike the first output, which is more general. 
2. The model identifies the role from the input as "user", so in the output, it switches to identity of "assistant" to reply back.

**2. Call the API with the concatenated prompt and log the conversation below.**

`'generated_text': "assistant\n\nWell, shucks! I'm happy to help you tackle those assignments! What kind of assignments do you have? Are they related to a specific subject or topic? Let me know"}`

**Task3, creating a chat interface**

The screenshot of the conversation is submitted in an extra "jpg" file.

**Task 3, the final optional Machine Translation task, the deployed app URL is here, please try it out!** https://huggingface.co/spaces/qdai/LLM3_Model
