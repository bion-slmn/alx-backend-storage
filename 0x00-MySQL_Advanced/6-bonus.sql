--  stored procedure AddBonus that adds a new correction for a student

DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
	DECLARE project_id INT;

	SELECT id INTO project_id FROM projects WHERE projects.name = project_name;
	-- check if project_id exists
	
	IF project_id IS NULL THEN
		-- create a the project
		INSERT INTO projects(name) VALUES (project_name);
		SET project_id = LAST_INSERT_ID();
	END IF;
	
	-- adding a new correction
	INSERT INTO corrections(user_id, project_id, score)
	VALUES (user_id, project_id, score);
END $$
DELIMITER ;
