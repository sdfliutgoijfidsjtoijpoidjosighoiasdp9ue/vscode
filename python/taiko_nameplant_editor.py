fileName = "1P.json"
playerName_def = '"1P"'

print("What's your player name?")

playerName = input("Type: ")

with open(r'1P.json', 'r') as file:

    data = file.read()
    jls_extract_var = playerName_def
    data = data.replace('"1"' , playerName)
with open(r'1P.json', 'w') as file:
  
    # Writing the replaced data in our
    # text file
    file.write(data)