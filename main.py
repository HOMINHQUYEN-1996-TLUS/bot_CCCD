from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
from dotenv import load_dotenv

load_dotenv()
print(os.getenv("TOKEN"))
BOT_USERNAME: Final = '@Muc_hai_bot'

#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Bấm /CCCD để xem hướng dẫn liên quan đên CCCD hoặc'
                                    '\n /DDDT để xem hướng dãn liên quan đến Định danh điện tử')
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('/CCCD để xem hướng dẫn liên quan đên CCCD'
                                    '\n /DDDT để xem hướng dãn liên quan đến Định danh điện tử'
                                    '\n /quy_trinh để xem quy trình cấp thẻ CCCD'
                                    '\n /phi để xem mức phí khi làm thẻ'
                                    '\n /lien_quan để xem các vấn đề liên quan')

async def CCCD_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('/quy_trinh để xem quy trình cấp thẻ CCCD'
                                    '\n /phi để xem mức phí khi làm thẻ'
                                    '\n /lien_quan để xem các vấn đề liên quan')

async def quyTrinh_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('B1: Công dân đăng ký dịch vụ công tại trang https://dichvucong.bocongan.gov.vn/?home=1' 
                                    '( bấm /DVC để xem hướng dẫn đăng ký Dịch vụ công)'
                                    '\n B2: Sau khi công dân đăng ký thành công trên cổng DVC phải đến nơi mà công dân đăng ký để làm thủ tục tiếp theo'
                                    '\n B3: Nghe cán bộ gọi tên để hỏi các thông tin'
                                    '\n B4: Tiến hành chụp hình và lăn tay'
                                    '\n B5: Nhận giấy CC02 và biên lai ( nếu có ) và ký nộp lại cho cán bộ'
                                    '\n B6: Công dân có thể lựa chọn 2 cách để nhận thẻ. 1 là tại nơi làm hoặc liên hệ nhân viên Bưu điện để đăng ký gửi về nhà')
    
async def phi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Về mức phí có 3 loại mức tương ứng với từng loại cấp'
                                    '\n 1: Cấp mới: 15.000 vnd hoặc miễn phí bấm /capmoi_CCCD để xem chi tiết'
                                    '\n 2: Cấp đổi: 25.000 vnd hoặc miễn phí bấm /capdoi_CCCD để xem chi tiết'
                                    '\n 3: Cấp lại: 35.000 vnd bấm /caplai_CCCD để xem chi tiết')

async def capmoi_CCCD_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Những trường hợp thuộc cấp mới : '
                                    '\n 1: Đã có CMND 9 số hoặc 12 số. Trường hợp này phí sẽ là 15.000 vnd'
                                    '\n 2: Chưa có CMND 9 số hoặc 12 số. Trường hợp này sẽ miễn phí')   

async def capdoi_CCCD_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Những trường hợp thuộc cấp đổi : '
                                    '\n 1: Thay đổi thông tin trên thẻ ( ngày sinh, số CMND, địa chỉ, ...) phí sẽ là 25.000 vnd'
                                    '\n 2: Thẻ hết hạn. Nếu công dân đi làm lại thẻ trước ngày hết hạn thì phí sẽ là 25.000'
                                    'vnd. Còn sau khi hết hạn mới đi đỏi thì sẽ là MIỄN PHÍ'
                                    '\n 3: Công dân muốn thay đổi ảnh hoặc cảm thấy thẻ đã cũ. Trường hợp này mức phí sẽ là 25.000 vnd'
                                    '\n Chú ý: Đối với trường hợp cấp đổi. Thẻ CCCD cũ của công dẫn sẽ được cán bộ thu'
                                    'lại')

async def caplai_CCCD_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Chỉ cấp lại thẻ khi công dân bị mất thẻ và mức phí là 35.000 vnd')

async def lien_quan_CCCD_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Những trường hợp không được cấp thẻ CCCD : '
                                    '\n 1: Khai báo thông tin sai khác so với kho dữ liệu dân cư. VD công dân khai họ tên mẹ :'
                                    'Nguyễn Thị Son nhưng trong kho dữ liệu là Nguyễn Thị Sọn '
                                    '\n 2: Công dân đi khỏi nơi cư trú và bị xoá thông tin trên kho dữ liệu dân cư'
                                    '\n 3: Công dân đi nước ngoài về nhưng nhập cảnh bằng hộ chiếu nước ngoài'
                                    'VD Công dân đi mỹ về nhập cảnh bằng hộ chiếu Mỹ thì sẽ không được cấp CCCD. Bắt buộc phải '
                                    'nhập cảnh bằng hộ chiếu Việt Nam')
    
async def DVC_CCCD_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('/desktop_DVC để xem hướng dẫn trên máy tính'
                                    '\n /mobile_DVC để xem hướng dẫn trên điện thoại')

async def desktop_DVC_CCCD_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('B1: Truy cập vào link https://dichvucong.bocongan.gov.vn/?home=1 ấn vào đăng ký')
    await update.message.reply_photo('./DVC/dk.png')
    await update.message.reply_text('B2: Cửa số mới hiện ra chúng ta chỉ quan tâm tới hai hình thức đăng ký ở khung')
    await update.message.reply_photo('./DVC/1.png')
    await update.message.reply_text('B3: Lưu ý chỉ chọn hình thức thuê bao di động nếu công dân đã đăng ký sim chính chủ với' 
                                    'nhà mạng trước đó.'
                                    'Đối với hình thức đăng ký bằng thuê bao di động chúng ta nhập các trường thông tin '
                                    'tương ứng. Mục CMT/CCCD công dân đăng ký sim chính chủ bằng CMT thì nhập số CMND.'
                                    'Nếu công dân đăng ký sim chính chủ bằng CCCD thì nhập CCCD.'
                                    'Sau khi điền đầy đủ thông tin click vào Đăng ký')
    await update.message.reply_photo('./DVC/2.png')
    await update.message.reply_text('B4: Nhập 6 số OTP được gửi về SDT và ấn Xác nhận')
    await update.message.reply_photo('./DVC/3.png')
    await update.message.reply_text('Nếu thông báo như hình dưới xuất hiện thì chúng ta cần kiểm tra lại SDT đã được đăng ký'
                                    ' chính chủ với nhà mạng hay chưa bằng cách soạn tin nhắn \'tttb\' gửi đến 1414')
    await update.message.reply_photo('./DVC/4.png')
    

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
    app = Application.builder().token(os.getenv('TOKEN')).build()
    
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('CCCD', CCCD_command))
    app.add_handler(CommandHandler('quy_trinh', quyTrinh_command))
    app.add_handler(CommandHandler('phi', phi_command))
    app.add_handler(CommandHandler('capmoi_CCCD', capmoi_CCCD_command))
    app.add_handler(CommandHandler('capdoi_CCCD', capdoi_CCCD_command))
    app.add_handler(CommandHandler('caplai_CCCD', caplai_CCCD_command))
    app.add_handler(CommandHandler('lien_quan', lien_quan_CCCD_command))
    app.add_handler(CommandHandler('desktop_DVC', desktop_DVC_CCCD_command))
    app.add_handler(CommandHandler('DVC', DVC_CCCD_command))

    #Message
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #Error
    app.add_error_handler(error)

    #Polling Bot
    print('Polling .....')
    app.run_polling(poll_interval=3)
