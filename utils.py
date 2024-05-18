from typing import List


def format_as_chat(message: str, history: List[List[str]]) -> str:
    """
    Given a message and a history of previous messages, returns a string that formats the conversation as a chat.
    Uses the format expected by Meta Llama 3 Instruct.

    :param message: A string containing the user's most recent message
    :param history: A list of lists of previous messages, where each sublist is a conversation turn:
        [[user_message1, assistant_reply1], [user_message2, assistant_reply2], ...]
    """
    chat_format = "<|begin_of_text|>"
    if len(history) > 0:
        for turn in history:
            user_message, assistant_message = turn
            chat_format += f"<|start_header_id|>user<|end_header_id|>\n\n{user_message}<|eot_id|>"
            chat_format += f"<|start_header_id|>assistant<|end_header_id|>\n\n{assistant_message}<|eot_id|>"

    # Append the most recent user message
    chat_format += f"<|start_header_id|>user<|end_header_id|>\n\n{message}<|eot_id|>"
    return chat_format
