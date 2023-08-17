# Cyberpunk Cafe

> This trend of restaurants getting rid of hard copies of their menus is kinda annoying, but this new cyberpunk-themed cafe is taking it a bit too far. Check out what they gave me.

Didapat sebuah file txt berisi angka 0 dan 1 dengan total karakter sebanyak 1681. Ya bisa jadi ini merupakan sebuah QR code karna dapat dipetakan menjadi 41x41, angka 0 adalah hitam dan 1 adalah putih.
Berikut solver menggunakan script python

```
binary_string = ""  # Paste your binary string here

from PIL import Image

# Ensure the binary string length is a multiple of 1681 (41x41)
binary_string = binary_string[:1681]

# Convert binary string to a list of rows
rows = [binary_string[i:i+41] for i in range(0, len(binary_string), 41)]

image_data = [[(0, 0, 0) if pixel == '1' else (255, 255, 255) for pixel in row] for row in rows]

image = Image.new('RGB', (41, 41))
image.putdata([pixel for row in image_data for pixel in row])

image.save("qr_code_image.png")
```
