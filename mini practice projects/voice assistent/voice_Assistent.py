from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from elevenlabs.types import ConversationConfig
import os
from dotenv import load_dotenv

load_dotenv()

AGENT_ID = os.getenv("AGENT_ID")
API_KEY = os.getenv("API_KEY")

user_name = "Shaani"
schedule = "workout from 7 am to 8 am , completing course modules from 10 am to 12 pm  , push projects from 1 pm to 3 pm , complete unit 1 of DA from 4 pm to 5 pm , and leisure reading from 6 pm to 7 pm."
prompt = f"You are a helpful assistant. Your interlocutor has the following schedule: {schedule}."
first_message = f"Hello {user_name}, how can I help you today?"

conversation_override = {
    "agent": {
        "prompt": {"prompt": prompt},
        "first_message": first_message,
    }
}

config = ConversationConfig(
    agent_id=AGENT_ID,
    enable_avatars=False,
    dynamic_variables={},
    extra_body={}
)



client = ElevenLabs(api_key=API_KEY)

conversation = Conversation(
    client,
    AGENT_ID,
    config=config,
    requires_auth=True,
    audio_interface=DefaultAudioInterface(),
)

conversation.start_session()
