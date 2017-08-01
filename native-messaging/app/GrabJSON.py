#!/usr/bin/env python

import sys
import json
import struct

#fw = open('sample.txt', 'w')

def is_json(a):
    #Will check if the msg received from the browser is a valid json or not...
    try:
        json_object = json.loads(a)
    except ValueError:
        return False
    return True



try:
    # Python 3.x version
    # Read a message from stdin and decode it.
    def getMessage():
        rawLength = sys.stdin.buffer.read(4)
        if len(rawLength) == 0:
            sys.exit(0)
        messageLength = struct.unpack('@I', rawLength)[0]
        message = sys.stdin.buffer.read(messageLength).decode('utf-8')
        return json.loads(message)

    # Encode a message for transmission,
    # given its content.
    def encodeMessage(messageContent):
        encodedContent = json.dumps(messageContent).encode('utf-8')
        encodedLength = struct.pack('@I', len(encodedContent))
        return {'length': encodedLength, 'content': encodedContent}

    # Send an encoded message to stdout
    def sendMessage(encodedMessage):
        sys.stdout.buffer.write(encodedMessage['length'])
        sys.stdout.buffer.write(encodedMessage['content'])
        sys.stdout.buffer.flush()

    while True:
        receivedMessage = getMessage()
        strjson = receivedMessage
        isvalid = is_json(strjson)
        if (isvalid) :
            msg_to_send = "d8cf97594449bb27baa83b2314de77f946138171576f10c7cb26aa98f29439b4ff813bec5d0467faaf1abd84d479e5339246e7e3fd8b814b412bfe39c965b1dc"
            sendMessage(encodeMessage(msg_to_send))
        else :
            sendMessage(encodeMessage("The json data received by native app was invalid"))    
except AttributeError:
    # Python 2.x version (if sys.stdin.buffer is not defined)
    # Read a message from stdin and decode it.
    def getMessage():
        rawLength = sys.stdin.read(4)
        if len(rawLength) == 0:
            sys.exit(0)
        messageLength = struct.unpack('@I', rawLength)[0]
        message = sys.stdin.read(messageLength)
        return json.loads(message)

    # Encode a message for transmission,
    # given its content.
    def encodeMessage(messageContent):
        encodedContent = json.dumps(messageContent)
        encodedLength = struct.pack('@I', len(encodedContent))
        return {'length': encodedLength, 'content': encodedContent}

    # Send an encoded message to stdout
    def sendMessage(encodedMessage):
        sys.stdout.write(encodedMessage['length'])
        sys.stdout.write(encodedMessage['content'])
        sys.stdout.flush()

    while True:
        receivedMessage = getMessage()
        strjson = receivedMessage
        isvalid = is_json(strjson)
        if (isvalid) :
            msg_to_send = "d8cf97594449bb27baa83b2314de77f946138171576f10c7cb26aa98f29439b4ff813bec5d0467faaf1abd84d479e5339246e7e3fd8b814b412bfe39c965b1dc"
            sendMessage(encodeMessage(msg_to_send))
        else :
            sendMessage(encodeMessage("The json data received by native app was invalid"))
            
            
            
            
            
            
            