import aiohttp

class translate:

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
    
    async def translate(self, source, target, text) -> dict:
        async with aiohttp.ClientSession() as session:
            request_url = "https://openapi.naver.com/v1/papago/n2mt"
            headers= {"X-Naver-Client-Id": self.client_id, "X-Naver-Client-Secret": self.client_secret}
            params = {"source": source, "target": target, "text": text}
            async with session.post(request_url, headers=headers, data=params) as resp:
                result = await resp.json()
                return result['message']['result']['translatedText']

