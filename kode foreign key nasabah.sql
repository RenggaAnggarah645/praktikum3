ALTER TABLE nasabah
ADD CONSTRAINT fk_nasabah_teller FOREIGN KEY (KK)
REFERENCES teller(id_teller);
