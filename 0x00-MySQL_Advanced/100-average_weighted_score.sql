---Calculates a weightd average score for a student
CREATE PROCEDURE ComputeAverageScoreForUser (
  IN user_id INT
)
BEGIN
  SET @weighted_sum = SELECT SUM(score * weight) FROM corrections WHERE user_id = user_id
  INNER JOIN projects
  ON corrections.project_id = projects.id;

  SET @sum_weights = SELECT SUM(weight) FROM projects WHERE id IN (
    SELECT project_id FROM corrections WHERE user_id = user_id
  );
  SET @weighted_average = weighted_sum / sum_weights;
  UPDATE users (average_score) VALUES (weighted_average) WHERE user_id = user_id;
END