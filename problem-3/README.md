# Soran-soran

## Description

Di problem ini anda diminta untuk mengimplementasikan prototipe sistem registrasi sederhana. Sistemnya harus bekerja berdasarkan prinsip berikut.

Setiap kali user register, user tersebut mengirimkan string ke system tersebut dengan namanya. Misal saja usernya bernama kaguya. Jika "kaguya" tidak ada di sistem, maka "kaguya" akan dimasukkan ke database, dan si user mendapat respon "OK". Jika "kaguya" sudah ada di dalam sistem, maka sistem akan membuat nama baru, mengirimkan nama baru tersebut ke user, dan juga memasukkan nama tersebut ke database. Nama baru memiliki peraturan seperti berikut. Angka yang dimulai dari 1 ditambahkan di akhir nama, sehingga menjadi misalnya "kaguya1", lalu "kaguya2".

## Input

Baris pertama adalah angka n, 1 <= n <= 100069.

N baris berikutnya merupakan request ke sistem. Setiap request adalah string yang terdiri dari lowercase latin character dan panjangnya tidak lebih dari 169 karakter.

## Output

Print n baris, yang merupakan respon dari request: "OK" jika registrasi sukses, atau nama baru, jika nama yang diberikan sudah pernah tersimpan di database.

## Sample Input 1

```bash
4
abacaba
acaba
abacaba
acab
```

## Sample Output 1

```bash
OK
OK
abacaba1
OK
```

## Sample Input 2

```bash
6
first
first
second
second
third
third
```

## Sample Output 2

```bash
OK
first1
OK
second1
OK
third1
```
