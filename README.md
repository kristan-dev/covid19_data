# COVID 19 Data Loader

This project simulates the first part of an ETL which is called `Extract`.

This project extracts data from the source files `COVID-19 Activity.csv` and inserts the raw data into a database. Ready to be transformed.

The database has been provided as a container, to properly execute the code, the database must exist in your local environment.

## Getting Started

1) Begin by creating the `database container` using the provided docker-compose file `docker-compose.local.yml`.

To create the container, execute the command:
```
docker-compose -f docker-compose.local.yml up --build
```

2) Prepare environment by running `pip install -r requirements.txt`

3) Using your preferred database client, connect to the database using credentials supplied in the `conf/config.yml`.

4) Create the database schema and table using the SQL files provided in `sql/covid_schema.sql`

5) Execute load_data.py and wait for script to finish.

6) Query database to see result. The data source inserts a total of 755077 rows in the database.

## What is in the data

The data contains comprehensive information about logged COVID 19 cases in a given area. The raw data in itself is good but can still be transformed depending on the requirements
of the models created by the data scientists.

## Why do you think it can be interesting for RingCentral

1) The data can be used by RingCentral to push for targetted ads depending on the location and number of covid 19 cases.
An area with a high number of cases could mean more people staying home, which means more people communicating to each online and may need RingCentral's solutions.

## Your thoughts regarding the project

I think the project has a lot of potential, given the proper requirements, a fully realized ETL can be created, ready to used by your Data Scientists or be consumed by your Business Intelligence Application.

## Versioning
Version 1.0.0
We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Kristan Eres** - [kristan-dev](https://github.com/kristan-dev/covid19_data)

## License

This project is licensed under the MIT License

MIT License

Copyright (c) 2020 Kristan Sangalang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
