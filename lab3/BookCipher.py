class BookCipher:
    def __init__(self, matrix):
        self.matrix = matrix # г' є ї ф ш
        self.ukr_lower_alphabet = 'абвгґдеєжзийіїклмнопрстуфхцчшщьюя' 
        self.ukr_upper_alphabet = 'АБВГҐДЕЄЖЗИЙІЇКЛМНОПРСТУФХЦЧШЩЬЮЯ'
        self.unwanted_chars = 'ґєїфш'

    def encrypt(self, data):
        encrypted_text = []
        data = ''.join([char for char in data if char not in self.unwanted_chars])

        for char in data:
            lower_char = char.lower()
            row, col = self._find_char_in_matrix(lower_char)
            if row is not None and col is not None:
                encrypted_text.append(f"{row+1},{col+1}")
            else:
                encrypted_text.append(char) 

        return ' '.join(encrypted_text)

    def decrypt(self, data):
        decrypted_text = []
        data_pairs = data.split()
        
        for pair in data_pairs:
            if ',' in pair and len(pair.split(',')) == 2:  
                try:
                    row, col = map(int, pair.split(','))
                    decrypted_text.append(self.matrix[row-1][col-1])
                except (ValueError, IndexError): 
                    decrypted_text.append(pair)
            else:
                decrypted_text.append(pair) 

        return ''.join(decrypted_text)

    def _find_char_in_matrix(self, char):
        for i, row in enumerate(self.matrix):
            if char in row:
                return i, row.index(char)
        return None, None  
    