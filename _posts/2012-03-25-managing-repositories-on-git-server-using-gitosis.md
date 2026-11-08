---
title: "Managing Git Repositories with Gitosis"
date: 2012-03-25 13:14:24 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /managing-repositories-on-git-server-using-gitosis/
---

Gitosis provides a lightweight way to manage Git repositories and user access on a self-hosted server. This post covers user management, repository configuration, and access control. For initial server setup, refer to your Gitosis installation documentation.

## Adding a New User

Each user needs an SSH key pair for authentication. The user generates their key locally:

``` bash
ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub
```

The user shares their public key (the contents of `id_rsa.pub`) with the administrator through a secure channel—email, secure file transfer, or direct message. The administrator saves this to a temporary location:

``` bash
# Administrator receives the key and saves it
cat > /tmp/user1.pub << 'EOF'
ssh-rsa AAAAB3NzaC1yc2EA... user1@hostname
EOF
```

The administrator then adds the key to their local gitosis-admin repository:

``` bash
cp /tmp/user1.pub keydir/user1.pub
git -C gitosis-admin add keydir/user1.pub
git -C gitosis-admin commit -m "Add user1"
git -C gitosis-admin push
```

The filename must match the username exactly. Gitosis uses the filename (minus `.pub`) as the username for access control.

## Configuring Repository Access

All configuration happens in the `gitosis.conf` file within the gitosis-admin repository. Define groups and assign them permissions to repositories.

### Write Access

To grant write access to a repository:

    [group developers]
    writable = myproject
    members = user1 user2

Multiple repositories can be listed:

    [group developers]
    writable = myproject backend-api
    members = user1 user2

### Read-Only Access

For read-only access:

    [group viewers]
    readonly = myproject
    members = user3 user4

### Mixed Permissions

A user can belong to multiple groups with different permission levels:

    [group developers]
    writable = myproject
    members = user1

    [group viewers]
    readonly = myproject
    members = user2

User1 has write access, user2 has read-only access.

## Applying Configuration Changes

After editing `gitosis.conf`, commit and push the changes:

``` bash
git -C gitosis-admin add gitosis.conf
git -C gitosis-admin commit -m "Configure myproject repository and permissions"
git -C gitosis-admin push
```

Changes take effect immediately on the server.

## Creating and Initializing a Repository

Once configured, users can initialize a repository on the server. The administrator creates the bare repository on the Gitosis server:

``` bash
sudo su - git
cd ~/repositories
mkdir myproject.git
cd myproject.git
git init --bare
exit
```

Alternatively, a developer with write access can initialize it by pushing an existing local repository:

``` bash
git clone git@gitserver:myproject.git
cd myproject
echo "# My Project" > README.md
git add README.md
git commit -m "Initial commit"
git push origin master
```

## Managing Existing Users

To add a user to an existing group:

    [group developers]
    writable = myproject
    members = user1 user2 user3

To remove access, remove the user from the group:

    [group developers]
    writable = myproject
    members = user1 user2

To revoke all access to a user, remove their public key file and push the change:

``` bash
rm gitosis-admin/keydir/user1.pub
git -C gitosis-admin add -u
git -C gitosis-admin commit -m "Remove user1 access"
git -C gitosis-admin push
```

The user can no longer authenticate to the server.

## Restricting Repository Access by Project

You can create separate groups for different projects:

    [group backend-team]
    writable = backend-api
    members = user1 user2

    [group frontend-team]
    writable = frontend-app
    members = user3 user4

    [group devops]
    writable = backend-api frontend-app infrastructure
    members = user5 user6

This keeps permissions granular and audit-friendly. DevOps team members can deploy both projects while developers only access their assigned repositories.
