# ants in my pants

## Author
Earf

## Domain
Forensics

## Difficulty
Medium 

### Question Description

I think there is ant in my keyboard, my numlock keeps blinking...

**Files Provided:**
```
  handout.zip
- contains a handout.pcap
 ```

### Intended Solution
- On unzipping, we get a .pcap file and a .txt file. The .txt file contains the link to a pastebin.
- **Identify NumLock LED control packets:**  
  Filter USB traffic for control transfers (URB_CONTROL) from the host to the keyboard with a single byte payload. These payloads toggle the NumLock LED on or off with `0x01` representing OFF and `0x02` representing ON.

- **Extract timing intervals between LED state changes:**  
  For each change in NumLock LED state, calculate the time difference since the previous change.

- **Interpret these intervals as Morse code symbols:**  
  - Short intervals (< 300ms) represent dots (`.`)  
  - Longer intervals (≥ 300ms) represent dashes (`-`)  
  Longer on intervals or gaps between toggles mark letter separations.

- **Build a Morse timing pattern string:**  
  Translate the sequence of LED toggles and timing intervals into a string combining dots, dashes, and underscores signaling symbol and letter gaps using a python script

- **Decode the Morse pattern into text:**  
  Use a Morse code dictionary to map the Morse sequence into letters and digits.

- **Format the decoded message:**  
  The decoded message will give password for the pastebin

This approach leverages the temporal modulation of NumLock LED state in USB HID control packets as a covert channel for transmitting Morse code messages, which are then reliably extracted and decoded by analyzing the capture's timing data.
***


### Flag

> ctf{nUm1Ck_cOvr7_cHNl_dc7D}kernel

