#!/bin/bash

key=$(ecdsakeygen -s)

if [ -z "$1" ]; then
    echo "Usage: $0 <community name>"
    exit 1
fi

ansible-vault encrypt_string --vault-password-file "$(realpath $(dirname $0)/../.fflev-vault-secret.txt)" --encrypt-vault-id default "$key" --name "$1"
printf "\nPublic Key: $(echo "$key" | ecdsakeygen -p)\n"
