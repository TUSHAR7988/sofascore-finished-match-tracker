# import asyncio
# from utils.state import is_new
# from config.settings import POLL_INTERVAL_SECONDS
# from sports.football import get_today_events_url, extract_finished_matches
# from core.browser import browser_fetch_json
# from utils.json_writer import write_match_json
# from core.semaphore import SEMAPHORE



# async def poll_finished_matches(context):

#     while True:
#         try:
#             async with SEMAPHORE:


#                 payload = await browser_fetch_json(

#                     context,

#                     get_today_events_url()
#             )

#             matches = extract_finished_matches(payload)

            

#             for m in matches:
#                 if is_new(m["match_id"]):
#                     write_match_json(m)


#         except Exception as e:
#             print("[POLL][ERROR]", e)

#         await asyncio.sleep(POLL_INTERVAL_SECONDS)


import asyncio
from core.browser import browser_fetch_json
from core.semaphore import SEMAPHORE
from sports.football import get_today_events_url, extract_finished_matches
from utils.state import is_new
from utils.json_writer import write_match_json
from config.settings import POLL_INTERVAL_SECONDS


async def poll_finished_matches(context):
    while True:
        try:
            async with SEMAPHORE:
                payload = await browser_fetch_json(
                    context,
                    get_today_events_url()
                )

            matches = extract_finished_matches(payload)

            for match in matches:
                if is_new(match["match_id"]):
                    write_match_json(match)
                    print("[NEW FINISHED MATCH]", match)

        except Exception as e:
            print("[POLL][ERROR]", e)

        await asyncio.sleep(POLL_INTERVAL_SECONDS)
