#Guest list
guests = ['warm', 'earth', 'khawtoo', 'khawpun', 'tintin']
for guest in guests:
    print("Hey " + guest.title() + ", Do you want to come to dinner with me?")
print("")

#chaning guest list
print(guests[0].title() + " cannot come to dinner with me.")
guests.remove("warm")
guests.append("Job")

for guest in guests:
    print("Hey " + guest.title() + ", Do you want to come to dinner with me?")
print("")
print(guests)
guests.insert(0, 'guide')
guests.insert(3, 'SKK')
guests.append('Jack')
print(guests)
for guest in guests:
    print("Hey " + guest.title() + ", Do you want to come to dinner with me?")

#Shrinking Guest List
#the dinner only for two guest
print("Oh wait, i can only invite only Variables and Simple Data Types people for dinner !\n")

for guest in guests:
        while len(guests) != 2 :
             guests_poped = guests.pop()
             print("Hey " + guests_poped.title() + ", am sorry to say that i will not be able to invite you to dinner. ")

for guest in guests:
    print("Hey " + guest.title() + ", Do you still want to go dinner with me?")

del guests[0:]

print(guests)

