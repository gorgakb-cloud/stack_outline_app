
Model: ChatGPT
Question: 
CREATE TABLE professors ( PID INT(11) NOT NULL AUTO_INCREMENT, FullName VARCHAR(100) NOT NULL COLLATE 'utf8mb4_uca1400_ai_ci', Email VARCHAR(150) NOT NULL COLLATE 'utf8mb4_uca1400_ai_ci', UpdatedDate DATETIME NOT NULL DEFAULT current_timestamp(), PRIMARY KEY (PID) USING BTREE ) 

CREATE TABLE classes ( CID INT(11) NOT NULL AUTO_INCREMENT, PID INT(11) NOT NULL, UpdatedDate DATETIME NOT NULL, Title VARCHAR(100) NOT NULL DEFAULT '0' COLLATE 'utf8mb4_uca1400_ai_ci', PRIMARY KEY (CID) USING BTREE, INDEX PID (PID) USING BTREE, CONSTRAINT PID FOREIGN KEY (PID) REFERENCES professors (PID) ON UPDATE NO ACTION ON DELETE CASCADE )

CREATE TABLE status lookup ( SID INT(11) NOT NULL, Name VARCHAR(50) NOT NULL DEFAULT '\'No Status Available\'' COLLATE 'utf8mb4_uca1400_ai_ci', PRIMARY KEY (SID) USING BTREE )

CREATE TABLE assignments (
	`AID` INT(11) NOT NULL AUTO_INCREMENT,
	`Title` VARCHAR(100) NOT NULL COLLATE 'utf8mb4_uca1400_ai_ci',
	`Description` VARCHAR(500) NULL DEFAULT 'No Description' COLLATE 'utf8mb4_uca1400_ai_ci',
	`DueDate` DATETIME NULL DEFAULT NULL,
	`SID` INT(11) NOT NULL,
	`Grade` DECIMAL(5,2) NULL DEFAULT '0.00',
	`CID` INT(11) NOT NULL,
	`UpdatedDate` DATETIME NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
	PRIMARY KEY (`AID`) USING BTREE,
	INDEX `CID` (`CID`) USING BTREE,
	INDEX `SID` (`SID`) USING BTREE,
	CONSTRAINT `CID` FOREIGN KEY (`CID`) REFERENCES `classes` (`CID`) ON UPDATE NO ACTION ON DELETE CASCADE,
	CONSTRAINT `SID` FOREIGN KEY (`SID`) REFERENCES `status lookup` (`SID`) ON UPDATE NO ACTION ON DELETE NO ACTION
)

reformat this as a python class for a sqlalchemy app

Answer:
class Professor(Base):
    __tablename__ = 'professors'

    PID = Column(Integer, primary_key=True, autoincrement=True)
    FullName = Column(String(100), nullable=False)
    Email = Column(String(150), nullable=False)
    UpdatedDate = Column(DateTime, nullable=False, server_default=func.current_timestamp())

    def __repr__(self):
        return f"<Professor(PID={self.PID}, FullName='{self.FullName}', Email='{self.Email}')>"

class Class(Base):
    __tablename__ = 'classes'

    CID = Column(Integer, primary_key=True, autoincrement=True)
    PID = Column(Integer, ForeignKey('professors.PID', ondelete='CASCADE', onupdate='NO ACTION'), nullable=False)
    UpdatedDate = Column(DateTime, nullable=False)
    Title = Column(String(100), nullable=False, default='0')

    # Relationship to Professor
    professor = relationship("Professor", backref="classes")

    def __repr__(self):
        return f"<Class(CID={self.CID}, Title='{self.Title}', PID={self.PID})>"

class StatusLookup(Base):
    __tablename__ = 'status lookup'  # keep exact name with space

    SID = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=False, default='No Status Available')

    def __repr__(self):
        return f"<StatusLookup(SID={self.SID}, Name='{self.Name}')>"

class Assignment(Base):
    __tablename__ = 'assignments'

    AID = Column(Integer, primary_key=True, autoincrement=True)
    Title = Column(String(100), nullable=False)
    Description = Column(String(500), nullable=True, default='No Description')
    DueDate = Column(DateTime, nullable=True)
    SID = Column(Integer, ForeignKey('status lookup.SID', onupdate='NO ACTION', ondelete='NO ACTION'), nullable=False)
    Grade = Column(DECIMAL(5, 2), nullable=True, default=0.00)
    CID = Column(Integer, ForeignKey('classes.CID', onupdate='NO ACTION', ondelete='CASCADE'), nullable=False)
    UpdatedDate = Column(
        DateTime,
        nullable=False,
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp()
    )

    # Relationships
    class_ref = relationship("Class", backref="assignments")
    status = relationship("StatusLookup", backref="assignments")

    def __repr__(self):
        return f"<Assignment(AID={self.AID}, Title='{self.Title}', CID={self.CID}, SID={self.SID})>"

    I reformatted/fixed these to fit the code I already created and inserted them as class creation statements
    ----------------------------------------------------------------------------
    