-- procedure to compute the verage score of a student

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (user_id INT)
BEGIN
	-- get the average of the user
	DECLARE avg_score FLOAT;
	SELECT AVG(score) INTO avg_score FROM corrections
	WHERE corrections.user_id = user_id;
	-- set the avg score in the user table
	UPDATE users
	SET average_score = avg_score
	WHERE id = user_id;
END $$
DELIMITER ;
