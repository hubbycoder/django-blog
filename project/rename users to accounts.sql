-- SQLite
UPDATE django_content_type SET app_label='accounts' WHERE app_label='users';

ALTER TABLE users_profile RENAME TO accounts_profile;

UPDATE django_migrations SET app='accounts' WHERE app='users';