import bot


#Dados relacionados ao login
login_with_facebook,email_username,password = bot.user_login_data()

#Dados relacionados ao comentários
comment_post,comments,comments_interval,repeat = bot.coments_data()

#Inicia o driver
bot.start_driver()
if login_with_facebook is 'y':
    bot.login_with_facebook(email_username,password)
else:
    bot.login_with_instagram(email_username,password)

bot.comment(comment_post,comments,comments_interval,repeat)
