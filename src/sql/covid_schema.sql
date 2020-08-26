CREATE SCHEMA IF NOT EXISTS covid_data_schema;

create table covid_data_schema.raw_data (
	row_number serial primary key,
	data jsonb
);