# ------------------
# Create a campaign\
# ------------------

# Include the Sendinblue library\
from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

# Instantiate the client\
sib_api_v3_sdk.configuration.api_key['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'] = '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'

api_instance = sib_api_v3_sdk.EmailCampaignsApi()

# Define the campaign settings\
email_campaigns = sib_api_v3_sdk.CreateEmailCampaign(
    name= "Campaign sent via the API", 
    subject= "My subject",
    sender= { "name": "From name", "email": "theo.kobuoe@umuzi.org"},
    type= "classic",

    # Content that will be sent\
    html_content= "Congratulations! You successfully sent this example campaign via the Sendinblue API.",

    # Select the recipients\
    recipients= {"listIds": [2, 7]},

    # Schedule the sending in one hour\
    scheduled_at= "2020-03-13 00:00:01"
)

# Make the call to the client\
try: 
    api_response = api_instance.create_email_campaign(email_campaigns)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailCampaignsApi->create_email_campaign: %s\n" % e)
