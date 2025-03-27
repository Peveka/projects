#include "rsa.h"

ulonglong gcd(ulonglong x, ulonglong y){
	while (y){
		ulonglong temp = y;
		y = x%y;
		x = temp;
	}
	return x;
}

//e < phi(n)
ulonglong GetPublicKey(ulonglong phi){
	for (int i = 3; i < phi; i++){
		if (gcd(i, phi)==1){
			return i;
		}
	}
	return 0;
}

ulonglong GetPrivateKey(ulonglong exp, ulonglong phi){
	for (ulonglong d = 2; d < phi; d++){
		if((d*exp)%phi == 1){
			return d;
		}
	}
	return 0;
}
// возвращает массив простых чисел от min_val до max_val
ulonglong* GetPrimeNumList(ulonglong min_val, ulonglong max_val){
	ulonglong *buffer = malloc(max_val*sizeof(long long));
	for (ulonglong i = 0; i < max_val; i++)
		buffer[i] = i;

	// 1 не явл. простым, начинаем с двойки
	buffer[1] = 0;
	ulonglong i = 2;
	// идём до половины всех чисел (после этого перебирать не имеет смысла,
	// т.к. остальные нельзя представить как произведение целых a*b, где 
	// a и b != 1), домножаем текущее число на n и зануляем кратные числа
	while (i < (max_val/2+1)){
		if (buffer[i]) {
			ulonglong j = 2*i;
			while (j < max_val) {
				buffer[j] = 0;
				j+=i;
			}
		}
		i++;
	}

	// кол-во простых чисел (размер итогового массива)
	ulonglong primesCounter = 0;
	for (ulonglong i = min_val; i < max_val; i++){
		if (buffer[i]!=0){
			primesCounter+=1;
		}
	}

	// массив простых чисел
	ulonglong *primes = calloc(primesCounter, sizeof(long long));
	long long pos = -1;
	for (ulonglong i = 0; i < max_val; i++){
		if (buffer[i] && buffer[i]>=min_val){
			primes[++pos] = buffer[i];
		}
	}

	free(buffer);
	return(primes);
}

// алгоритм быстрого возведения в степень по модулю n
ulonglong QuickModExp(ulonglong a, ulonglong b, ulonglong n){
	a %= n;
	ulonglong res = 1;

	while (b) {
		if (b%2==1){
			res = (a*res)%n;
		}
		a = (a*a)%n;
		b /= 2;
	}

	return res;
}

// возвращает массив вида [n, e, d]
ulonglong* GetRandomKeyPair(){
	srand(time(NULL));

	ulonglong* keys = malloc(3*sizeof(long long));

	// произведение p*q должно превышать 255, т.к. шифровать будем
	// числовой код ASCII символов, поэтому необходимо обеспечить гарантировать,
	// что любые два взятых простых числа при умножении дадут число > 255
	// нижняя граница - 17 (17*19=323)) 
	ulonglong *primes = GetPrimeNumList(16, 256);
	ulonglong arrSize = 48; //размер primes

	ulonglong p = primes[rand()%arrSize];
	ulonglong q = primes[rand()%arrSize];
	while (p == q){
		q = primes[rand()%arrSize];
	}

	ulonglong n = p*q;
	ulonglong phi = (p-1)*(q-1);

	ulonglong exp = GetPublicKey(phi);
	ulonglong d = GetPrivateKey(exp, phi);

	keys[0] = n;
	keys[1] = exp;
	keys[2] = d;

	return keys;
}

// шифрует строку открытым ключом
ulonglong* EncryptMessageWithRSA(char *message, ulonglong msgLen, 
									ulonglong n, ulonglong publicKey){
	ulonglong* cipher = malloc(msgLen*sizeof(long long));
	for (int i = 0; i < msgLen; i++){
		cipher[i] = QuickModExp((ulonglong)message[i], publicKey, n);
	}
	return cipher;
}

// дешифрует набор чисел закрытым ключом
char* DecryptMessageWithRSA(ulonglong *cipher, ulonglong ciphLen, 
									ulonglong n, ulonglong privateKey){
	char *message = malloc(ciphLen+1);
	for (int i = 0; i < ciphLen; i++){
		message[i] = (char)QuickModExp(cipher[i], privateKey, n);
	}
	message[ciphLen] = '\0';

	return message;
}

