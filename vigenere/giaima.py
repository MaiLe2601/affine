LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# hàm giải mã
def giaima(message, key):
	plaintext = [] 
	keyIndex = 0 
	key = key.upper() 
# duyệt từng kí tự trong thông điệp(bản mã)
	for symbol in message:
		if symbol.isalpha():
			num = LETTERS.find(symbol.upper()) 
			num -= LETTERS.find(key[keyIndex]) 
			num %= len(LETTERS)

			if symbol.isupper(): 
				plaintext.append(LETTERS[num]) 
			elif symbol.islower(): 
				plaintext.append(LETTERS[num].lower()) 

			keyIndex += 1
			if keyIndex == len(key): 
					keyIndex = 0 
		else:
			# Giữ nguyên các ký tự khác (khoảng trắng, dấu câu, số, ...)
			plaintext += symbol
		
	return ''.join(plaintext)