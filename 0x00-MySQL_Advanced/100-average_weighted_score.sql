-- creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.

DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser( IN user_id INT)
BEGIN
	DECLARE weighted_av FLOAT;
	SELECT SUM(score * weight) / SUM(weight)  INTO weighted_av
	FROM corrections
	INNER JOIN projects
	ON projects.id = corrections.project_id
	WHERE corrections.user_id = user_id;
	
	SET weighted_av = IFNULL(weighted_av, 0);

	-- update a user table
	UPDATE users
	SET average_score = weighted_av
	WHERE id = user_id;
END //
DELIMITER ;
