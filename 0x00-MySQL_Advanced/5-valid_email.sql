---creates a trigger that resets the attribute valid_email only when the email has been changed
CREATE TRIGGER validate_email
AFTER UPDATE ON users
BEGIN
    DECLARE old_email VARCHAR(255);
    DECLARE new_email VARCHAR(255);
    IF NEW.email != OLD.email THEN
      UPDATE  users SET valid_email = 0;
    END IF
END;