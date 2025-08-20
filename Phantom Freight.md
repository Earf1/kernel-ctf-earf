Title
Phantom Freight

Author
Earf

Domain
Forensics

Difficulty
Medium

Question Description
A damaged ZIP is provided that refuses to extract. On hex inspection, the PK headers appear corrupted by an extra byte each. Fix the archive, extract its contents, and continue digging through the nested artifact(s) to recover the final flag.

Provided:

File: broken.zip

Hints:

“Mind the application markers.”

“Shop talk.”

Expected flow: repair the ZIP headers, extract to obtain an inner zip and a media file (JPEG), then find the password to unlock the inner zip.

Intended Solution
Inspect and identify ZIP header corruption

Open the file in a hex viewer or run hexdump -C broken.zip.

Valid ZIP local file headers start with 50 4B 03 04 and central directory entries with 50 4B 01 02; here each PK marker appears shifted with an extra byte inserted before 50 4B.

Strategy: remove the extra byte consistently before every PK signature occurrence.

Repair PK headers

Automate removal with a small script:

Scan for occurrences of 0xXX 50 4B where 0xXX is the injected byte.

Drop the injected 0xXX so the stream reads 50 4B … at each header boundary.

Save the corrected file as fixed.zip.

Validate with zip -T fixed.zip or unzip -l fixed.zip.

Extract the repaired archive

unzip fixed.zip into ./out/.

Contents expected:

inner.zip (password-protected)

cover.jpg (or an audio/radio capture depending on variant)

A quick strings/exiftool on cover.jpg reveals a plausible decoy password in visible metadata (e.g., IPTC Caption-Abstract: password=Spring2025!).

Recognize the decoy and locate the real channel

The decoy fails to open inner.zip.

Hints “application markers” and “Shop talk” point to JPEG APP segments, specifically APP13 used by Photoshop (IRB: “8BIM”) rather than APP2.

exiftool -v cover.jpg shows:

JPEG APP13 (Photoshop 3.0) with 8BIM resource blocks; one block has an unknown Resource ID (e.g., 0x1FFF) and name “auth”.

Extract and parse the APP13 IRB payload

Dump the APP13 payload around the “Photoshop 3.0” header and the following “8BIM” IRB.

IRB structure: "8BIM" | resourceID(2B) | name(Pascal, padded) | size(4B) | data(padded).

The custom IRB’s data starts with a simple “PASS” structure:

ASCII “PASS” (4B)

ver(1)=0x01

flags(1)=0x00

algo(1)=0x01 (XOR)

pwlen(2,BE)

pwdata(pwlen) where each byte XOR 0x5A

crc32(4B) of pwdata for integrity

Recover the zip password

Read pwlen, slice pwdata, verify CRC32 matches.

Reverse XOR with 0x5A to obtain the ASCII password, e.g., m4g1cALiMag3.

Open the inner zip and retrieve the flag

unzip -P m4g1cALiMag3 inner.zip

Extracted contents include flag.txt.

View it to obtain the final flag.

Validation and pitfalls

Pitfall: relying on visible EXIF/IPTC/XMP decoys; these won’t open the inner zip.

Validation: the recovered password should match an integrity clue (CRC32 embedded in the PASS payload). If CRC mismatches, you grabbed the wrong IRB/data.

Tools that help:

exiftool -v (to see APP13/Photoshop)

hex editor/xxd (to locate “Photoshop 3.0”, “8BIM”, and parse)

Optional parser script to decode the PASS structure reliably.

Flag
flag format is kernel ctf{.....}kernel

kernel ctf{m4rk3rS_ov3r_m3tadatA}kernel

If you share the other challenge prompts or filenames, I’ll generate matching writeups in the exact same structure.
