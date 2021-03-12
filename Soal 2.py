# Menghitung Umur
TglLahir = 29
BlnLahir = 4
ThnLahir = 2002

TglSekarang = 12
BlnSekarang = 3
ThnSekarang = 2021

Umur_dalam_tahun = ((ThnSekarang - ThnLahir) + (BlnSekarang-BlnLahir)/12 + (TglSekarang-TglLahir)/365)
Umur_dalam_bulan = ((TglSekarang - TglLahir)/30) + (BlnSekarang - BlnLahir) + ((ThnSekarang - ThnLahir)*12)
Umur_dalam_hari = ((ThnSekarang-ThnLahir)*365 + (BlnSekarang-BlnLahir)*30 + (TglSekarang-TglLahir))

# RT dan RW
RT = 2
RW = 5

# Tinggi Badan
TB = 155

# Berat Badan
BB = 53

# Ukuran Sepatu
Ukuran_sepatu = 39

print("Nama saya Erlinda Madiastuti Nur Hafifah")
print("Saya lahir di Sukoharjo tanggal", TglLahir, "bulan", BlnLahir, "tahun", ThnLahir)
print("Umur saya", Umur_dalam_tahun, "tahun atau ", Umur_dalam_bulan, "bulan atau ", Umur_dalam_hari, "hari")
print("Saya tinggal di Candirejo RT ", RT, "/RW ", RW, "Klumprit, Kecamatan Mojolaban, Kabupaten Sukoharjo")
print("Saat ini saya berkuliah di Program Studi Teknik Industri Universitas Sebelas Maret Surakarta")
print("Saya tidak kos karena rumah saya tidak terlalu jauh dengan kampus")
print("Tinggi badan saya ", TB, "cm")
print("Berat badan saya ", BB, "kg")
print("Ukuran sepatu saya ", Ukuran_sepatu)
