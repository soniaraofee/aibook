#!/bin/bash

# Hardcoded credentials
USERNAME="admin"
PASSWORD="1234"

read -p "Username: " input_user
read -s -p "Password: " input_pass
echo

if [[ "$input_user" == "$USERNAME" && "$input_pass" == "$PASSWORD" ]]; then
    echo "Login successful!"
else
    echo "Invalid username or password."
fi