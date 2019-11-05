db.createUser({
    user: "burrobot",
    pwd: "password",
    roles: [
        {
            role: "dbOwner",
            db: "burrobot"
        }
    ]
});
