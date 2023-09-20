ALTER TABLE saldo_tabungan
ADD CONSTRAINT fk_saldo_tabungan_direktur FOREIGN KEY (id_transaksi)
REFERENCES direktur_bank(id_direktur);
