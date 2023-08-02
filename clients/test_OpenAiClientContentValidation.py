import unittest

from clients.OpenAiClient import OpenAiClient
from helpers.ArgumentException import ArgumentException


class TestOpenAiClientContentValidation(unittest.TestCase):
    def test_empty_call_raises(self):
        # model = None
        system_message = None
        message = None
        self.assertRaises(
            ArgumentException,
            OpenAiClient.validate_content,
            message=message,
            system_message=system_message
        )

    def test_ok_call_returns(self):
        # model = None
        system_message = "You are some kind of expert"
        message = "Please explain something"
        OpenAiClient.validate_content(
            message=message,
            system_message=system_message
        )
        self.assertEqual(True, True, "Exceptions should not be thrown and this line should be executed.")
