<!DOCTYPE html>
<html>
<head>
    <title>Member Login</title>
    <link rel="stylesheet" href="login.css">
</head>

<body>

<div class="login-box">

    <h1>FITVERSE GYM</h1>
    <h2>Membership Portal</h2>

    <form action="/member-login" method="POST">

        <input
            type="text"
            name="member_id"
            placeholder="Enter Membership ID"
            required>

        <button type="submit">
            View Profile
        </button>

    </form>

</div>

</body>
</html>
