# file nackal

## Description

Ketika bapak kau ingin mengirim file di Tinder, dia mendapati error. Jika nama filenya mengandung tiga atau lebih "x", (huruf latin lowercase x) secara berturut-turut, sistem akan memblokir file nackal tersebut.

Tentukan jumlah karakter minimum yang perlu dihapus agar nama file tidak nackal atau mengandung substring "xxx". Print0apabila nama file dari awal memang tidak nackal.

Posisi karakter yang dihapus sembarang, tidak harus berturut-turut. Jika kita menghapus 1 karakter, maka panjang stringnya akan berkurang1. Sebagai contoh, jika kamu menghapus karakter diposisi ke 2 di string "uxxxaas", maka stringnya menjadi "uxxaas".

## Input

Baris pertama berupa integer n(3 <=n<= 100) -- Panjang dari nama file

Baris kedua adalah sebuah string dengan panjang n yang mengandung lowercase latin saja, yaitu nama filenya.

## Output

Print jumlah karakter minimum yang harus dihapus dari nama file supaya tidak mengandung "xxx" sebagai substring. Apabila dari awal tidak terdapat "xxx", print 0.
