plain_text = "Hello my name is Ollie. I am allergic to everything"
encrypted_text = []

for i in range(5):
	for a in range(11):
		
		if a == 10 and i!= 0:
			print ("Invalid index")
		else:
			encrypted_letter = i+ 5*a
			encrypted_text.append(plain_text[encrypted_letter])
		
print (encrypted_text)
print ("Length of encrypted text: " + str(len(plain_text)))