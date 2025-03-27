#ifndef RSA_ENCRYPTION_HEADER_INCLUDED
#define RSA_ENCRYPTION_HEADER_INCLUDED 

#include "xor.h"

#define ulonglong unsigned long long

ulonglong gcd(ulonglong x, ulonglong y);

ulonglong GetPublicKey(ulonglong phi);

ulonglong GetPrivateKey(ulonglong exp, ulonglong phi);

ulonglong* GetPrimeNumList(ulonglong min_val, ulonglong max_val);

ulonglong QuickModExp(ulonglong a, ulonglong b, ulonglong n);

ulonglong* GetRandomKeyPair();

ulonglong* EncryptMessageWithRSA(char *message, ulonglong msgLen, 
									ulonglong n, ulonglong publicKey);

char* DecryptMessageWithRSA(ulonglong *cipher, ulonglong ciphLen, 
									ulonglong n, ulonglong privateKey);

#endif
