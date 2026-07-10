import base64
from fireworks.client import Fireworks
from fireworks.client import Fireworks 
class VideoAnalysisAgent:
    def __init__(self, api_key):
        self.client = Fireworks(api_key=api_key)
        self.model_name = "accounts/fireworks/models/kimi-k2p6"
        self.tones = {
            "sarcastic": "You are a witty, cynical assistant. Provide a summary that mocks the events as if they were a monumental disaster.",
            "formal": "You are a professional consultant. Provide an objective, concise, and academic analysis.",
            "humorous_tech": "You are a fun-loving tech enthusiast. Use slang, enthusiasm, and light-hearted jokes to explain the technical concepts.",
            "non_humorous_tech": "You are a senior systems engineer. Provide a clinical, precise, and purely factual technical report."
        }

    def analyze_storyboard(self, frames, prompt, tone_key="formal"):
        system_instruction = self.tones.get(tone_key, self.tones["formal"])
        system_instruction += " Only answer based on the provided frames. If you cannot see it, say you cannot see it."
        content = [{"type": "text", "text": prompt}]
        for frame_b64 in frames:
            content.append({"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{frame_b64}"}})

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "system", "content": system_instruction}, {"role": "user", "content": content}]
        )
        return response.choices[0].message.content