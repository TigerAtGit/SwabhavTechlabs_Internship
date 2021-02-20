DROP TABLE IF EXISTS `Contact`;
CREATE TABLE `Contact` (
`ContactID` INT NOT NULL AUTO_INCREMENT,
`FirstName` VARCHAR(30) NOT NULL,
`LastName` VARCHAR(30),
`Contact_no` CHAR(10) NOT NULL UNIQUE,
`Email` VARCHAR(40),
`Contact_type` VARCHAR(15),
PRIMARY KEY(`ContactID`)
);

ALTER TABLE Contact AUTO_INCREMENT = 100;

INSERT INTO contact(`FirstName`, `LastName`, `Contact_no`, `Email`, `Contact_type`) VALUES('Amit', 'Kumar', '9922455679', 'amitk321@gmail.com', 'Office');
INSERT INTO Contact(`FirstName`, `LastName`, `Contact_no`, `Email`, `Contact_type`) VALUES('Sanjay', 'Singh', '8855667744', 'sansingh1@gmail.com', 'Friend'); 
INSERT INTO Contact(`FirstName`, `LastName`, `Contact_no`, `Email`, `Contact_type`) VALUES('Vishnu', 'Tiwari', '5454789912', 'vishnu.tiw@gmail.com', 'Office'); 
INSERT INTO Contact(`FirstName`, `LastName`, `Contact_no`, `Email`, `Contact_type`) VALUES('Lakshya', 'Dutt', '9966932145', 'ldutt2000@gmail.com', 'Family'); 
INSERT INTO Contact(`FirstName`, `LastName`, `Contact_no`, `Email`, `Contact_type`) VALUES('Jack', 'Ryan', '7400574008', 'ryanjack7@yahoo.com', 'Friend'); 
INSERT INTO Contact(`FirstName`, `LastName`, `Contact_no`, `Email`, `Contact_type`) VALUES('Vishal', 'R', '7676525234', 'r.vishal@gmail.com', 'Friend'); 
INSERT INTO Contact(`FirstName`, `LastName`, `Contact_no`, `Email`, `Contact_type`) VALUES('Nitin', 'Sharma', '9000588850', 'NKsharma11@gmail.com', 'Family'); 

DROP TABLE IF EXISTS `Contact_Address`;
CREATE TABLE `Contact_Address` (
`CID` INT NOT NULL,
`Address` VARCHAR(40),
`City` VARCHAR(20),
`Pin Code` VARCHAR(6),
FOREIGN KEY(`CID`) REFERENCES `Contact`(`ContactID`)
);

INSERT INTO Contact_Address VALUES('100', '245-B Chandan Nagar', 'Mumbai', '400083');
INSERT INTO Contact_Address VALUES('101', '931-P Model Town', 'Ambala', '125045');
INSERT INTO Contact_Address VALUES('103', 'D Block 227 Sector 11', 'Patiala', '135607');
INSERT INTO Contact_Address VALUES('102', 'Hotel Paradise DP Road', 'Delhi', '100402');
INSERT INTO contact_address VALUES('104', '93 B Aveneue Centrals', 'Panaji', '403110');
INSERT INTO contact_address VALUES('106', 'House no.48 Model Town', 'Rohtak', '125032');
INSERT INTO contact_address VALUES('105', '481/7 Enclave Vista', 'Mumbai', '400012');