from utils.Converter import Converter
from TGConvertor import SessionManager
import pathlib

async def start(thread: int, session_name: str, phone_number: str, proxy: [str, None]):
    Con = Converter(session_name=session_name, phone_number=phone_number, thread=thread, proxy=proxy)
    account = session_name + '.session'
    await Con.client.connect()
    session_string = await Con.client.export_session_string()
    await Con.client.disconnect()
    await Con.session.close()
    sess = SessionManager.from_pyrogram_string(session_string)
    p = pathlib.Path('tdatas/' + session_name)
    await sess.to_tdata_folder(path=p)
