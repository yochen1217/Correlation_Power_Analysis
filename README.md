# Intro
A simple code that applies a Correlation Power Analysis (CPA) attack on five datasets using AES-128.
Each dataset contains 1,280 traces and plaintext for calculation.
There is also a ciphertext to verify the answer.
You can use key_verify.py to check whether the key is correct.

# Understanding CPA Attack
CPA is a side-channel attack that exploits the correlation between power consumption and processed data to extract the secret key used in cryptographic operations (e.g., AES).
It assumes that power consumption depends on the number of bits set to 1 (Hamming weight model).

Steps in CPA
1. Collect Power Traces
    * Measure power consumption while an AES encryption is running.
    * Each power trace corresponds to a plaintext-ciphertext pair.

2. Hypothesis for Key Guessing

    * For each key byte (16 bytes in AES), make 256 possible key guesses (0-255).
    * Compute the intermediate values of AES using the S-box.

3. Power Model (Hamming Weight Model)

    * Convert the intermediate value to Hamming weight.
    * Ex: HW(01101010) = 4 (since there are four '1' bits).

4. Correlation Computation

    * Compute correlation between Hamming weight values and power traces.
    * The key hypothesis with the highest correlation is the most likely key.
