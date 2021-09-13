import translatetool
import asyncio


async def runit():
    add = translatetool.translate("SfbGsa1PLAc0jJ8J8_OG", "SD9226FaO1")
    add1 = await add.translate("ko", "en", "안녕하세요, 테스트 입니다.")
    print(add1)


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(runit())