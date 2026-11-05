import edge_tts
import asyncio


async def _tts_async(text, output_path):
    communicate = edge_tts.Communicate(text, voice="en-US-JennyNeural")
    await communicate.save(output_path)


def text_to_speech(text, output_path="output.mp3"):
    asyncio.run(_tts_async(text, output_path))
