-- Lists all privileges of the MySQL users user_0d_1 and user_0d_2
SELECT * 
FROM information_schema.user_privileges 
WHERE grantee = 'user_0d_1@localhost'
OR grantee = 'user_0d_2@localhost';
