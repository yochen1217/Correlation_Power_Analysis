from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import numpy as np

def check_key(pt, ct, key):
    # 確保 key 為 16 bytes (AES-128)
    key_bytes = key.astype(np.uint8).tobytes()
    if len(key_bytes) != 16:
        raise ValueError("Key must be 16 bytes (AES-128).")

    # 確保 pt, ct 是 16 bytes 區塊
    pt_bytes = pt.tobytes()
    ct_bytes = ct.tobytes()
    
    if len(pt_bytes) % 16 != 0 or len(ct_bytes) % 16 != 0:
        raise ValueError("Plaintext and ciphertext must be a multiple of 16 bytes (AES block size).")

    # AES-128 ECB 加密
    cipher = Cipher(algorithms.AES(key_bytes), modes.ECB())
    encryptor = cipher.encryptor()
    pred_ct = encryptor.update(pt_bytes) + encryptor.finalize()  # 正確的加密流程

    return pred_ct == ct_bytes  # 直接比對 bytes

# 測試數據
# pt = np.array([0x32, 0x43, 0xf6, 0xa8, 0x88, 0x5a, 0x30, 0x8d,
#                0x31, 0x31, 0x98, 0xa2, 0xe0, 0x37, 0x07, 0x34], dtype=np.uint8)

# key = np.array([0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6,
#                 0xab, 0xf7, 0x87, 0x32, 0x20, 0xa0, 0x7d, 0x67], dtype=np.uint8)
pt  = np.array([0xb9, 0xd2, 0x00, 0xb8, 0xff, 0x40, 0x07, 0x09, 0x41, 0x65, 0x2e, 0xb8, 0x82, 0xde, 0x7b, 0xa0], dtype=np.uint8)
key = np.array([0xca ,0x38 ,0xb2 ,0x02 ,0x17 ,0x53 ,0x73 ,0xc0, 0x50, 0xb7 ,0xda, 0xad, 0xfd, 0x06, 0x39 ,0xf1], dtype=np.uint8)

# **重新確認 `ct` 來自 AES-128 ECB**
cipher = Cipher(algorithms.AES(key.tobytes()), modes.ECB())
encryptor = cipher.encryptor()
correct_ct = encryptor.update(pt.tobytes()) + encryptor.finalize()

ct = np.frombuffer(correct_ct, dtype=np.uint8)  # 確保 `ct` 正確

print(check_key(pt, ct, key))  # 應該回傳 True