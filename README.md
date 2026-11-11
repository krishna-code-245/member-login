# FitVerse Gym

The project has two hosting targets:

- The root `index.html` is a static GitHub Pages homepage.
- The Flask app serves the working membership lookup and connects to MySQL.

GitHub Pages cannot run Python or connect directly to MySQL. Use the Railway
Flask app URL for live member lookups.

## Deploy Flask and MySQL on Railway

1. Create a Railway project and add a MySQL service.
2. Deploy this GitHub repository as a web service. Railway uses `requirements.txt`
   to install packages and `Procfile` to start Gunicorn.
3. In the Flask service's variables, add the MySQL service's values using these
   exact variable names: `MYSQLHOST`, `MYSQLPORT`, `MYSQLUSER`, `MYSQLPASSWORD`,
   and `MYSQLDATABASE`. Use Railway variable references or copy the values from
   the MySQL service. Do not commit credentials or paste them into source files.
4. Create the `members` table and import the sample rows from `gym_db.sql` into
   the database named by `MYSQLDATABASE`. If Railway has already created a
   database for the service, select that database and run the table and insert
   statements from the SQL file; omit its `CREATE DATABASE` and `USE` lines.
   Only import into a new or empty database, since the table uses a primary key.
5. Generate a public domain for the Flask service. Open that domain and check
   `/health`; it should return `{"status":"ok"}`. Then test a member ID.

The application defaults to `localhost` and the `gym_db` database for local
development. Railway connection settings come from environment variables.

## Connect the GitHub Pages form to Railway

After Railway gives the Flask service a public domain, update the `action` on
the membership form in the root `index.html` to:

```html
action="https://YOUR-RAILWAY-DOMAIN/member-login"
```

Replace `YOUR-RAILWAY-DOMAIN` with the actual domain, then commit and push that
change. The Railway-hosted homepage already posts to its own Flask endpoint.

## Member privacy

The lookup currently uses member ID as its only check. Before using real member
records, add a second verification factor and avoid loading real records into
public sample SQL or a public repository.
