# ==============================================================================
# Copyright (c) 2020, NVIDIA CORPORATION. All rights reserved.
#
# The License information can be found under the "License" section of the
# README.md file.
# ==============================================================================

client_config = {
    "CLIENT_APPLICATION": "WEBAPPLICATION", # Default and only config value for this version
    "PORT": 6006, # The port your flask app will be hosted at
    "DEBUG": False, # When this flag is set, the UI displays detailed Riva data
    "VERBOSE": True  # print logs/details for diagnostics
}

riva_config = {
    "RIVA_SPEECH_API_URL": "10.20.30.40:50051", # Replace the IP port with your hosted RIVA endpoint
    "VERBOSE": True  # print logs/details for diagnostics
}

dialogflow_config = {
    "VERBOSE": False, # Print logs/details for diagnostics
    "PROJECT_ID": "", # Add your google dialogflow weatherbot's project id here
    "LANGUAGE_CODE": "en"
}

asr_config = {
    "VERBOSE": False, # Print logs/details for diagnostics
    "SAMPLING_RATE": 16000, # The Sampling Rate for the audio input file. The only value currently supported is 16000
    "LANGUAGE_CODE": "en-US", # The language code as a BCP-47 language tag. The only value currently supported is "en-US"
    "ENABLE_AUTOMATIC_PUNCTUATION": True, # Enable or Disable punctuation in the transcript generated. The only value currently supported by the chatbot is True (Although Riva ASR supports both True & False)
}

tts_config = {
    "VERBOSE": True, # Print logs/details for diagnostics
    "SAMPLE_RATE": 22050, # The speech is generated at this sampling rate. The only value currently supported is 22050
    "LANGUAGE_CODE": "en-US", # The language code as a BCP-47 language tag. The only value currently supported is "en-US"
    "VOICE_NAME": "ljspeech", # The voice name for the speech generated. The only value currently supported is "ljspeech"
}
