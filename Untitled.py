#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install twilio


# In[1]:


from twilio.rest import Client
# Your Twilio account SID and authentication token
account_sid = 'AC6f86f1b155697f9507dc2a97c492fd48'
auth_token = '5f7687e71b1910e2751f53ff3f11aaab'

# Create a Twilio client
client = Client('AC6f86f1b155697f9507dc2a97c492fd48','5f7687e71b1910e2751f53ff3f11aaab' )

# Define the recipient's phone number and the message you want to send
recipient_phone_number = '+917905131362'  # Replace with the recipient's phone number
message_body = 'Hello, this is an automated message from your Python script.'

try:
    # Send the message
    message = client.messages.create(
        body=message_body,
        from_='+12562911447',  # Your Twilio phone number (must be purchased on Twilio)
        to=recipient_phone_number
    )
    print(f'Message sent with SID: {message.sid}')
except Exception as e:
    print(f'Error: {str(e)}')


# In[ ]:




