import string

class CaesarCipher:
    def __init__(self, key):
        self.key = key
        self.eng_lower = string.ascii_lowercase  
        self.eng_upper = string.ascii_uppercase 
        self.ukr_lower = 'абвгґдеєжзийіїклмнопрстуфхцчшщьюя' 
        self.ukr_upper = 'АБВГҐДЕЄЖЗИЙІЇКЛМНОПРСТУФХЦЧШЩЬЮЯ' 


    def validate_key(self):
        if not isinstance(self.key, int):
            raise ValueError("Ключ має бути числом.")
        if self.key < 1:
            raise ValueError("Ключ має бути додатнім числом більше 0.")
    

    def validate_data(self, data):
        if not isinstance(data, str):
            raise ValueError("Дані мають бути рядком.")
        if not data:
            raise ValueError("Дані не можуть бути порожніми.")


    def encrypt(self, data):
        self.validate_key()  
        self.validate_data(data) 
        
        encrypted_text = ''.join([self._key_char(c, self.key) for c in data])
        return encrypted_text


    def decrypt(self, data):
        self.validate_key()  
        self.validate_data(data)  
        
        decrypted_text = ''.join([self._key_char(c, -self.key) for c in data])
        return decrypted_text
    

    def brute_force_attack(self, data):
        self.validate_data(data) 
        
        possible_decryptions = []
        max_key = max(len(self.eng_lower), len(self.ukr_lower))

        for key in range(1, max_key):
            decrypted_text = ''.join([self._key_char(c, -key) for c in data])
            possible_decryptions.append((key, decrypted_text))
        
        return possible_decryptions

 
    def _key_char(self, c, key):
        if c in self.eng_lower:
            return self._key_within_alphabet(c, self.eng_lower, key)
        elif c in self.eng_upper:
            return self._key_within_alphabet(c, self.eng_upper, key)
        elif c in self.ukr_lower:
            return self._key_within_alphabet(c, self.ukr_lower, key)
        elif c in self.ukr_upper:
            return self._key_within_alphabet(c, self.ukr_upper, key)
        else:
            return c  


    def _key_within_alphabet(self, char, alphabet, key):
        index = alphabet.index(char)
        return alphabet[(index + key) % len(alphabet)]

