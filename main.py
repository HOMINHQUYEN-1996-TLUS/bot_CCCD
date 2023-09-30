from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '6509296492:AAH_i5pMrMbhaIjaLzRtFdUVf97fl5cSa2M'
BOT_USERNAME: Final = '@Muc_hai_bot'

#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Xin chào! Rất vui vì được chat với bạn tôi là CCCD có thể dùng lệnh /help để xem hướng dãn')

async def fee_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Cấp mới : 15k đối với người đã có CMND 9 số hoặc 12 số \n Cấp đổi : 25k đối với người cần they đổi thông tin trên thẻ vd : ngày sinh, quê quán, họ tên , ... \n Cấp lại : 35k đối với người bị mất thẻ')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('/fee : là dùng để xem mức phí khi làm CCCD')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Đây là một câu lệnh tuỳ chọn')

#Responds
def handle_response(text: str)->str:

    proccessed: str = text.lower()

    if 'xin chào' in proccessed:
        return 'Tôi ở đây'
    if 'Bạn khoẻ không' in proccessed:
        return 'Tôi Khoẻ'
    return 'Tôi không hiểu ý của bạn'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User({update.message.chat.id}) in {message_type} : "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else :
        response: str = handle_response(text)
    print('Bot ', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':

    print('Starting bot .....')
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('fee', fee_command))

    #Message
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #Error
    app.add_error_handler(error)

    #Polling Bot
    print('Polling .....')
    app.run_polling(poll_interval=3)
