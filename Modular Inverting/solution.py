#!/usr/bin/env python3

"""
Challenge: Modular Inverting
Category: Modular Arithmetic
Description: Find the multiplicative inverse of 3 modulo 13
"""

def modular_inverse_fermat(a, p):
    """
    Find modular inverse using Fermat's Little Theorem.
    For prime p: a^(p-1) ≡ 1 (mod p)
    Therefore: a^(p-2) ≡ a^(-1) (mod p)
    """
    return pow(a, p - 2, p)

def modular_inverse_extended_gcd(a, m):
    """
    Find modular inverse using Extended Euclidean Algorithm.
    This works for any modulus (not just prime).
    """
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
    
    gcd, x, _ = extended_gcd(a % m, m)
    if gcd != 1:
        raise ValueError(f"Modular inverse does not exist (gcd({a}, {m}) = {gcd})")
    return (x % m + m) % m

def solve():
    a = 3
    p = 13
    
    print(f"Finding the multiplicative inverse of {a} modulo {p}")
    print(f"We need to find d such that {a} * d ≡ 1 (mod {p})")
    print()
    
    # Method 1: Fermat's Little Theorem (works for prime modulus)
    print("Method 1: Fermat's Little Theorem")
    print(f"Since {p} is prime, we can use: d = {a}^({p}-2) mod {p}")
    print(f"d = {a}^{p-2} mod {p}")
    
    d_fermat = modular_inverse_fermat(a, p)
    print(f"d = {d_fermat}")
    print()
    
    # Verify
    print("Verification:")
    result = (a * d_fermat) % p
    print(f"{a} * {d_fermat} = {a * d_fermat} ≡ {result} (mod {p})")
    print()
    
    # Method 2: Extended Euclidean Algorithm (works for any coprime modulus)
    print("Method 2: Extended Euclidean Algorithm")
    d_egcd = modular_inverse_extended_gcd(a, p)
    print(f"d = {d_egcd}")
    print()
    
    # Python's built-in pow function can also compute modular inverse
    print("Method 3: Python's pow(a, -1, p) [Python 3.8+]")
    d_builtin = pow(a, -1, p)
    print(f"d = {d_builtin}")
    print()
    
    print("="*50)
    print(f"ANSWER: {d_fermat}")
    print("="*50)
    
    return d_fermat

if __name__ == "__main__":
    answer = solve()
