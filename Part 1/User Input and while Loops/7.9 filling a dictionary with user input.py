#set flag
polling_active = True
responses = {}

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to clib someday? ")

    #store response to dictionary
    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) \n")
    if repeat.lower() == 'no':
        polling_active = False

#polling is now completed. show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name.title() + " Would like to climb " + response.title() + '.')




