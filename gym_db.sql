CREATE DATABASE gym_db;

USE gym_db;

CREATE TABLE members (
    member_id VARCHAR(20) PRIMARY KEY,
    member_name VARCHAR(100),
    membership_type VARCHAR(50),
    expiry_date DATE
);

INSERT INTO members VALUES
('MEM001','John Doe','Premium','2027-01-15'),
('MEM002','Alice Smith','Basic','2027-02-20'),
('MEM003','Michael Brown','Premium','2027-03-18'),
('MEM004','Emma Wilson','Gold','2027-04-10'),
('MEM005','David Johnson','Basic','2027-05-12'),
('MEM006','Sophia Davis','Premium','2027-01-30'),
('MEM007','James Miller','Gold','2027-06-25'),
('MEM008','Olivia Garcia','Basic','2027-07-05'),
('MEM009','William Martinez','Premium','2027-08-15'),
('MEM010','Ava Anderson','Gold','2027-09-01'),
('MEM011','Benjamin Thomas','Basic','2027-03-22'),
('MEM012','Mia Jackson','Premium','2027-11-10'),
('MEM013','Lucas White','Gold','2027-12-01'),
('MEM014','Charlotte Harris','Basic','2027-10-18'),
('MEM015','Henry Martin','Premium','2027-04-28'),
('MEM016','Amelia Thompson','Gold','2027-05-08'),
('MEM017','Daniel Moore','Basic','2027-02-14'),
('MEM018','Evelyn Taylor','Premium','2027-06-30'),
('MEM019','Matthew Clark','Gold','2027-08-08'),
('MEM020','Harper Lewis','Basic','2027-09-25');