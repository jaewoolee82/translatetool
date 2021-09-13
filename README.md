# translatetool
A Papago Translate module.

## Example

```py
import translatetool
import asyncio


async def runit():
    add = translatetool.translate("Papago Client ID", "Papago Client Secret") # https://developers.naver.com/ 에서 발급
    add1 = await add.translate("ko", "en", "안녕하세요, 테스트 입니다.") # 언어: ko, en, ja, zh-CN, zh-TW, vi, id, th, de, ru, es, it, fr
    print(add1)


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(runit())
```

## Language List
![](https://i.ibb.co/d2Fcs2B/image1.png)
