create_queries_dict = {
    "create_organisation_table": """ CREATE TABLE IF NOT EXISTS organizationT (
                                org_id int NOT NULL PRIMARY KEY,
                                organisation_name varchar(100) NOT NULL,
                                number_of_members int NOT NULL,
                                number_of_repositories int NOT NULL,
                                number_of_languages int NOT NULL); """,

    "create_language_table": """ CREATE TABLE IF NOT EXISTS languagesT (
                                    lang_id int NOT NULL PRIMARY KEY,
                                    language_typ varchar(100) NOT NULL,
                                    number_of_bytes int NOT NULL,
                                    organisation_name varchar(100) NOT NULL); """,

    "create_org_lang_table": """ CREATE TABLE IF NOT EXISTS org_langs (
                                    org_langs_id int NOT NULL PRIMARY KEY,
                                    organisation_id int NOT NULL REFERENCES organizationT(org_id),
                                    language_typ_id int NOT NULL REFERENCES languagesT(lang_id)); """
}
