from collections import deque
from itertools import repeat


# Trivium Cipher class
class Trivium:
    def __init__(self, key, iv):
        self.state = None
        self.key = key
        self.iv = iv
        # Ensure key and IV are 80 bits long
        assert len(self.key) == 80, "Key must be 80 bits."
        assert len(self.iv) == 80, "IV must be 80 bits."
        # Initialize state with Key, IV, and other bits
        # init_state = self.key + [0] * 13        # (K1...K80;    0...0)
        init_state = list(map(int, list(self.key)))
        init_state += list(repeat(0, 13))
        # init_state += self.iv + [0] * 4         # (IV1...IV80;  0...0)
        init_state += list(map(int, list(self.iv)))
        init_state += list(repeat(0, 4))
        # init_state += [0] * 108 + [1, 1, 1]     # (0...0;   1;  1;  1)
        init_state += list(repeat(0, 108))
        init_state += list([1, 1, 1])
        self.state = deque(init_state)
        
        # Perform 4 * 288 clock cycles for initialization
        for _ in range(4 * 288):
            self.gen_keystream()
    
    
    def gen_keystream(self):
        # Extract values from the current state
        t_1 = self.state[65] ^ self.state[92]
        t_2 = self.state[161] ^ self.state[176]
        t_3 = self.state[242] ^ self.state[287]
        
        # Output bit
        z = t_1 ^ t_2 ^ t_3
        
        # Update internal state with new t_1, t_2, t_3 values
        t_1 = t_1 ^ (self.state[90] & self.state[91]) ^ self.state[170]
        t_2 = t_2 ^ (self.state[174] & self.state[175]) ^ self.state[263]
        t_3 = t_3 ^ (self.state[285] & self.state[286]) ^ self.state[68]
        
        # Rotate state and insert new values
        self.state.rotate(1)
        self.state[0] = t_3
        self.state[93] = t_1
        self.state[177] = t_2
        
        return z
    
    
    def keystream(self, msglen):
        keystream = []
        
        for _ in range(msglen):
            keystream.append(self.gen_keystream())
        
        return keystream


# Helper functions
def _hex_to_bytes(s):
    _allbytes = dict([("%02X" % i, i) for i in range(256)])
    
    return [_allbytes[s[i:i+2].upper()] for i in range(0, len(s), 2)]


def bits_to_hex(b):
    return "".join(["%02X" % sum([b[i + j] << j for j in range(8)]) for i in range(0, len(b), 8)])


def hex_to_bits(s):
    return [(b >> i) & 1 for b in _hex_to_bytes(s) for i in range(8)]

def clean_hex_input(hex_str):
    """Remove '0x' and spaces from the hex string."""
    return hex_str.replace("0x", "").replace(" ", "")


def format_hex_output(hex_str):
    """Add '0x' and format the hex string."""
    return "0x" + " ".join([hex_str[i:i+4] for i in range(0, len(hex_str), 4)])