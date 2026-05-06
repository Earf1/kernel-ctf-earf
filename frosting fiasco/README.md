# Title  
frosting fiasco 
## Earf

## Domain  
Forensics

## Difficulty  
Medium

### Question Description  

Provided:
`http://allthepics.net/image/hh.apjYU#embeds`


### Intended Solution  
1. **Analyze the PNG IHDR Chunk:**  
   On opening the PNG in a hex editor, we can locate the IHDR chunk, which contains original width, height, and a CRC32 checksum.  

2. **Modify IHDR Dimensions:**  
   Players need to guess how much to increase the height of the image by, increase it by only a small amount will reveal a decoy, increasing it by the correct amount (or more) will reveal the flag.

3. **Recalculate CRC32:**  
   The CRC covers the IHDR chunk type plus chunk data (13 bytes).  
   Using Python's `zlib.crc32()`, we compute the new CRC32 to match the fixed IHDR data. 

   Without changing the CRC for this chunk, the image will get corrupted and will not be uncropped properly. 

   ```python
   import zlib
   ihdr_data = bytes.fromhex('4948445200000400000003A50806000000')
   crc = zlib.crc32(ihdr_data) & 0xffffffff
   print(f'{crc:08X}') 
   ```

4. **Patch the PNG File:**  
   Replacing the cropped height/width and the old CRC in the file's hex with the new height width hex values and new CRC gives the uncropped image with the hidden flag.


### Flag  
> `ctf{h3igH7_oF_d3c3p710n}kernel`

