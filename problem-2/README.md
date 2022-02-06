# Komm susser tod

## Description

Pada problem ini, anda akan diberikan deretan angka dan sebuah string.

Misalkan kita punya string "amogus". Jika kita geser ke kanan 1 kali, maka akan menjadi "samogu". Jika kita geser lagi ke kanan 2 kali, maka akan menjadi "gusamo". Kemudian jika kita geser ke kiri 4 kali, maka akan menjadi "mogusa".

Sudah paham? Ok. Sekarang akan dijelaskan guna dari deret angka yang diberikan. Misal kita diberikan deret angka 2 5 3 7 4 2. Maka kita akan melakukan operasi berikut pada string yang diberikan: Geser ke kanan 2 kali, geser kiri 5 kali, geser kanan 3 kali, geser kiri 7 kali, geser kanan 4 kali, dan geser kiri 2 kali. Urutannya selang seling bergantian kanan-kiri dimulai dari kanan dulu.

Tugas anda adalah, temukan wujud string yang diberikan setelah dilakukan operasi berdasarkan deretan angka yang diberikan.

## Input

Input memiliki 3 baris

Baris pertama adalah n, banyak angka didalam deretan angka, 3 <= n <= 169.

Baris kedua adalah deretan angka a sebanyak n, 3 <= a <= 169.

Baris ketiga adalah string s yang terdiri dari lowercase dan uppercase latin character tanpa spasi. Panjang string tidak lebih dari 169 karakter.

## Output

Outputnya 1 baris saja, string s yang sudah dioperasikan berdasarkan deret angka yang diberikan.

## Sample Input 1

```bash
18
32 3 139 88 38 106 169 148 62 50 66 47 16 74 94 107 79 45
XsbyZKbVJUPYsFPKLmJpVWQhYOfNTiJEKQhVKGtoHrWEuzSeoRQdWSKWRNSvozyyOMLylrfLsnNavnbJzFvUuSTwovplKkMpeGEaXtXmR
```

## Sample Output 1

```bash
bJzFvUuSTwovplKkMpeGEaXtXmRXsbyZKbVJUPYsFPKLmJpVWQhYOfNTiJEKQhVKGtoHrWEuzSeoRQdWSKWRNSvozyyOMLylrfLsnNavn
```

## Sample Input 2

```bash
122
98 40 92 112 39 47 17 48 61 161 9 155 89 98 29 5 50 64 162 8 139 42 79 12 84 94 24 101 140 134 75 76 162 128 102 44 94 125 25 57 80 127 152 52 151 150 116 83 35 169 13 106 111 37 9 105 132 59 126 12 32 111 80 103 113 24 97 113 117 142 90 140 79 53 48 125 134 166 107 155 112 18 140 137 97 164 46 140 109 55 132 119 160 126 110 17 52 126 89 75 11 39 75 122 32 110 145 87 77 26 162 76 113 136 77 155 11 13 44 50 84 161
zlRujMeKftrTRKtLSjgkFFjQnqJTBcmyYYTeoPNmbcTBdNzOHhPsbWdtJqoZqGwK
```

## Sample Output 2

```bash
trTRKtLSjgkFFjQnqJTBcmyYYTeoPNmbcTBdNzOHhPsbWdtJqoZqGwKzlRujMeKf
```

## Sample Input 3

```bash
3
1 5 2
ayam
```

## Sample Output 3

```bash
amay
```
