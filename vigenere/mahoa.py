LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def mahoa(message, key):
	ciphertext = []
	keyIndex = 0
	key = key.upper()
# duyệt từng kí tự trong thông điệp(bản rõ)
	for symbol in message:
		if symbol.isalpha():
			num = LETTERS.find(symbol.upper())
			num += LETTERS.find(key[keyIndex])
			num %= len(LETTERS)

			if symbol.isupper():
				ciphertext.append(LETTERS[num])
			elif symbol.islower():
				ciphertext.append(LETTERS[num].lower())
			keyIndex += 1
			if keyIndex == len(key):
					keyIndex = 0
		else:
			# Giữ nguyên các ký tự khác (khoảng trắng, dấu câu, số, ...)
			ciphertext += symbol

	return ''.join(ciphertext)