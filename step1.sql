CREATE SCHEMA `step1` ;
#建立step1数据库
CREATE TABLE `step1`.`dept_name` (
  `dept_name` VARCHAR(45) NOT NULL,
  `building` VARCHAR(45) NULL,
  `budget` VARCHAR(45) NULL,
  PRIMARY KEY (`dept_name`));
#建立dept_name表格，主键为dept_name
CREATE TABLE `step1`.`student` (
  `ID` INT(20) NOT NULL,
  `name` VARCHAR(45) NULL,
  `sex` CHAR(1) NULL,
  `age` INT(3) NULL,
  `emotin_state` VARCHAR(45) NULL,
  `dept_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID`),
  INDEX `dept_name_idx` (`dept_name` ASC),
  CONSTRAINT `dept_name`
    FOREIGN KEY (`dept_name`)
    REFERENCES `step1`.`dept_name` (`dept_name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
#建立student表格，主键为ID，外键为dept_name
CREATE TABLE `step1`.`exam` (
  `student_ID` INT(20) NOT NULL,
  `exam_name` VARCHAR(45) NULL,
  `grade` VARCHAR(45) NULL,
  PRIMARY KEY (`student_ID`),
  CONSTRAINT `student_ID`
    FOREIGN KEY (`student_ID`)
    REFERENCES `step1`.`student` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
#建立exam表格，stduent_ID和exam_name主键，外键为stduent_ID