message = 'Hello, world!'
print(len(message))

# Opening a txt file in write mode
with open('message.txt', 'w') as file:

    # Writing the message to the file
    file.write(message)

    # Closing the file
    file.close()

    