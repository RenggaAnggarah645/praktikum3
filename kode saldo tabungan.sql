CREATE TABLE SALDO_TEBUNGAN (
    No_rekening INT(40) PRIMARY KEY,
    Tanggal_transaksi DATETIME,
    Jenis_transaksi VARCHAR(30),
    Id_transaksi INT(40),
    Jumlah_transaksi DECIMAL(40),
    Bukti_transaksi VARCHAR(40)
);
