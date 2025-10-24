word = None

while True:
	word = input("Enter a word to see if it is a palindrome or not (or press Enter to quit): ").strip().lower()

	if word == "":
		break
	if word == word[::-1]:
		print(f"'{word}' is a palindrome.")
	else:
		print(f"'{word}' is not a palindrome.")