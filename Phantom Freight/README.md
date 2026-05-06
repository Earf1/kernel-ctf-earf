# Phantom Freight

## Earf 

## Domain 

Forensics

## Intended Solution

### 1) Inspect the header and find anomalies
- Normal ZIP markers:
  - Local file header: bytes `50 4B 03 04` 
  - Central directory file header: `50 4B 01 02`.
  - End of central directory: `50 4B 05 06`.
Here, each expected `PK` signature has an extra byte immediately after `50 4B`
- First PK headers and the placeholder ones towards the end have `{ m a r k` appended. This is the first part of the flag

### 2) Repair the ZIP 
The extra bytes have to be removed and the file can be extracted.

### 3) Inspecting the extracted contents
Upon extracting the zip file gives a zip named `hi.zip` and a `load.jpg`. The zip is password protected, so the password must be smw in the image

### 4) Inspect the image
- Running `exiftool -v load.jpg` 
```
XExif
yothisthepasswordfr
nahthisthepasswordong
JFIF
@Photoshop 3.0
8BIM
auth
PASS
7n=k9
1"AQ
```
- Here, `@Photoshop 3.0 8BIM auth PASS Jn=k91"AQ` is the beginning of the IRB injection into the APP13 block which is used by photoshop for its resource blocks

### 5) Parse IRB
- IRB structure repeats as:
  - Signature: `8BIM` (ASCII, 4 bytes).
  - Resource ID: 2 bytes, big-endian
  - Pascal name: 1-byte length n, then n name bytes; pad a single `00` if 1+n is odd (so total name field is even).
  - Data size: 4 bytes, big-endian N.
  - Data: next N bytes; then pad a single `00` if N is odd (so next IRB begins on an even boundary).

### 6) Identify the custom IRB
- Non-standard Resource IDs (like `0x1FFF`) draw attention.
- A human-readable Pascal name (e.g., `auth`) suggests intentional placement.
- Data size is modest, hinting at a structured secret.

### 7) Recognize and parse the PASS structure
- Inside the target IRB’s Data, you should see a clear 4-byte magic: `50 41 53 53` (“PASS”). That tells you it’s a compact, custom container.
```
# Structure:
#  8BIM            (4)  : 38 42 49 4D
#  ResourceID      (2)  : 1F FF
#  Pascal name len (1)  : 04
#  Pascal name          : 61 75 74 68  ("auth")
#  Name padding    (0/1): 00           (to make name field even)
#  Data size       (4)  : 00 00 00 19  (25 bytes)
#  Data (N bytes)       : 50 41 53 53 01 00 01 00 12 37 6E 3D 6B 39 11 11 11 11 11 11 1B 16 33 17 3B 3D 69 2D DE E5 8C
#  Data padding    (0/1): 00           (to make total data even)
```

### 8) Recover the password from PASS
Looking at the data bytes, 
`50 41 53 53 01 00 01 00 0C 37 6E 3D 6B 39 11 11 11 11 11 11 1B 16 33 17 3B 3D 69 2D DE E5 8C` 

Here `50 41 53 53` translates to PASS in ascii, the bits after that `01 00 01 00 0C` are ver | flags | algo | pwlen 

pwlen gives us that the password is 18 characters. 

which are `37 6E 3D 6B 39 11 11 11 11 11 11 1B 16 33 17 3B 3D 69`

Running XOR bruteforce on this gives the pwd as `m4g1cKKKKKKALiMag3`

### 9) Final step
- Unizziping hi.zip gives hi.png, opening which gives the other part of the flag written on it.

> ctf{m4Rk3rS_ov3r_m37ADat4}kernel
