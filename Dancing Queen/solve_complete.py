#!/usr/bin/env python3

from chacha20_c76e2a43164af8b6ecb0e145415ab931 import ChaCha20, xor, bytes_to_words, words_to_bytes

def rotate(x, n):
    return ((x << n) & 0xffffffff) | ((x >> (32 - n)) & 0xffffffff)

def rotate_right(x, n):
    return ((x >> n) & 0xffffffff) | ((x << (32 - n)) & 0xffffffff)

def word(x):
    return x % (2 ** 32)

def inverse_quarter_round(x, a, b, c, d):
    x[b] = rotate_right(x[b], 7); x[b] ^= x[c]; x[c] = word(x[c] - x[d])
    x[d] = rotate_right(x[d], 8); x[d] ^= x[a]; x[a] = word(x[a] - x[b])
    x[b] = rotate_right(x[b], 12); x[b] ^= x[c]; x[c] = word(x[c] - x[d])
    x[d] = rotate_right(x[d], 16); x[d] ^= x[a]; x[a] = word(x[a] - x[b])

def inverse_inner_block(state):
    inverse_quarter_round(state, 3, 4, 9, 14)
    inverse_quarter_round(state, 2, 7, 8, 13)
    inverse_quarter_round(state, 1, 6, 11, 12)
    inverse_quarter_round(state, 0, 5, 10, 15)
    inverse_quarter_round(state, 3, 7, 11, 15)
    inverse_quarter_round(state, 2, 6, 10, 14)
    inverse_quarter_round(state, 1, 5, 9, 13)
    inverse_quarter_round(state, 0, 4, 8, 12)

def recover_key(msg, msg_enc, iv):
    keystream = xor(msg[:64], msg_enc[:64])
    state = bytes_to_words(keystream)
    
    for _ in range(10):
        inverse_inner_block(state)
    
    return words_to_bytes(state[4:12])

def main():
    msg = b'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula.'
    iv1 = bytes.fromhex('e42758d6d218013ea63e3c49')
    iv2 = bytes.fromhex('a99f9a7d097daabd2aa2a235')
    msg_enc = bytes.fromhex('f3afbada8237af6e94c7d2065ee0e221a1748b8c7b11105a8cc8a1c74253611c94fe7ea6fa8a9133505772ef619f04b05d2e2b0732cc483df72ccebb09a92c211ef5a52628094f09a30fc692cb25647f')
    flag_enc = bytes.fromhex('b6327e9a2253034096344ad5694a2040b114753e24ea9c1af17c10263281fb0fe622b32732')
    
    key = recover_key(msg, msg_enc, iv1)
    flag = ChaCha20().decrypt(flag_enc, key, iv2)
    
    print(flag.decode())

if __name__ == '__main__':
    main()
