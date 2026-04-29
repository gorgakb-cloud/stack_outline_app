
Original schema:
Professors
| PID (PK) | FullName | Email | UpdatedDate |

Classes
| CID (PK) | Title | PID (FK) | UpdatedDate |

Assignments
| AID (PK) | Title | Description | DueDate | Status | Grade | CID (FK) | DaysUntilDue | UpdatedDate |
---------------------------------------------------------------------------
• Original Functional Dependencies: A list of all functional dependencies
identified in the starting schema.

Professors
PID -> FullName, Email, UpdatedDate

Classes
CID -> Title, PID, UpdatedDate

Assignments 
AID -> Title, Desc, DueDate, Status, Grade, CID, UpdatedDate
DueDate -> DaysUntilDue
---------------------------------------------------------------------------
• Anomaly Identification: An explanation of any potential update, insertion, or
deletion anomalies found in the original structure.

Update: 

Updating due date of assign but not days until due value
Ex: | 5-1-2026 | 7 | --> | 5-6-2026 | 7 | this value is now wrong

Insertion: 

Cant insert an assignment without a class
Ex: 1 | SoftENg HW1 | Software architecture | 5-1-2026 | Not started | NULL | NULL | 7 | 4-24-2026 |

Deletion:

Deleting a class could cause issues when creating assignments. You cannot create an assignment without a class. 

-----------------------------------------------------------------------------
• Decomposition Steps: If a table violates 3rd Normal Form, show the step-by-step
decomposition into smaller tables.

The classes and professors tables aligns with 3NF already. The contents are only functionally dependant on the PK, and it meets the requirements of 1NF/2NF

The assignments table, however, does not. There is a transitive dependancy as DueDate relies on AID, and DaysUntilDue relies on DueDate. This violates 3NF. Decomposing this results in:

Assignments
| AID (PK) | Title | Description | DueDate | SID (FK) | Grade | CID (FK)| UpdatedDate |

Date
| DueDate (PK) | DaysUntilDue | 

Status
| SID (PK) | Status |

As best practice, I also decompose the status column into a lookup table

However, having a dedicated column for DaysUntilDue will be a bit challenging in practice, as the column must be updated every day. Removing it will fix that problem (and also remove the transitive dependancy). Prof. Farlow said this was ok.

Removing that column results in two tables:

Assignments
| AID (PK) | Title | Description | DueDate | SID (FK) | Grade | CID (FK)| UpdatedDate |

Status
| SID | Status |

-------------------------------------------------------------------------------
• Final Relational Schema: The updated schema that the Python application will
actually use.

Professors
| PID (PK) AUTO INCREMENTING INT | FullName VC(100) | Email VC(150)| UpdatedDate DATETIME |

Classes
| CID (PK) AUTO INCREMENTING INT | Title VC(100) | PID (FK) | UpdatedDate DATETIME |

Assignments
| AID (PK) AUTO INCREMENTING INT | Title VC(100) | Description VC(500) | DueDate DATETIME | SID (FK) INT | Grade DECIMAL(5,2) | CID (FK) INT | UpdatedDate DATETIME |

Status
| SID (PK) INT | Status VC(50) |