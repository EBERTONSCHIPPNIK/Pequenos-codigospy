import win32com.client as win32

#criar a integração com o outlook
outlook = win32.dispatch('outlook.application')

#configurar as informações do seu e-mail
email.to = "adicione seu email"
email.subject = "Email automatico do Python"
email.htmlbody = """

<p>OLÁ BETO, AQUI É O CODIGO PYTHON<p/>

<p>Abs,<p/>
"""

email.send()

print ('E-mail Enviado')