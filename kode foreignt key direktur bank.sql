ALTER TABLE direktur_bank
ADD CONSTRAINT fk_direktur_bank_cs FOREIGN KEY (Kode_bank)
REFERENCES cs(id_cs);
