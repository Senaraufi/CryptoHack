# Dancing Queen Challenge

## Challenge Description

"I don't trust other developers so I made my own ChaCha20 implementation. In this way, I am sure you will never be able to read my flag!"

**Given files:**
- `chacha20.py` - Custom ChaCha20 implementation
- `output.txt` - Encrypted message and flag with different IVs

## Vulnerability Analysis

The custom ChaCha20 implementation has a cryptographic flaw on line 62:

```python
c += xor(m[i:i+64], words_to_bytes(self._state))
```


## Implementation

See `solve_complete.py` for the full solution with:
- `inverse_quarter_round()` - Inverts a single quarter-round
- `inverse_inner_block()` - Inverts a double-round (8 quarter-rounds)
- `recover_key()` - Recovers the key from known plaintext
- Complete decryption of the flag

```

## Result

```
crypto{M1x1n6_r0und5_4r3_1nv3r71bl3!}
```