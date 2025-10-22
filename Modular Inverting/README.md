# Modular Inverting

## Challenge Description

As we've seen, we can work within a finite field F_p, adding and multiplying elements, and always obtain another element of the field.

For all elements `g` in the field, there exists a unique integer `d` such that `g·d ≡ 1 (mod p)`.

This is the multiplicative inverse of `g`.

**Example:** `7·8 = 56 ≡ 1 (mod 11)`

**Question:** What is the inverse element `d = 3^(-1)` such that `3·d ≡ 1 (mod 13)`?

**Hint:** Think about the little theorem we just worked with. How does this help you find the inverse of an element?

## Solution Approach

The hint refers to **Fermat's Little Theorem**.


### Application to This Problem

To find `3^(-1) mod 13`:

```
d = 3^(13-2) mod 13
d = 3^11 mod 13
d = 177147 mod 13
d = 9
```

### Verification

```
3 × 9 = 27 ≡ 1 (mod 13) ✓
```

## Result

```
9
```
