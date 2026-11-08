---
title: "Automating Password Changes on Linux: passwd, chpasswd, and Safer Methods"
date: 2013-08-25 10:09:35 +0000
layout: post
canonical: https://www.systutorials.com/changing-linux-users-password-in-one-command-line/
---

The `passwd` command is designed for interactive use—it prompts for input rather than accepting passwords via stdin by default. When you need to set passwords programmatically (bulk user provisioning, CI/CD automation, remote administration), you need methods that bypass the interactive prompt.

## Using passwd with –stdin

The `--stdin` flag tells `passwd` to read the new password from standard input:

``` bash
echo "newpassword" | passwd --stdin username
```

This works on most modern distributions (RHEL/CentOS, Fedora, Debian/Ubuntu, AlmaLinux, Rocky Linux). However, some systems disable `--stdin` via PAM configuration for security reasons. If you get “passwd: unrecognized option ‘–stdin’”, use an alternative method.

## Piping Multiple Inputs

If `--stdin` isn’t available, pipe the password twice with newlines:

``` bash
echo -e "newpassword\nnewpassword" | passwd username
```

The `-e` flag tells `echo` to interpret escape sequences. This works because `passwd` normally asks for the password twice to prevent typos.

For changing your own password as a regular user, provide the current password first, then the new password twice:

``` bash
echo -e "currentpass\nnewpass\nnewpass" | passwd
```

## Using chpasswd for Batch Operations

For multiple password changes on a single system, `chpasswd` is more efficient than spawning multiple `passwd` processes:

``` bash
echo "user1:password1" | chpasswd
echo "user2:password2" | chpasswd
```

Or load from a file with `username:password` format on each line:

``` bash
chpasswd < passwordfile.txt
```

Specify the encryption method with the `-c` option:

``` bash
echo "user1:newpass" | chpasswd -c SHA512
```

Verify the encryption in the shadow file:

``` bash
sudo grep user1 /etc/shadow
```

## Remote Password Changes

Combine these methods with SSH for bulk operations across servers:

``` bash
ssh user@remotehost 'echo "newpass" | passwd --stdin targetuser'
```

For multiple servers:

``` bash
for server in server1 server2 server3; do
  ssh root@$server "echo 'newpass' | passwd --stdin targetuser"
done
```

Using IP ranges:

``` bash
for ((i=1; i<=100; i++)); do
  ssh root@10.1.0.$i "echo 'newpass' | passwd --stdin targetuser"
done
```

## Creating Users with Initial Passwords

Combine user creation and password setting in one operation:

``` bash
ssh remotehost 'useradd -m -s /bin/bash newuser && echo "initialpass" | passwd --stdin newuser'
```

Add the user to supplementary groups during creation:

``` bash
ssh remotehost 'useradd -m -s /bin/bash -G sudo,docker newuser && echo "pass123" | passwd --stdin newuser'
```

Set the user’s home directory with specific permissions:

``` bash
ssh remotehost 'useradd -m -d /home/newuser -s /bin/bash newuser && echo "pass123" | passwd --stdin newuser && chmod 750 /home/newuser'
```

## Why Non-Interactive Passwords Are Risky

Passwords visible in command lines can be read by:

- Other users via `ps`, `ps aux`, or `/proc/<pid>/cmdline`
- Shell history files (`.bash_history`, `.zsh_history`)
- SSH server logs and authentication logs
- Process monitoring tools and container image layers
- Reverse history search in interactive shells

Non-interactive password methods should only be used when:

- Operating in isolated environments or CI/CD systems with restricted access
- Passwords are temporary and users change them on first login
- You control all systems in the pipeline
- Interactive prompts aren’t feasible

## Secure Alternatives

**SSH key-based authentication** — Eliminates password use entirely:

``` bash
ssh-copy-id -i ~/.ssh/id_rsa.pub user@remotehost
```

**Force password change on first login** — Use `chage` to expire the initial password:

``` bash
chage -d 0 newuser
```

This sets the password change date to epoch, forcing a password change at next login.

**Configuration management tools** — Ansible, Terraform, and Puppet support secure credential handling with vaults, encrypted variables, and secret backends:

``` bash
# Ansible with vault
ansible-vault create group_vars/webservers/vault.yml
# Then reference: {% raw %}{{{% endraw %} vault_password }}
```

**Centralized authentication** — LDAP, Active Directory, FreeIPA, or RADIUS offload password management and policy enforcement to dedicated servers.

**Credential vaults** — HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, or 1Password for Business:

``` bash
# HashiCorp Vault example
vault kv put secret/newuser password="$(openssl rand -base64 16)"
```

Generate temporary credentials at runtime instead of embedding them in scripts.

**Never** hardcode production passwords in scripts, container images, configuration files, or version control. Use environment variables from secure sources, read from credential managers at runtime, or implement interactive prompts for sensitive deployments.
