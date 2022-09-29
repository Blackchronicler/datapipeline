-- Creating necessary tables --
DROP TABLE IF EXISTS orga_langs;
DROP TABLE IF EXISTS languages;
DROP TABLE IF EXISTS organisation; 
CREATE TABLE IF NOT EXISTS organisation (
                                        orga_id SERIAL NOT NULL PRIMARY KEY,
                                        organisation_name varchar(100) NOT NULL,
                                        number_of_members int NOT NULL,
                                        number_of_repositories int NOT NULL,
                                        number_of_languages int NOT NULL);                       
CREATE TABLE IF NOT EXISTS languages (
                                        lang_id SERIAL NOT NULL PRIMARY KEY,
                                        language_typ varchar(100) NOT NULL,
                                        number_of_bytes int NOT NULL,
                                        organisation_name varchar(100) NOT NULL);                                    
CREATE TABLE IF NOT EXISTS orga_langs (
                                        orga_langs_id SERIAL NOT NULL PRIMARY KEY,
                                        organisation_id int NOT NULL REFERENCES organisation(orga_id),
                                        language_typ_id int NOT NULL REFERENCES languages(lang_id));


-- Automating sql skript reading
--with open('workspace_itech/git/lf8/queries.sql', 'r') as sqlfile: 
  --      database_queries = sqlfile.read()
    --    database_queries = database_queries.split("CREATE")

--print(len(database_queries))        
--for x in database_queries[0:2]:
 --print(x)        