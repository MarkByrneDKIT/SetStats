
--SELECT STATEMENTS ONLY --

--Select all trainees on system
SELECT * FROM trainee

--Select certain trainee by name on system
SELECT * FROM trainee WHERE username = "Trainee1"

--Select certain trainee by name and password on system
SELECT * FROM trainee WHERE username = "Trainee1" AND password = "password1"

--Select all trainers on system
SELECT * FROM trainer

--Select certain trainer by name on system
SELECT * FROM trainer WHERE username = "Trainer1"


--Select certain trainer by name and password on system
SELECT * FROM trainer WHERE username = "Trainer1" AND password = "password1"


--Select all sessions in History
SELECT * FROM history


--Select session by date in History
SELECT * FROM history WHERE date = "2021-11-01"


--Select session by trainee id in History
SELECT * FROM history WHERE trainee_id = 1


--Select session in session by session_id



--Select set_num by session id in session



--Select the lift bar co-ordinates in current lift by id of lift
SELECT xy FROM `current_session` JOIN `current_lift` WHERE lift_id = 1   -- NOW DISPLAYING CORRECLTY NOT .BIN FILE


--https://stackoverflow.com/questions/34911046/getting-geojson-linestring-from-mysql-geometry-wkt-data







--INSERT STATEMENTS ONLY --
INSERT INTO `trainee` (`username`,`password`) VALUES ("Liam Denning", "LiamPassword")  --No trainer

INSERT INTO `trainee` (`trainer_id`,`username`,`password`) VALUES (1, "Liam Denning", "LiamPassword") --with trainer


-- Add bar positions to current lift table using Geometry LineString
INSERT INTO `current_lift` (`lift_id`,`session_id`, `xy`) VALUES (1,1, ST_GeomFromText('LINESTRING(0 1,-0.5 2,-0.6 3,-0.7 4,-0.6 5,-0.45 6,-0.2 7,0 8)',0))     'SRID'
INSERT INTO `current_lift` (`lift_id`,`session_id`, `xy`) VALUES (3,1, ST_GeomFromText('LINESTRING(0 1,-0.5 2,-0.6 3,-0.7 4,-0.6 5,-0.45 6,-0.2 7,0 8)'))
INSERT INTO `current_lift` (`lift_id`, `session_id`, `xy`) VALUES (4, 1, ST_GeomFromText('LINESTRING(1 0,1 1,1 2,2 3,2 4,1.5 5,1 6,.5 7,0 8)'))		-- SETS XY TO NULL BUT SHOULD BE WORKING IDK WHY







--UPDATE STATEMENTS ONLY --


