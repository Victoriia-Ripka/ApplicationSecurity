import random

class KnapsackCipher:
    def __init__(self, n=8):
        self.n = n # size of the super-increasing sequence
        self.public_key = []
        self.private_key = []
        self.q = 0 # modulus
        self.r = 0 # random number

        # Generate keys upon initialization
        self.generate_keys()


    def generate_super_increasing_sequence(self):
        sequence = [random.randint(1, 100)]
        while len(sequence) < self.n:
            next_element = sum(sequence) + random.randint(1, 10)
            sequence.append(next_element)
        return sequence


    def generate_keys(self):
        super_increasing_sequence = self.generate_super_increasing_sequence()
        self.q = sum(super_increasing_sequence) + random.randint(1, 10)  # Modulus
        self.r = random.randint(2, self.q - 1)

        # Ensure that r and q are coprime
        while self.gcd(self.r, self.q) != 1:
            self.r = random.randint(2, self.q - 1)

        # Generate public key
        self.public_key = [(self.r * element) % self.q for element in super_increasing_sequence]
        self.private_key = super_increasing_sequence  # Store the private key as the super-increasing sequence


    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a


    def knapsack_encrypt(self, plaintext):
        encrypted_message = sum(self.public_key[i] for i in range(len(plaintext)) if plaintext[i] == '1')
        return encrypted_message


    def knapsack_decrypt(self, ciphertext) :
        r_inverse = pow(self.r, -1, self.q) 
        decrypted_message = ''
        total = (ciphertext * r_inverse) % self.q
        
        for element in reversed(self.private_key):
            if total >= element:
                decrypted_message = '1' + decrypted_message
                total -= element
            else:
                decrypted_message = '0' + decrypted_message

        return decrypted_message