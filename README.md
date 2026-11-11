# FitVerse Gym

This repository contains a static GitHub Pages site. Its homepage is `index.html`,
with styles in `login.css` and the page background in `images/bg.jpg`.

## Publish with GitHub Pages

1. Push the repository to GitHub.
2. Open the repository's **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**.
4. Select the branch you want to publish and the `/ (root)` folder, then save.

GitHub will provide the published site URL in the Pages settings.

## Membership lookup limitation

GitHub Pages only hosts static files; it does not run the Flask application or
connect to MySQL. The homepage therefore explains that member profiles are
unavailable instead of attempting an insecure client-side lookup.

For private, live membership lookups, deploy the Flask app and database to a
server that supports them. Do not publish real member records, credentials, or
database passwords in this repository.
