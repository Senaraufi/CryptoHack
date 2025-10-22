# Lemur XOR Challenge

## Challenge Description

Two images have been encrypted by XORing them with the same secret key. The challenge requires performing a visual XOR between the RGB bytes of the two images to reveal the hidden content.

**Given files:**
- `flag_7ae18c704272532658c10b5faad06d74.png` - First encrypted image
- `lemur_ed66878c338e662d3473f0d98eedbd0d.png` - Second encrypted image


## Solution

See `solve.py` for the complete solution.


## Result

The XOR operation reveals both images combined, showing:
- A lemur image
- The flag text overlaid on the image

**Flag:** `crypto{X0Rly_n0t!}`

