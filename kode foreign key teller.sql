ALTER TABLE teller
ADD CONSTRAINT fk_teller_saldo_tabungan FOREIGN KEY (Nomor_pegawai)
REFERENCES saldo_tabungan(No_rekening);
