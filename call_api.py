import requests


## Call the API using Python
def generate_output(payload):

    # Sending the request
    response = requests.post('https://uf9t072wj5ki2ho4.eu-west-1.aws.endpoints.huggingface.cloud/generate', json=payload)

    # Handling the response
    data = response.json()

    return data





# Payload for the request
#
# payload1 = {
#     "inputs": "Howdy!",
#     "parameters": {
#         "do_sample": False,
#         "max_new_tokens": 40
#     }
# }
#
# output1 = generate_output(payload1)
# print(f"output1: {output1}")
#
# formatted_input = (
#     "<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\nHowdy!<|eot_id|>"
# )
# payload2 = {
#     "inputs": formatted_input,
#     "parameters": {
#         "do_sample": False,
#         "max_new_tokens": 40
#     }
# }
#
#
# output2 = generate_output(payload2)
# print(f"output2: {output2}")
#
# multi_turn_input = "<|begin_of_text|>" \
#                    "<|start_header_id|>user<|end_header_id|>\n\nHowdy!<|eot_id|>" \
#                    "<|start_header_id|>assistant<|end_header_id|>\n\nHowdy back atcha! What brings you to these here parts?<|eot_id|>" \
#                    "<|start_header_id|>user<|end_header_id|>\n\nMy assignments!<|eot_id|>"
#
# payload3 = {
#     "inputs": multi_turn_input,
#     "parameters": {
#         "do_sample": False,
#         "max_new_tokens": 40
#     }
# }
#
#
# output3 = generate_output(payload3)
# print(f"output3: {output3}")
#
