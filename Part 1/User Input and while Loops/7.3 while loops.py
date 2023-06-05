current_num = 1
while current_num <= 5:
    print(current_num)
    current_num += 1

prompt = '\nTell me something, and I will repeat it back to you:'
prompt += "\nEnter 'quit' to end the program."

message = ''
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)