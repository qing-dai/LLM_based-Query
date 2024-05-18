from unittest import TestCase

from utils import format_as_chat


class UtilsTestCase(TestCase):

    def test_format_as_chat(self):
        self.user_message_1 = "Howdy!"
        self.assistant_message_1 = "Hi, how can I help you?"
        self.user_message_2 = "What's the weather today?"
        self.assistant_message_2 = "As an AI, I don't know about wheather."
        self.user_message_3 = "OK"

        self.assertEqual(
            '<|begin_of_text|>'
            '<|start_header_id|>user<|end_header_id|>\n\nHowdy!<|eot_id|>',
            format_as_chat(self.user_message_1, [])
        )

        self.assertEqual(
            '<|begin_of_text|>'
            '<|start_header_id|>user<|end_header_id|>\n\nHowdy!<|eot_id|>'
            '<|start_header_id|>assistant<|end_header_id|>\n\nHi, how can I help you?<|eot_id|>'
            '<|start_header_id|>user<|end_header_id|>\n\nWhat\'s the weather today?<|eot_id|>',
            format_as_chat(self.user_message_2, [[self.user_message_1, self.assistant_message_1]])
        )

        self.assertEqual(
            '<|begin_of_text|>'
            '<|start_header_id|>user<|end_header_id|>\n\nHowdy!<|eot_id|>'
            '<|start_header_id|>assistant<|end_header_id|>\n\nHi, how can I help you?<|eot_id|>'
            '<|start_header_id|>user<|end_header_id|>\n\nWhat\'s the weather today?<|eot_id|>'
            '<|start_header_id|>assistant<|end_header_id|>\n\nAs an AI, I don\'t know about wheather.<|eot_id|>'
            '<|start_header_id|>user<|end_header_id|>\n\nOK<|eot_id|>',
            format_as_chat(self.user_message_3, [[self.user_message_1, self.assistant_message_1], [self.user_message_2, self.assistant_message_2]])
        )
