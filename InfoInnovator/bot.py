# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount

def process_msg(message):
    return 'Hello, World!'


from botbuilder.core import ActivityHandler, MessageFactory, TurnContext

class InfoInnovator(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        # Get the incoming message text
        incoming_message = turn_context.activity.text

        # Process the message
        response = process_msg(incoming_message)

        # Send 'Hello, World!' as a response
        await turn_context.send_activity(MessageFactory.text(response))

