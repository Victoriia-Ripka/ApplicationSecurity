import string

class TrithemiusCipher:
    def __init__(self, key):
        self.key_type, self.key_value = key
        self.eng_lower = string.ascii_lowercase  
        self.eng_upper = string.ascii_uppercase 
        self.ukr_lower = 'абвгґдеєжзийіїклмнопрстуфхцчшщьюя' 
        self.ukr_upper = 'АБВГҐДЕЄЖЗИЙІЇКЛМНОПРСТУФХЦЧШЩЬЮЯ'
        self.validation_cases = {
            "3D": self._validate_3d,
            "2D": self._validate_2d,
            "phrase": self._validate_phrase
        } 


    def validate_key(self):
        if self.key_type in self.validation_cases:
            self.validation_cases[self.key_type]()
        else:
            raise ValueError("Невідомий тип ключа.")


    def _validate_3d(self):
        if len(self.key_value) != 3 or not all(isinstance(i, int) for i in self.key_value):
            raise ValueError("Ключ для тривимірного вектора має складатися з трьох цілих чисел.")
        if any(i < 1 for i in self.key_value):
            raise ValueError("Ключові значення в тривимірному векторі мають бути додатніми числами.")


    def _validate_2d(self):
        if len(self.key_value) != 2 or not all(isinstance(i, int) for i in self.key_value):
            raise ValueError("Ключ для двовимірного вектора має складатися з двох цілих чисел.")
        if any(i < 1 for i in self.key_value):
            raise ValueError("Ключові значення в двовимірному векторі мають бути додатніми числами.")


    def _validate_phrase(self):
        if not isinstance(self.key_value[0], str) or not self.key_value[0]:
            raise ValueError("Ключ-фраза має бути непорожнім рядком.")
            

    def validate_data(self, data):
        if not isinstance(data, str):
            raise ValueError("Дані мають бути рядком.")
        if not data:
            raise ValueError("Дані не можуть бути порожніми.")


    def encrypt(self, data):
        self.validate_key()  
        self.validate_data(data) 
        
        encrypted_text = ''.join([self._key_char(c, i, self.key_type, self.key_value) for  i, c in enumerate(data)])
        return encrypted_text


    def decrypt(self, data):
        self.validate_key()  
        self.validate_data(data) 

        decrypted_text = ''.join([self._decrypt_key_char(c, i, self.key_type, self.key_value) for i, c in enumerate(data)])
        return decrypted_text
    

    def _key_char(self, c, i, key_type, key_value):
        if c in self.eng_lower:
            key = self._set_key(key_type, key_value, i, len(self.eng_lower)) 
            return self._key_within_alphabet(c, self.eng_lower, key)
        elif c in self.eng_upper:
            key = self._set_key(key_type, key_value, i, len(self.eng_upper))
            return self._key_within_alphabet(c, self.eng_upper, key)
        elif c in self.ukr_lower:
            key = self._set_key(key_type, key_value, i, len(self.ukr_lower)) 
            return self._key_within_alphabet(c, self.ukr_lower, key)
        elif c in self.ukr_upper:
            key = self._set_key(key_type, key_value, i, len(self.ukr_upper))
            return self._key_within_alphabet(c, self.ukr_upper, key)
        else:
            return c 
        

    def _decrypt_key_char(self, c, i, key_type, key_value):
        if c in self.eng_lower:
            key = self._set_key(key_type, key_value, i, len(self.eng_lower))
            return self._d_key_within_alphabet(c, self.eng_lower, -key)  
        elif c in self.eng_upper:
            key = self._set_key(key_type, key_value, i, len(self.eng_upper))
            return self._d_key_within_alphabet(c, self.eng_upper, -key)
        elif c in self.ukr_lower:
            key = self._set_key(key_type, key_value, i, len(self.ukr_lower))
            return self._d_key_within_alphabet(c, self.ukr_lower, -key)
        elif c in self.ukr_upper:
            key = self._set_key(key_type, key_value, i, len(self.ukr_upper))
            return self._d_key_within_alphabet(c, self.ukr_upper, -key)
        else:
            return c  
            
    
    def _set_key(self, key_type, key_value, position, alphabet_length):
        if key_type == "2D":
            a, b = key_value
            key = (a * position + b) % alphabet_length 
        elif key_type == "3D":
            a, b, c = key_value
            key = (a*a + b*position + c) % alphabet_length
        elif key_type == "phrase":
            phrase = key_value[0]
            key = ord(phrase[position % len(phrase)]) % alphabet_length
        return key


    def _key_within_alphabet(self, char, alphabet, key):
        index = alphabet.index(char)
        return alphabet[(index + key) % len(alphabet)]
    

    def _d_key_within_alphabet(self, char, alphabet, key):
        index = alphabet.index(char)
        return alphabet[(index + len(alphabet) - abs(key)) % len(alphabet)]