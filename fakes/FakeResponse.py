class FakeUsage:
    prompt_tokens = 128
    completion_tokens = 32
    total_tokens = 160


class FakeMessage:
    role = "assistant"
    content = "this is a fake response"


class FakeChoice:
    index = 0
    message = FakeMessage()
    finish_reason = "stop"


class FakeResponse:
    choices: [FakeChoice] = [FakeChoice]
    id = "FAKE_ID"
    object = "chat.completion"
    created = 1690507805
    model = "gpt-3.5-turbo-0613"
    usage = FakeUsage()


def create_fake_response(message: str):
    fake_response = FakeResponse()
    fake_response.id = "fake-id:92492949293915935"
    fake_response.object = "chat.completion"
    fake_response.created = 9165050875
    fake_response.model = "gpt-3.5-turbo-0613"
    fake_response.usage = FakeUsage()
    fake_response.usage.total_tokens = 24
    fake_response.usage.prompt_tokens = 8
    fake_response.usage.completion_tokens = 16
    fake_choice = FakeChoice()
    fake_choice.message = FakeMessage()
    fake_choice.message.role = "assistant"
    fake_choice.message.content = "fake assistant responded with this fake choice"
    fake_choice.finish_reason = "STOP"
    fake_choice_2 = FakeChoice()
    fake_choice_2.message.role = "human"
    fake_choice_2.message.content = message
    fake_choice_2.finish_reason = None
    fake_choice_2.index = 1
    fake_response.choices = [
        fake_choice,
        fake_choice_2
    ]
    return fake_response
