# Freifunk Leverkusen Ansible

Ansible Roles and Playbooks for the Freifunk Leverkusen Infrastructure

## Usage

To deploy a gateway run:

```
ansible-playbook gateways.yml
```

You will need the secrets file for Ansible Vault to be present in the base
directory of this repository. The expected filename is
`.fflev-vault-secret.txt` and it needs to contain only the secret string.

## Environment

These Ansible playbooks and roles are currently intended for and tested on
Fedora 36 systems running in the Hetzner Cloud.

## Contributing

This repository uses [`pre-commit`](https://pre-commit.com/) to ensure
consistency.
So before submitting pull requests ensure you installed `pre-commit` to your
local git hooks using `pre-commit install`.
