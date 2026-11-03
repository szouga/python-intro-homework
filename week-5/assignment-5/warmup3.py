username = input("Is your name special? Let's see type it here 👉 ")
names = [
    "Pegasus",
    "Anubis",
    "Thoth",
    "Ma'at",
    "Apollo",
    "Hephaestus",
    "Hermes",
    "Medusa",
    "Sphinx"
]

username = username.title().strip()
index = -1
# range(len(names)) == enumerate(names)
for i, name in enumerate(names):
    if name == username:
        found = True
        index = i
        break
    else:
        continue
if index != -1:
    print(f"Found {username} at index {index}\nYour name, {username}, is special!\nYou're named after an Egyptian/Greek mythological being")
else:
    print(f"{username} was not found in the list\n  ...Maybe try another name?")