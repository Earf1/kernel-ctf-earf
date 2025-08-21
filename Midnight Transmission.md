# Midnight Transmission

## Earf

## Forensics

## Medium 

### Question Description

My grandfather was a radio enthusiast who worked as a telegraph operator. After he passed away, I inherited his old car, a 1970s sedan that he'd heavily modified with custom SDR equipment built into the dashboard. While going through the glove compartment, I found a peculiar note tucked behind the owner's manual: *"When the clock strikes midnight, tune to the frequency where the old pirates used to broadcast. The numbers tell a different story when you capture both phases. The key to everything is in the trunk."*

In the trunk, I discoverd a hidden compartment containing an old USB drive with a single file labeled `midnight_1640.iq`

**Files provided:** `midnight_1640.iq`

**Flag format:** `ctf{LAT_LON}kernel` where LAT and LON are decimal degrees rounded to 4 decimal places (e.g., `ctf{40.7128_-74.0060})kernel`)

### Intended Solution

1. **Load IQ File**: Import the raw RF data using appropriate SDR software or Python

2. **Component Separation**: Extract I (In-phase) and Q (Quadrature) components

3. **Signal Analysis**: Examine the constellation diagram and frequency spectrum
   - Use GNU Radio Companion to visualize I/Q constellation
   - Identify that both components contain modulated data
   - Notice phase relationships between I and Q channels

4. **Demodulation Process**: Apply different demodulation schemes to each component
   ```python
   # AM demodulation
   i_demod = np.abs(i_component)
   
   # FM demodulation
   q_demod = np.diff(np.unwrap(np.angle(q_component)))
   ```

5. **Phase Relationship Analysis**: Calculate instantaneous phase differences
   ```python
   phase_diff = np.angle(samples)
   phase_degrees = np.degrees(phase_diff) % 360
   ```

6. **Data Extraction**: The phase differences encode characters for UTM coordinates

7. **UTM Coordinate Parsing**: Extract UTM zone, easting, and northing
   ```python
   # Example decoded string: "18T 0585628 4511322"
   # Format: [Zone][Band] [Easting] [Northing]
   parts = utm_string.split()
   zone_band = parts[0] 
   easting = int(parts[1])  
   northing = int(parts[2]) 
   
   zone_number = int(zone_band[:-1]) 
   zone_letter = zone_band[-1] 
   ```

8. **UTM to Lat/Lon Conversion**: Convert UTM coordinates to decimal degrees
   ```python
   import utm
   
   lat, lon = utm.to_latlon(easting, northing, zone_number, zone_letter)
   lat_rounded = round(lat, 4)
   lon_rounded = round(lon, 4)
   
   print(f"Latitude: {lat_rounded}")
   print(f"Longitude: {lon_rounded}")
   ```

9. **Flag Construction**: Format the coordinates into the flag

### Flag
> `ctf{40.7589_-73.9851}kernel` (placeholder coordinates for now)


(can expand this level more by adding parts of the place mentioned in the coords in the final flag)
