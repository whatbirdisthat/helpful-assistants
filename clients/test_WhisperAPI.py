import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        expected = "famous quoote from jfk"
        import os
        os.environ["OPENAI_ORGANISATION"] = "OPENAI_ORGANISATION"
        os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"
        os.environ["OPENAI_API_URL"] = "http://127.0.0.1:8080"

        from clients.OpenAiClient import OpenAiClient
        the_client = OpenAiClient("http://127.0.0.1:8080")
        with open("docs/examples/jfk.wav", 'rb') as audio_file:
            actual = the_client.call_openai_whisper_endpoint(audio_file)

        self.assertEqual(actual, expected)  # add assertion here


if __name__ == '__main__':
    unittest.main()
