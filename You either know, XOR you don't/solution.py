#!/usr/bin/env python3

def xor_bytes(data, key):
    """XOR data with a repeating key"""
    return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])

def solve():
    # The encrypted flag in hex
    ciphertext_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
    
    # Convert hex to bytes
    ciphertext = bytes.fromhex(ciphertext_hex)
    
    print(f"Ciphertext length: {len(ciphertext)} bytes")
    
    # Known plaintext: flags start with "crypto{"
    known_plaintext = b"crypto{"
    
    # The repeating pattern at distance 16 suggests key length is 16
    # We know: plaintext[0:7] = "crypto{"
    # We can deduce: plaintext[9:25] repeats at plaintext[25:41]
    # This means the same key bytes encrypted the same plaintext
    
    # Let's assume the key is "myXORkey" repeated (common pattern)
    # Or we can try to recover it byte by byte
    
    key_length = 1
    # Start with what we know
    key = bytearray(xor_bytes(ciphertext[:7], known_plaintext))
    
    print(f"Known key bytes (from 'crypto{{'): {key.decode('ascii', errors='replace')}")
    
    # The pattern repeats at position 9 and 25 (distance 16)
    # This means: plaintext[9] XOR key[9] = ciphertext[9]
    #             plaintext[25] XOR key[9] = ciphertext[25]
    # Since ciphertext[9:16] has a repeating pattern with ciphertext[25:32]
    # And key repeats every 16 bytes, plaintext[9:16] should equal plaintext[25:32]
    
    # Let's try key length of 1 (single byte key - unlikely but let's check)
    # Then try common patterns
    
    # Most likely: the key is "myXORkey" (8 bytes) or similar
    # Let's try to extend the key intelligently
    
    # Try assuming the flag contains common words
    # Flags often contain: "you", "know", "xor", etc.
    
    # Let's try key = "myXORkey" (8 bytes)
    test_key = b"myXORkey"
    plaintext = xor_bytes(ciphertext, test_key)
    try:
        decoded = plaintext.decode('ascii')
        print(f"\nTrying key 'myXORkey':")
        print(f"  Result: {decoded}")
        if decoded.startswith('crypto{') and decoded.endswith('}'):
            return decoded
    except:
        pass
    
    # If that doesn't work, try to recover the full key
    # by assuming the plaintext makes sense
    print("\nTrying to recover full key...")
    
    # We know positions 9-15 and 25-31 have the same ciphertext pattern
    # repeating with distance 16, so key length is likely 16 or a divisor
    
    for key_len in [1, 2, 4, 8, 16]:
        # Build key from known plaintext
        key = bytearray(key_len)
        for i in range(min(7, key_len)):
            key[i] = ciphertext[i] ^ known_plaintext[i]
        
        # For remaining key bytes, try to infer from repeating patterns
        if key_len > 7:
            # Use the repeating pattern: ciphertext[9:16] repeats at [25:32]
            # If key repeats every key_len bytes, we can deduce more
            for i in range(7, key_len):
                if i < len(ciphertext):
                    # Try common characters for position i
                    for guess_char in b'_{}abcdefghijklmnopqrstuvwxyz0123456789':
                        key[i] = ciphertext[i] ^ guess_char
                        test_plaintext = xor_bytes(ciphertext, bytes(key))
                        try:
                            test_decoded = test_plaintext.decode('ascii')
                            if all(32 <= ord(c) <= 126 for c in test_decoded):
                                # This might work, continue
                                break
                        except:
                            pass
        
        plaintext = xor_bytes(ciphertext, bytes(key))
        try:
            decoded = plaintext.decode('ascii')
            if decoded.startswith('crypto{') and all(32 <= ord(c) <= 126 for c in decoded):
                print(f"\nKey length {key_len}:")
                print(f"  Key: {bytes(key).decode('ascii', errors='replace')}")
                print(f"  Plaintext: {decoded}")
                if decoded.endswith('}'):
                    return decoded
        except:
            pass
    
    return None

if __name__ == "__main__":
    flag = solve()
    print(f"\nFinal answer: {flag}")
