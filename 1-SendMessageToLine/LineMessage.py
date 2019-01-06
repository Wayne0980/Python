from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage
from linebot.exceptions import LineBotApiError

CHANNEL_ACCESS_TOKEN = "Channel access token "
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

try:
    line_bot_api.push_message('object Your user ID', TextSendMessage(text='Warning Someone coming....Please check the your gmail to check the picture'))
except LineBotApiError as e:
    # error handle
    raise e
 
