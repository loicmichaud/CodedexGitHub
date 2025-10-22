sent_message = 'Hey there! This is a secret message.'

with open('sent_message.txt', 'w') as file:
  file.write(sent_message)

with open('sent_message.txt', 'r+') as file:
    # Read the sent message from the file
    original_message = file.read()
    print(original_message)

    # Move the cursor to the beginning of the file
    file.seek(0)
    unsent_message = 'This message has been unsent.'
    file.truncate(len(unsent_message))
    file.write(unsent_message)
    file.seek(0)
    content = file.read()
    print(content)

# Modify the message to simulate unsending
