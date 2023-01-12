---adds a new correction for a student
CREATE PROCEDURE AddBonus (
  IN user_id INT,
  IN project_name VARCHAR(255),
  IN score INT
)
BEGIN
  SET @existing_project = SELECT name FROM projects WHERE name = project_name;
  IF existing_project IS NOT NULL THEN
    UPDATE corrections SET score = score WHERE user_id = user_id;
  ELSE
    INSERT INTO projects (name) VALUES (project_name);
    SET @proj_id = SELECT id FROM projects WHERE name = project_name;
    INSERT INTO corrections ( user_id, project_id, score ) VALUES ( user_id, proj_id, score );
  END IF
END;
