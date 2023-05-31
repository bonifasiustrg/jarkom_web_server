# Tugas Besar Mata Kuliah Jaringan Komputer
Untuk mendapatkan projek ini di local direktori anda, jalankan command berikut:
### git clone link jarkom_web_server

Untuk menjalankan server, buka cmd/terminal di direktori folder jarkom_web_server
Lalu jalankan perintah 
### py server.py

Server ready untuk menerima request client.

Spesifikasi utama aplikasi:
1. Implementasi pembuatan TCP socket dan mengaitkannya ke alamat dan port tertentu 
2. Program web server dapat menerima dan memparsing HTTP request yang dikirimkan oleh browser 
3. Web server dapat mencari dan mengambil file (dari file system) yang diminta oleh client 
4. Web server dapat membuat HTTP response message yang terdiri dari header dan konten file yang diminta
5. Web server dapat mengirimkan response message yang sudah dibuat ke browser (client) dan dapat ditampilkan dengan benar di sisi client
6. Jika file yang diminta oleh client tidak tersedia, web server dapat mengirimkan pesan “404 Not Found” dan dapat ditampilkan dengan benar di sisi client.


<img src="https://user-images.githubusercontent.com/52784596/236688105-c426d056-4971-4534-b63d-13f6dbfc104f.png">
