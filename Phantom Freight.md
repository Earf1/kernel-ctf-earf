# Phantom Freight

## Earf

## Forensics

## Medium

### Question Description
A damaged ZIP is provided that refuses to extract. On hex inspection, the PK headers appear corrupted by an extra byte each. Fix the archive, extract its contents, and continue digging through the nested artifact(s) to recover the final flag.

Provided:

File: broken.zip

### Intended Solution
- Inspect and identify ZIP header corruption

- Open the file in a hex viewer or run hexdump -C broken.zip.

- Valid ZIP local file headers start with 50 4B 03 04 and central directory entries with 50 4B 01 02; here each PK marker appears shifted with an extra byte inserted before 50 4B.

- Each header has exactly one injected byte immediately after “PK”, and the sequence of those injected bytes across the file is crafted to read “{m4Rk” when concatenated in order. For example, as the headers appear:

```
PK{ (0x50 0x4B 0x7B …) → ‘{’

PKm (0x50 0x4B 0x6D …) → ‘m’

PK4 (0x50 0x4B 0x34 …) → ‘4’

PKR (0x50 0x4B 0x52 …) → ‘R’

PKk (0x50 0x4B 0x6B …) → ‘k’
```
- Remove the extra byte consistently before every PK signature occurrence.

- Extract the repaired archive

``unzip fixed.zip into ./out/.``

- Contents expected:

``inner.zip (password-protected)
cover.jpg``

- A quick strings/exiftool on cover.jpg reveals a plausible decoy password in visible metadata (e.g., IPTC Caption-Abstract: password=thisthepasswordfr).

- The decoy fails to open inner.zip.

``exiftool -v cover.jpg shows:``

- JPEG APP13 (Photoshop 3.0) with 8BIM resource blocks; one block has an unknown Resource ID (e.g., 0x1FFF) and name “auth”.

- Extract and parse the APP13 IRB payload

- Dump the APP13 payload around the “Photoshop 3.0” header and the following “8BIM” IRB.

- IRB structure: "8BIM" | resourceID(2B) | name(Pascal, padded) | size(4B) | data(padded).

- The custom IRB’s data starts with a simple “PASS” structure:

```
ASCII “PASS” (4B)

ver(1)=0x01

flags(1)=0x00

algo(1)=0x01 (XOR)

pwlen(2,BE)

pwdata(pwlen) where each byte XOR 0x5A

crc32(4B) of pwdata for integrity
```

- Recover the zip password

- Read pwlen, slice pwdata, verify CRC32 matches.

- Reverse XOR with 0x5A (ascii Z) to obtain the password i.e m4g1cALiMag3.

- Open the inner zip and retrieve the flag

```unzip -P m4g1cALiMag3 inner.zip```

- Extracted contents include flag.png.

- View it to obtain the other part of the flag.

Flag

>kernel ctf{m4Rk3rS_ov3r_m37ADat4}kernel
