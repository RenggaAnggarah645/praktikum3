ALTER TABLE cs
ADD CONSTRAINT fk_cs_nasabah FOREIGN KEY (Nomor_pegawai)
REFERENCES nasabah(no_rekening);
