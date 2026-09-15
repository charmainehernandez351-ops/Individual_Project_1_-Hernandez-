import os 
name ="Charmaine Hernandez"

file_name = input("Enter the file name (including .txt extension): ")

if os.path.exists(file_name):
	print(f"\n--Contents of {file_name}---")
	with open(file_name,"r") as file:
		print(file.read())
	print("----------------\n")
else:
	print(f"File '{file_name}' does not exist. A new file will be created.")

user_mess = input("Enter your message: ")
formatted_mess = f"[{name}]: {user_mess}\n"

with open(file_name,"a") as file:
	file.write(formatted_mess)
print(f" Message has been saved to {file_name}!")



