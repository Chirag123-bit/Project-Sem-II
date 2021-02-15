"""
CREATE TABLE 'assignment'.'new_table' (
  'SID' INT NOT NULL AUTO_INCREMENT,
  'FName' VARCHAR(45) NOT NULL,
  'LName' VARCHAR(45) NOT NULL,
  'EAddress' VARCHAR(45) NOT NULL,
  'Password' VARCHAR(45) NOT NULL,
  'UserName' VARCHAR(45) NOT NULL,
  'DOB' date NOT NULL,
  'Class' int NOT NULL,
  'Section' VARCHAR(45) NOT NULL,
  CONSTRAINT pk_register PRIMARY KEY ('SID'),
  UNIQUE INDEX 'UserName_UNIQUE' ('UserName' ASC) VISIBLE);
"""




"""
CREATE TABLE `assignment`.`grades` (
  `UserName` VARCHAR(45) NOT NULL,
  `Maths` INT NULL,
  `Science` INT NULL,
  `Nepali` INT NULL,
  `English` INT NULL,
  `Social` INT NULL,
  `Computer` INT NULL,
  `EPH` INT NULL,
  `Geography` INT NULL,
  `Total` INT GENERATED ALWAYS AS (Maths+Science+Nepali+English+Social+Computer+EPH+Geography) VIRTUAL,
  `Percentage` FLOAT GENERATED ALWAYS AS (Total/8) VIRTUAL,
  Foreign KEY (`UserName`) references user_info(UserName));

"""