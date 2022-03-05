def encode(message, key):
    encode_message = []
    for x in message:
        encoded = chr(ord(x) + key)
        encode_message.append(encoded)
    encode_message.remove(encode_message[-1])
    encode_message = ''.join(encode_message)
    return encode_message