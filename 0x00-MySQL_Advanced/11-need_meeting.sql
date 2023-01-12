---create a view that lists all students that have a score under 80 and and no last_meeting or or more that 1 month
CREATE VIEW need_meeting
AS SELECT name FROM students WHERE score < 80 AND (DATEDIFF(month, last_meeting ,CURDATE()) >= 1) OR last_meeting IS NULL;