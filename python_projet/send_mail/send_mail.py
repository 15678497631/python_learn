# encoding=utf8
import smtplib

qq_login = '824908000@qq.com'
qq_pwd = 'yumrmqyxvfribdia'


def send_qq_mail(to_mail, msg):
    global qq_login,qq_pwd
    smtp_obj = smtplib.SMTP_SSL("smtp.qq.com", 465)
    try:
        smtp_obj.login(qq_login, qq_pwd)
        smtp_obj.sendmail(qq_login, to_mail, msg.encode("utf-8"))
        print ("发送成功")
    except smtplib.SMTPException as e:
        print("发送失败")
    finally:
        smtp_obj.quit()


if __name__ == "__main__":
    msg = "Subject: bibi,你好呀。\n 这里是lulu的邮件呀！"
    # test(to_qq_mail,msg)
    to_qq_mail = "941412472@qq.com"
    send_qq_mail(to_qq_mail,msg)