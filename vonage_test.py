import vonage

client = vonage.Client(key="4388a5ed", secret="WQEaD3BYses5ic8p")
sms = vonage.Sms(client)

responseData = sms.send_message(
    {
        "from": "Vonage APIs",
        "to": "918799726101",
        "text": "Call ma error a raha hai pata nhi kyu.",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {
          responseData['messages'][0]['error-text']}")
