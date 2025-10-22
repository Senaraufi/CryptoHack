# You either know, XOR you don't

**Category:** XOR  
**Challenge:** I've encrypted the flag with my secret key, you'll never be able to guess it.

Remember the flag format and how it might help you in this challenge!

## Challenge Description

Given ciphertext (hex):
```
0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104
```

## Solution Approach

This is a **known-plaintext attack** on a repeating-key XOR cipher.

### Key Insights:

1. **Known Plaintext**: All CryptoHack flags start with `crypto{`, giving us 7 bytes of known plaintext
2. **Key Recovery**: XOR the known plaintext with the first 7 bytes of ciphertext to recover part of the key
3. **Pattern Analysis**: The ciphertext shows repeating patterns at distance 16, suggesting the key repeats
4. **Key Guessing**: With `myXORke` recovered, the full key is likely `myXORkey` (8 bytes)

### Attack Steps:

```python
# Known: plaintext[0:7] = "crypto{"
# Ciphertext[0:7] = 0e0b213f26041e

# Recover key:
key[0:7] = ciphertext[0:7] XOR "crypto{" = "myXORke"

# Guess complete key: "myXORkey"
# Decrypt: plaintext = ciphertext XOR (repeating "myXORkey")
```

## Result

```
crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}
```

## Key Concepts

- **Repeating-key XOR cipher**: Simple but weak encryption where a short key is repeated
- **Known-plaintext attack**: Using known parts of plaintext to recover the key
- **Pattern analysis**: Repeating patterns in ciphertext reveal key length
- **Leetspeak**: "If you know enough, you know it all"
