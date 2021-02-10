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