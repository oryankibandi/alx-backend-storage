---calculated weighted-avareage for all students

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE user_id INT;
    DECLARE name VARCHAR(255);
    DECLARE cur CURSOR FOR SELECT user_id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;
        
        SET @weighted_sum = SELECT SUM(score * weight) FROM corrections WHERE user_id = user_id
        INNER JOIN projects
        ON corrections.project_id = projects.id;

        SET @sum_weights = SELECT SUM(weight) FROM projects WHERE id IN (
          SELECT project_id FROM corrections WHERE user_id = user_id
        );
        SET @weighted_average = weighted_sum / sum_weights;
        UPDATE users (average_score) VALUES (weighted_average) WHERE user_id = user_id;

    END LOOP;

    CLOSE cur;
END