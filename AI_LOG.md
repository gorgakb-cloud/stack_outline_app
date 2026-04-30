
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
    AI Model: ChatGPT

    Query: want to prepopulate status table
    
    Answer:
    def seed_status_table():
    statuses = ["Not Started", "In Progress", "Completed", "Graded"]

    for s in statuses:
        exists = Status.query.filter_by(name=s).first()
        if not exists:
            db.session.add(Status(name=s))

    db.session.commit()

    Use: Put this in a statuses.py file
    ----------------------------------------------------------------------------
    AI Model: ChatGPT

    Query: reformat
    <div class="right_side"> <h1>Assignments</h1> <a href="{{ url_for('add_assignment') }}"> Add Assignment </a> <table> <tr> <th>Title</th> <th>Description</th> <th>Class</th> <th>Due Date</th> <th>Status</th> <th>Grade</th> <th>Updated Date</th> <th>Actions</th> </tr> <tr> <td></td> <td></td> <td></td> <td></td> <td></td> <td></td> <td></td> <td> <a href="">Delete</a> <a href="">Update</a> </td> </tr> </table> </div>

    Answer:
    {% for assignment in assignments %}
<tr>
    <td>{{ assignment.Title }}</td>
    <td>{{ assignment.Description }}</td>
    <td>{{ assignment.class_.Title }}</td>
    <td>{{ assignment.DueDate }}</td>
    <td>{{ assignment.Status }}</td>
    <td>{{ assignment.Grade }}</td>
    <td>{{ assignment.UpdatedDate }}</td>
    <td>
        <a href="{{ url_for('main.delete_assignment', id=assignment.AID) }}">Delete</a>
        <a href="{{ url_for('main.update_assignment', id=assignment.AID) }}">Update</a>
    </td>
</tr>
{% endfor %}

Use: using this to fix the error in my index file
-------------------------------------------------------------------------------------------
Model: ChatGPT

Query: create assignment form

Response: 
<div class="main">
    
    <h1>Add Assignment</h1>

    <form action="{{ url_for('main.add_assignment') }}" method="post">
        
        <label>Title:</label><br>
        <input type="text" name="title" required><br>

        <label>Description:</label><br>
        <input type="text" name="description"><br>

        <label>Class:</label><br>
        <select name="class_id">
            {% for c in classes %}
                <option value="{{ c.CID }}">{{ c.Title }}</option>
            {% endfor %}
        </select><br>

        <label>Due Date:</label><br>
        <input type="date" name="due_date"><br>

        <label>Status:</label><br>
        <select name="status">
            <option value="Not Started">Not Started</option>
            <option value="In Progress">In Progress</option>
            <option value="Completed">Completed</option>
        </select><br>

        <label>Grade:</label><br>
        <input type="number" name="grade"><br><br>

        <input type="submit" value="Submit">
    </form> 

</div>

Use: use this code to add an assignment, use as a template for an add class form

