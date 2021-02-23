# Create database
database="$PWD/ab5-2.db"
sqlite3 $database <<EOF
CREATE TABLE users (UID INTEGER PRIMARY KEY, GID INTEGER, username TEXT, home TEXT);
EOF


# Load all users to database
while IFS=: read -r username passwd uid gid fullname home; do
echo $username $uid $gid $home
sqlite3 $database <<EOF
INSERT INTO users VALUES ($uid, $gid, '$username', '$home');
EOF
done < /etc/passwd

# Return all users
sqlite3 $database <<EOF
SELECT * FROM users
EOF

