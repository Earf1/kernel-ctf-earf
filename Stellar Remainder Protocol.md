# Stellar Remainder Protocol

## Earf

## Cryptography  

## Hard

### Question Description

The advanced civilization on Proxima Centauri b developed a sophisticated cryptographic protocol that combines their understanding of recursive mathematical sequences with multi-dimensional matrix transformations. Dr. Reyes intercepted their diplomatic transmission, which uses a layered encoding system.

The aliens' encoding process works in stages:
1. **Orbital Synchronization**: Uses Fibonacci sequences modulo prime orbital periods (Pisano periods)
2. **Dimensional Mapping**: Applies matrix transformations representing their 5-dimensional space
3. **Harmonic Convergence**: Combines results using Chinese Remainder Theorem

The message appears to be 34 characters long.

**Files provided:**
- `sequence_transmission.txt` - The intercepted encoded sequence
- `dimension_matrices.txt` - 5D transformation matrices (determinants are invertible mod given primes)
- `harmonic_frequencies.txt` - Encoded convergence parameters
- `decoder_framework.py` - Guided decoding framework

**Handout 1 (sequence_transmission.txt):**
```
[63D, A18, 1055, 1A6D, 2AC2, 452F, 6FF1, B520, 12511, 1DA31, 2FF42, 4D973, 7D8B5, CB228, 148ADD,
213D05, 35C7E2, 5704E7, 8CCCC9, E3D1B0, 1709E79, 2547029, 3C50EA2, 6197ECB, 9DE8D6D, FF80C38,
19D699A5, 29CEA5DD, 43A53F82, 6D73E55F, B11924E1, 11E8D0A40, 1CFA62F21, 2EE333961]

```
*Note: These are Fibonacci numbers F(17) through F(50) in hexadecimal, using indexing F(0)=0, F(1)=1*

**Handout 2 (dimension_matrices.txt):**
```
[[[13, 21], [8, 34]], [[34, 55], [21, 89]], [[89, 144], [55, 233]], [[233, 377], [144, 610]], [[610, 987], [377, 1597]]]
```
*Note: All matrix determinants are invertible modulo the convergence primes. Matrices cycle for encoding beyond 5 characters.*

**Handout 3 (harmonic_frequencies.txt):**
```
01100001 01100101 01100111 01101011 01101101
```
*Note: Primes encoded as ASCII codes in binary → decimal: (97, 101, 103, 107, 109)*

**Handout 4 (decoder_framework.py):**
working on it

### Intended Solution

The solution processes all 34 Fibonacci numbers (F(17) through F(50)) to decode the complete flag. The matrices cycle through the 5 available transformations to handle all characters.

**Key Implementation:**
- **Matrix cycling** for characters beyond the 5th
- **Complete flag decoding** using all mathematical stages
- **Progress tracking** shows first few characters for verification

### Flag

> `ctf{0rb1t4l_m4th_1s_0ut_0f_th1s_w0rld}kernel`



