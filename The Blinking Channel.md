# The Blinking Channel

## Author
Earf

## Domain
Forensics

## Difficulty
Medium 

### Question Description

Our SOC team noticed unusual activity on a compromised workstation. The user reported that their NumLock LED was behaving erratically - blinking in strange patterns during what appeared to be normal typing sessions. We managed to capture USB traffic during one of these incidents.

Something tells us this isn't just a hardware malfunction. Can you investigate what's really happening?

**Files Provided:**
- `handout.pcapng`

### Intended Solution

**Step 1: Initial Analysis**
- Open the pcapng file in Wireshark
- Filter for USB traffic using `usb.transfer_type == 0x01` to focus on LED transfers from host to kb.
- Look for patterns in URB_CONTROL packets going from host to keyboard device

**Step 2: Identify LED Control Packets**
- Focus on packets with single-byte payloads alternating between specific values
- These are HID Output Report packets that control LED states
- NumLock LED is controlled by bit 0 of the LED bitmap:
  - `0x01` = NumLock ON
  - `0x00` = NumLock OFF

**Step 3: Extract Timing Patterns**
- Each LED control packet contains a single byte payload
    Bit 0 controls NumLock: 0x01 = ON, 0x00 = OFF
- Calculate time intervals between consecutive state changes
- Apply timing thresholds to distinguish between Morse elements:
    Short intervals (< 300ms) = dots (.)
    Longer intervals (≥ 300ms) = dashes (-)
- Ignore edge cases, where rapid toggles are involved.

**Step 4: Timing Analysis**
- Write a script to analyze time differences between LED state changes
- Intervals < 300ms represent dots (.)
- Intervals > 300ms represent dashes (-)
- Longer gaps when NumLock is ON indicate letter separations

**Step 5: Decode Morse Code**
- Locate the Referenced Packet.
- Extract raw payload - Right-click packet → Follow Stream or copy hex data
- (Have to add more to this)

**Step 7: Format Flag**
- Take the decoded message and format it according to the specification
- Convert to lowercase and replace spaces with underscores

### Flag

> ctf{numl0ck_c0v3rt_ch4nn3l_d3t3ct3d}kernel


