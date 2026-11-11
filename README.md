# FitVerse Gym

The project includes a static GitHub Pages homepage and a Flask app for live
membership lookups. GitHub Pages cannot run Python or connect directly to
MySQL. Deploy the Flask app on Render and host the database on Aiven.

## 1. Create the Aiven MySQL database

1. Create a MySQL service in Aiven and wait until it is running.
2. In the service's connection information, note the host, port, user, and
   password. Keep the password private.
3. Download the service CA certificate from Aiven's connection information.
4. Connect with a MySQL client such as MySQL Workbench, using the Aiven host,
   port, user, password, and downloaded CA certificate.
5. Select the database provided by Aiven and run the `CREATE TABLE` and
   `INSERT` statements from `gym_db.sql`. Omit `CREATE DATABASE gym_db;` and
   `USE gym_db;` if Aiven has already created the database. Import only once;
   the member IDs are primary keys.

## 2. Deploy Flask on Render

1. In Render, create a **Web Service** from the GitHub repository
   `krishna-code-245/member-login`, using the `master` branch.
2. Set the build command to `pip install -r requirements.txt` and the start
   command to `gunicorn app:app`.
3. In the Render service's **Environment** settings, add:
   - `MYSQLHOST`: Aiven MySQL host
   - `MYSQLPORT`: Aiven MySQL port
   - `MYSQLUSER`: Aiven MySQL user
   - `MYSQLPASSWORD`: Aiven MySQL password
   - `MYSQLDATABASE`: the database selected for the member table
4. In Render's **Secret Files**, upload the Aiven CA certificate, for example
   as `aiven-ca.pem`. Add the environment variable `MYSQL_SSL_CA` with the
   path `/etc/secrets/aiven-ca.pem`.
5. Save the settings and deploy. Open the Render service URL followed by
   `/health`; it should return `{"status":"ok"}`. Then test with a member ID.

The app validates Aiven's TLS certificate when `MYSQL_SSL_CA` is set. Never
commit database passwords or the CA certificate to this repository.

## 3. Connect GitHub Pages

The root `index.html` is static and cannot submit to a relative Flask endpoint.
After Render gives the service a public URL, change the form action in that
file to the Render endpoint:

```html
action="https://YOUR-RENDER-SERVICE.onrender.com/member-login"
```

Replace the example domain with the actual Render URL, then commit and push.
You can also use the Render service URL directly; its Flask homepage already
posts to the correct endpoint.

## Member privacy

The lookup currently checks only a member ID. Before using real records, add a
second verification factor and keep real member data out of public repositories.
