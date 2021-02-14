DROP TABLE IF EXISTS `actors`;
CREATE TABLE actors (
`ActorId` int(3) NOT NULL,
`Name` varchar(30) NOT NULL,
`Age` int(2) NOT NULL,
`Gender` char(1) NOT NULL,
`ActiveSince` int(4),
PRIMARY KEY(`ActorId`)
);

INSERT INTO actors VALUES('101', 'Matt Damon', '50', 'M', '1988');
INSERT INTO actors VALUES('102', 'Tom Cruise', '58', 'M', '1986');
INSERT INTO actors VALUES('103', 'Christian Bale', '47', 'M', '1983');
INSERT INTO actors VALUES('104', 'Ben Affleck', '48', 'M', '1993');

DROP TABLE IF EXISTS `movies`;
CREATE TABLE movies (
`MovieId` int(2) NOT NULL,
`Title` varchar(40) NOT NULL,
`ReleaseDate` date NOT NULL,
`Genre` varchar(15) DEFAULT NULL,
`Runtime` int(3) NOT NULL,
PRIMARY KEY(`MovieId`)
);

INSERT INTO movies VALUES('11', 'Top Gun', '1986-05-12', 'Action', '110');
INSERT INTO movies VALUES('12', 'Prestige', '2006-10-17', 'Mystery', '135');
INSERT INTO movies VALUES('13', 'The Accountant', '2016-10-14', 'Action\Thriller', '128');
INSERT INTO movies VALUES('14', 'Collateral', '2004-08-06', 'Thriller', '120');
INSERT INTO movies VALUES('15', 'Jason Bourne', '2016-08-05', 'Action', '123');
INSERT INTO movies VALUES('16', 'Jack Reacher', '2013-01-04', 'Action\Thriller', '130');
INSERT INTO movies VALUES('17', 'Batman Begins', '2005-06-17', 'Action\Adventure', '140');
INSERT INTO movies VALUES('18', 'Green Zone', '2010-03-12', 'War\Action', '115');

DROP TABLE IF EXISTS `film`;
CREATE TABLE film (
`MovId` int(2) NOT NULL,
`Title` varchar(40) NOT NULL,
`ActId` int(3) NOT NULL,
`ActorName` varchar(30) NOT NULL,
FOREIGN KEY (`MovId`) REFERENCES `movies`(`MovieId`),
FOREIGN KEY (`ActId`) REFERENCES `actors`(`ActorId`)
);

INSERT INTO film VALUES('11', 'Top Gun', '102', 'Tom Cruise' );
INSERT INTO film VALUES('12', 'Prestige', '103', 'Christian Bale');
INSERT INTO film VALUES('13', 'The Accountant', '104', 'Ben Affleck');
INSERT INTO film VALUES('14', 'Collateral', '102', 'Tom Cruise');
INSERT INTO film VALUES('15', 'Jason Bourne', '101', 'Matt Damon');
INSERT INTO film VALUES('16', 'Jack Reacher', '102', 'Tom Cruise');
INSERT INTO film VALUES('17', 'Batman Begins', '103', 'Christian Bale');
INSERT INTO film VALUES('18', 'Green Zone', '101', 'Matt Damon');
