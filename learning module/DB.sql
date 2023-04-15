CREATE TABLE "MQ scores" ("index" INTEGER, "contract number" INTEGER, "Intervention Title" TEXT, "Planned date for draft report" date, "improvement_surcharge" REAL, "MQ 1_1" INTEGER,	"MQ 1_2" INTEGER,	"MQ 1_3" INTEGER, "MQ 1_4" INTEGER,	"MQ 2_1" INTEGER, "MQ 2_2" INTEGER,	"MQ 3_1" INTEGER,	"MQ 3_2" INTEGER,	"MQ 3_3" INTEGER,	"MQ 3_4" INTEGER,	"MQ 4_1" INTEGER,	"MQ 4_2" INTEGER,	"MQ 4_3" INTEGER,	"MQ 4_4" INTEGER, "MQ 5_1" INTEGER,	"MQ 5_2" INTEGER,	"MQ 5_3" INTEGER,	"MQ 5_4" INTEGER,	"MQ 5_5" INTEGER,	"MQ  6_1" INTEGER,	"MQ 6_2" INTEGER,	"MQ 6_3" INTEGER,	"MQ 6_4" INTEGER,	"MQ 7_1" INTEGER,	"MQ 7_2" INTEGER,	"MQ 7_3" INTEGER,	"MQ 7_4" INTEGER,	"MQ 7_5" INTEGER,	"MQ 8_1" INTEGER) WITH ("column_policy" = 'dynamic', "number_of_replicas" = '0', "refresh_interval" = 10000);

COPY "MQ_scores" ("Contract Number", "Intervention Title", "Planned date for draft report",	"MQ 1_1",	"MQ 1_2",	"MQ 1_3",	"MQ 1_4",	"MQ 2_1",	"MQ 2_2",	"MQ 3_1",	"MQ 3_2",	"MQ 3_3",	"MQ 3_4",	"MQ 4_1",	"MQ 4_2",	"MQ 4_3",	"MQ 4_4",	"MQ 5_1",	"MQ 5_2",	"MQ 5_3",	"MQ 5_4",	"MQ 5_5",	"MQ  6_1",	"MQ 6_2",	"MQ 6_3",	"MQ 6_4",	"MQ 7_1",	"MQ 7_2",	"MQ 7_3",	"MQ 7_4",	"MQ 7_5",	"MQ 8_1") FROM '/Users/leo/Library/CloudStorage/OneDrive-KOMISsrl/CAR report dev/Final version/MQ-scores_csv' WITH (format='csv')

COPY MQ_scores FROM 'file:///var/MQ_scores_csv' WITH (delimiter=',', format='csv');

CREATE TABLE "MQ_scores" ("contract number" INTEGER, "Intervention Title" TEXT, "Planned date for draft report" date, "improvement_surcharge" REAL, "MQ 1_1" INTEGER,	"MQ 1_2" INTEGER,	"MQ 1_3" INTEGER, "MQ 1_4" INTEGER,	"MQ 2_1" INTEGER, "MQ 2_2" INTEGER,	"MQ 3_1" INTEGER,	"MQ 3_2" INTEGER,	"MQ 3_3" INTEGER,	"MQ 3_4" INTEGER,	"MQ 4_1" INTEGER,	"MQ 4_2" INTEGER,	"MQ 4_3" INTEGER,	"MQ 4_4" INTEGER, "MQ 5_1" INTEGER,	"MQ 5_2" INTEGER,	"MQ 5_3" INTEGER,	"MQ 5_4" INTEGER,	"MQ 5_5" INTEGER,	"MQ  6_1" INTEGER,	"MQ 6_2" INTEGER,	"MQ 6_3" INTEGER,	"MQ 6_4" INTEGER,	"MQ 7_1" INTEGER,	"MQ 7_2" INTEGER,	"MQ 7_3" INTEGER,	"MQ 7_4" INTEGER,	"MQ 7_5" INTEGER,	"MQ 8_1" INTEGER)


URL:https://qualysguard.qg2.apps.qualys.eu/
Username:caret5lf
Password:HXcW8qS$

Access Key ID: SCWA1N5S5WPSEPQDJ6FF
Secret Key: 71ce061e-b594-470d-b8bd-5adf65f9eecc

createdb mq_scores_db
createuser -P blodesbaum
admin PASSWORD = "Stabillo&@978207+729582!"

psql -c "GRANT ALL PRIVILEGES ON DATABASE mq_scores_db TO blodesbaum;" postgres

psql -U blodesbaum -d mq_scores_db -W

CREATE TABLE mq_scores (
  "id" SMALLINT KEY,
  "Contract Number" VARCHAR(10),
  "Intervention Title" TEXT,
  "Planned date for draft report" DATE,
  "MQ 1_1" SMALLINT,
  "MQ 1_2" SMALLINT,
  "MQ 1_3" SMALLINT,
  "MQ 1_4" SMALLINT,
  "MQ 2_1" SMALLINT,
  "MQ 2_2" SMALLINT,
  "MQ 3_1" SMALLINT,
  "MQ 3_2" SMALLINT,
  "MQ 3_3" SMALLINT,
  "MQ 3_4" SMALLINT,
  "MQ 4_1" SMALLINT,
  "MQ 4_2" SMALLINT,
  "MQ 4_3" SMALLINT,
  "MQ 4_4" SMALLINT,
  "MQ 5_1" SMALLINT,
  "MQ 5_2" SMALLINT,
  "MQ 5_3" SMALLINT,
  "MQ 5_4" SMALLINT,
  "MQ 5_5" SMALLINT,
  "MQ 6_1" SMALLINT,
  "MQ 6_2" SMALLINT,
  "MQ 6_3" SMALLINT,
  "MQ 6_4" SMALLINT,
  "MQ 7_1" SMALLINT,
  "MQ 7_2" SMALLINT,
  "MQ 7_3" SMALLINT,
  "MQ 7_4" SMALLINT,
  "MQ 7_5" SMALLINT,
  "MQ 8_1" SMALLINT
  );

COPY mq_scores FROM '/Users/leo/Library/CloudStorage/OneDrive-KOMISsrl/CAR report dev/Final version/MQ-scores.csv' WITH (delimiter = ',', format = 'csv');





Yz7jgcQR2oQRHVUO