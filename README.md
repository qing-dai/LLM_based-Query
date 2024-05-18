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
    "max_new_tokens": 20
  }
}`
we can switch the query into mode of "greedy decoding". If input 

`Howdy!`,


the output is: 

`I'm a software engineer with a passion for building scalable and maintainable systems. I've worked on`

---

**Formatting the prompt as an instruction**

`output1: [{'generated_text': "Howdy! I'm a software engineer with a passion for building scalable and maintainable systems. I've worked on"}]

output2: [{'generated_text': '<|begin_of_text|><|start_header_id|>user<|end_header_id|>\nHowdy!<|eot_id|>assistant\n\nHowdy back atcha! What brings you to these here parts?'}]
`

**1. Observation:**

1. The model identifies the signal from the format of conversation requirement, so it then outputs in a more interactive way, as intended in a conversational setting. 
Unlike the first output, which is more general. 
2. The model identifies the role from the input as "user", so in the output, it switches to identity of "assistant" to reply back.

**2. Call the API with the concatenated prompt and log the conversation below.**

`"<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\nHowdy!<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\nHowdy back atcha! What brings you to these here parts?<|eot_id|><|start_header_id|>user<|end_header_id|>\n\nMy assignments!<|eot_id|>assistant\n\nWell, shucks! I'm happy to help you tackle those assignments! What"`


