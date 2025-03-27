#include "rsa.h"
// выводит на экран строку заданной длины
void printStr(char *str, ulonglong length){
	for(int i = 0; i < length; i++){
		printf("%c", str[i]);
	}
}
// выводит на экран и в файл числовой массив
void printCiph(ulonglong *ciph, int symKeyLength){
	FILE *file = fopen("xor_key.txt", "w");
	for(int i = 0; i < symKeyLength; i++){
		printf("%llu ", ciph[i]);
		fprintf(file, "%llu ", ciph[i]);
	}
	putchar('\n');
	fclose(file);
}

int main(int argc, char **argv){
	int keyLength = 16;

	if (argc == 1){ // hints
		printf("Usage: \n");
		printf("\t./rsa -k/-keygen\n");
		printf("\t./rsa -e/-encrypt yourfile public_key\n");
		printf("\t./rsa -d/-decrypt yourfile private_key encrypted_key\n");
		printf("Public/private keys format: n e/d\n");
		printf("Note: you can specify an encrypted key with a file using -f flag: \n");
		printf("\t./rsa -d yourfile private_key -f file_with_encrypted_key\n");
		return 1;
	} // key generator
	else if (argc == 2 && (!strcmp(argv[1], "-k") || !strcmp(argv[1], "-keygen"))){
		ulonglong *keys = GetRandomKeyPair();
		printf("Public key: (%llu, %llu)\n", keys[0], keys[1]);
		printf("Private key: (%llu, %llu)\n", keys[0], keys[2]);
		free(keys);
		return 0;
	} // encryption with specified public key
	else if (argc == 5 && (!strcmp(argv[1], "-e") || !strcmp(argv[1], "-encrypt"))){
		char *filename = argv[2];
		ulonglong n = strtoull(argv[3], NULL, 10);
		ulonglong exp = strtoull(argv[4], NULL, 10);
		char *symmetricKey = GetRandomSymmetricEncryptionKey(keyLength);
		XORFileWithKey(filename, symmetricKey);
		printf("The file has been encrypted successfully!\n");
		printf("The following encrypted key was saved in \"xor_key.txt\": \n");
		printCiph(EncryptMessageWithRSA(symmetricKey, keyLength, n, exp), keyLength);
		free(symmetricKey);
		return 0;
	} // decryption with specified private and xor keys
	else if (!strcmp(argv[1], "-d") || !strcmp(argv[1], "-decrypt")){
		char *filename = argv[2];
		ulonglong n = strtoull(argv[3], NULL, 10);
		ulonglong d = strtoull(argv[4], NULL, 10);
		ulonglong *cipher = malloc(keyLength * sizeof(long long));
		if (strcmp(argv[5], "-f") != 0){ // if input from file was specified
			for (int i = 5; argv[i] != NULL; i++){
				cipher[i-5] = strtoull(argv[i], NULL, 10);
			}
		} else { // manual input
			FILE *fileWithEncryptedKey = fopen(argv[6], "r");
			ulonglong temp;
			for (int i = 0; fscanf(fileWithEncryptedKey, "%llu", &temp)==1; i++){
				cipher[i] = temp;
			}
			fclose(fileWithEncryptedKey);
		}

		char *symmetricKey = DecryptMessageWithRSA(cipher, keyLength, n, d);
		XORFileWithKey(filename, symmetricKey);
		printf("The file has been decrypted successfully!\n");
		free(cipher);
		return 0;
	} else { // incorrect input case
		printf("Hmm, it seems you did something wrong. Run ./rsa to view all the "
			"available options and try again.\n");
		return 1;
	}

}
