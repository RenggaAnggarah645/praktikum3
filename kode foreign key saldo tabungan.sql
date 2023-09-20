ALTER TABLE saldo_tabungan
ADD CONSTRAINT fk_saldo_tabungan_direktur FOREIGN KEY (no_rekening)
REFERENCES direktur_bank(id_direktur);
