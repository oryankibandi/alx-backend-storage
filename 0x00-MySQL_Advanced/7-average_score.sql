---computes and stores average score for a student
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
  SET @num_of_corr = SELECT COUNT(*) FROM corrections WHERE user_id = user_id AND score IS NOT NULL;
  SET @average = SELECT AVG(score) FROM corrections WHERE user_id = user_id AND score IS NOT NULL;
  INSERT INTO users (average_score) VALUES average WHERE user_id = user_id;
END
