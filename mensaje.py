import streamlit as st
from twilio.rest import Client

# Configuración de Twilio
ACCOUNT_SID = 'TU_ACCOUNT_SID'
AUTH_TOKEN = 'TU_AUTH_TOKEN'
FROM_WHATSAPP_NUMBER = 'whatsapp:+14155238886'  # Número de Twilio para WhatsApp

# Crear cliente de Twilio
client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_whatsapp_message(to, message):
    try:
        client.messages.create(
            body=message,
            from_=FROM_WHATSAPP_NUMBER,
            to=f'whatsapp:{to}'
        )
        return "Mensaje enviado con éxito."
    except Exception as e:
        return f"Error al enviar el mensaje: {e}"

# Interfaz de Streamlit
st.title('Enviar mensajes a WhatsApp')

to = st.text_input('Número de WhatsApp del destinatario (con código de país, ej. +5215512345678):')
message = st.text_area('Mensaje:')

if st.button('Enviar'):
    result = send_whatsapp_message(to, message)
    st.write(result)

