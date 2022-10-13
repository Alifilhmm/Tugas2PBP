## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming
Asynchronous programming bersifat multithread, ia bisa menjalankan/mengeksekusi tugas arau operasi lebih dari 1 secara bersamaan. Synchronous programming bersifat single thread, ia hanya bisa mengeksekusi operasi satu per satu. Untuk kecepatan tentu akan lebih cepat asynchronous programming.

##  Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini
Event driven programming adalah cara kita menghandle jika atau saat terjadinya sebuah event yang kita inginkan, misalnya dalam tugas ini adalah button. Jika button create di modal di click, ia akan memanggil fungsi/membuat task card baru dan ditampilkan di todolist.

## Jelaskan penerapan asynchronous programming pada AJAX
Penerapan asynchronous di ajax dapat kita lihat saat menjalankan web dan membuat task. Kita tidak perlu mereload page untuk memunculkan task yang kita buat. Penerapannya ada di saat data dikirim atau diambil.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas

1. Menambahkan fungsi show_json (views.py) dan menambahkan url nya (urls.py)

2. Membuat fungsi ajax get di todolist.html untuk mengambil data. Data akan disajikan dalam bentuk json.

3. Membuat modal dengan mengambil template bootstrap dan menyambungkannya dengan link di navbar.

4. Membuat fungsi addTas_ajax (views.py) dan menambahkan url nya (urls.py)

5. Membuat fungsi ajax post di todolist.html untuk menambahkan data yang diinput user.

