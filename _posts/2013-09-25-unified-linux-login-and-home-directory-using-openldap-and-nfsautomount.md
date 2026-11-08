---
title: "OpenLDAP and NFS for Centralized User Authentication"
date: 2013-09-25 09:59:36 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/unified-linux-login-and-home-directory-using-openldap-and-nfsautomount/
---

This guide sets up OpenLDAP for centralized authentication and NFS with automount to provide unified home directories across a cluster. The setup uses modern OpenLDAP backends and current NFS4 best practices.

## System Environment

**Server:**

- LDAP and NFS: 10.0.0.2, Fedora 41 x86_64
- Base DN: dc=lgcpu1

**Clients:**

- Range: 10.0.0.1/24, Fedora 41 x86_64

## LDAP Server Setup

### Package Installation

``` bash
sudo dnf install openldap-servers openldap-clients
sudo systemctl enable slapd
sudo systemctl start slapd
```

### Configure slapd

Use dynamic configuration (cn=config) instead of static slapd.conf. This method allows configuration changes without restarting the daemon.

First, generate a password hash for the LDAP admin account:

``` bash
slappasswd -s your_password
```

Save the output (starts with `{SSHA}`). Create `/tmp/ldap-config.ldif`:

``` bash
sudo tee /tmp/ldap-config.ldif > /dev/null <<'EOF'
dn: olcDatabase={2}mdb,cn=config
changetype: modify
replace: olcSuffix
olcSuffix: dc=lgcpu1
-
replace: olcRootDN
olcRootDN: cn=manager,dc=lgcpu1
-
add: olcRootPW
olcRootPW: {SSHA}your_hashed_password_here
EOF
```

Apply the configuration:

``` bash
sudo ldapmodify -Y EXTERNAL -H ldapi:/// -f /tmp/ldap-config.ldif
```

Note: The mdb backend is the modern default — it’s faster and more reliable than the older bdb backend.

### Create Directory Structure

Create the LDAP tree structure with `top.ldif`:

``` bash
cat > top.ldif <<'EOF'
dn: dc=lgcpu1
objectClass: dcObject
objectClass: organization
o: lgcpu1
dc: lgcpu1

dn: cn=manager,dc=lgcpu1
objectClass: organizationalRole
cn: manager

dn: ou=people,dc=lgcpu1
objectClass: organizationalUnit
ou: people

dn: ou=group,dc=lgcpu1
objectClass: organizationalUnit
ou: group

dn: ou=auto.master,dc=lgcpu1
objectClass: automountMap
ou: auto.master

dn: cn=/home,ou=auto.master,dc=lgcpu1
objectClass: automount
automountInformation: ldap:ou=auto.home,dc=lgcpu1
cn: /home

dn: ou=auto.home,dc=lgcpu1
objectClass: automountMap
ou: auto.home
EOF
```

Load the LDIF:

``` bash
ldapadd -x -D 'cn=manager,dc=lgcpu1' -W -f top.ldif
```

Verify the structure loaded correctly:

``` bash
ldapsearch -x -D 'cn=manager,dc=lgcpu1' -W -b dc=lgcpu1
```

### Migrate Existing Users

If migrating from local `/etc/passwd` and `/etc/group` files, install the migration tools:

``` bash
sudo dnf install openldap-migration
```

Export only regular users (UID ≥ 1000):

``` bash
grep -E ':[0-9]{4,}:' /etc/passwd > /tmp/passwd.export
grep -E ':[0-9]{4,}:' /etc/group > /tmp/group.export
```

Edit migration script variables in `/usr/share/openldap/migration/migrate_common.ph`:

``` perl
$DEFAULT_MAIL_DOMAIN = "example.com";
$DEFAULT_BASE = "dc=lgcpu1";
```

Generate LDIF files from the exports:

``` bash
/usr/share/openldap/migration/migrate_passwd.pl /tmp/passwd.export > people.ldif
/usr/share/openldap/migration/migrate_group.pl /tmp/group.export > groups.ldif
```

Load them into LDAP:

``` bash
ldapadd -x -D 'cn=manager,dc=lgcpu1' -W -f people.ldif
ldapadd -x -D 'cn=manager,dc=lgcpu1' -W -f groups.ldif
```

## NFS Server Setup

### Export Configuration

Edit `/etc/exports`:

    /home 10.0.0.1/24(rw,sync,no_root_squash)

**Option reference:**

- `rw` — read/write access
- `sync` — writes are committed immediately (required for data consistency)
- `no_root_squash` — allows root on clients to write as root on server

For tighter security in production, use `root_squash` and add `anonuid=1000,anongid=1000` to map root requests to a regular unprivileged user instead.

### Enable NFS Services

``` bash
sudo systemctl enable nfs-server
sudo systemctl start nfs-server
sudo exportfs -a
```

Verify the exports are available:

``` bash
showmount -e 10.0.0.2
```

## Client Configuration

### Package Installation

``` bash
sudo dnf install nss-pam-ldapd autofs nfs-utils
```

On RHEL 9, the package is called `libnslcd` instead of `nss-pam-ldapd` (the naming changed between distributions).

### LDAP Authentication

Create `/etc/nslcd.conf`:

``` bash
sudo tee /etc/nslcd.conf > /dev/null <<'EOF'
uid nslcd
gid ldap
uri ldap://10.0.0.2/
base dc=lgcpu1
EOF
```

Set appropriate permissions:

``` bash
sudo chmod 600 /etc/nslcd.conf
```

Enable and start the nslcd service:

``` bash
sudo systemctl enable nslcd
sudo systemctl start nslcd
```

Update `/etc/nsswitch.conf` to query LDAP for user and group information:

    passwd:     files ldap
    group:      files ldap
    shadow:     files ldap

Test that NSS can resolve LDAP users:

``` bash
getent passwd sample
getent group sample
```

If these commands return user/group information, LDAP resolution is working.

### Automount Configuration

Edit `/etc/auto.master` to add the home directory mount point:

    /home ldap:ou=auto.home,dc=lgcpu1 --timeout=300

The `--timeout=300` unmounts idle mounts after 5 minutes, freeing system resources.

Enable and start autofs:

``` bash
sudo systemctl enable autofs
sudo systemctl start autofs
```

Test automounting by accessing a user’s home directory — it should mount on demand:

``` bash
ls /home/sample
```

Monitor automount activity:

``` bash
sudo journalctl -u autofs -f
```

## Adding Individual Users

Each new user requires three LDAP entries: a user account, a group, and an automount entry.

### User Account Entry

Create `user-sample.ldif`:

``` bash
cat > user-sample.ldif <<'EOF'
dn: uid=sample,ou=people,dc=lgcpu1
uid: sample
cn: sample
sn: sample
mail: sample@example.com
objectClass: inetOrgPerson
objectClass: posixAccount
objectClass: top
userPassword: {SSHA}hashed_password_here
loginShell: /bin/bash
uidNumber: 1001
gidNumber: 1001
homeDirectory: /home/sample
EOF
```

Generate the password hash:

``` bash
slappasswd -s your_password
```

Paste the output into the `userPassword` field. Assign unique `uidNumber` and `gidNumber` for each user, starting at 1001 and incrementing.

### Group Entry

Create `group-sample.ldif`:

``` bash
cat > group-sample.ldif <<'EOF'
dn: cn=sample,ou=group,dc=lgcpu1
objectClass: posixGroup
objectClass: top
cn: sample
gidNumber: 1001
memberUid: sample
EOF
```

The `gidNumber` must match the user’s `gidNumber`.

### Automount Entry

Create `auto.home-sample.ldif`:

``` bash
cat > auto.home-sample.ldif <<'EOF'
dn: cn=sample,ou=auto.home,dc=lgcpu1
objectClass: automount
automountInformation: -fstype=nfs4,rw,soft,intr 10.0.0.2:/home/sample
cn: sample
EOF
```

The `soft,intr` options allow automount to timeout gracefully if the NFS server is unreachable, rather than hanging indefinitely. NFS4 is preferred over NFSv3 for better security and performance.

### Load All Entries

``` bash
ldapadd -x -D 'cn=manager,dc=lgcpu1' -W -f user-sample.ldif
ldapadd -x -D 'cn=manager,dc=lgcpu1' -W -f group-sample.ldif
ldapadd -x -D 'cn=manager,dc=lgcpu1' -W -f auto.home-sample.ldif
```

### Prepare Home Directory on NFS Server

``` bash
sudo mkdir -p /home/sample
sudo cp -r /etc/skel/. /home/sample/
sudo chown -R 1001:1001 /home/sample
sudo chmod 700 /home/sample
```

## Verification and Troubleshooting

### Test Client Login

``` bash
ssh sample@10.0.0.1
```

If login fails, verify LDAP connectivity:

``` bash
ldapsearch -x -b dc=lgcpu1 uid=sample
```

This confirms the user exists in LDAP.

### Check Service Status

``` bash
sudo systemctl status nslcd
sudo systemctl status autofs
sudo systemctl status nfs-client.target
```

### NFS Mounting Issues

Ensure firewall rules allow NFS traffic (ports 111 for rpcbind, 2049 for NFS):

``` bash
sudo firewall-cmd --permanent --add-service=nfs
sudo firewall-cmd --permanent --add-service=rpc-bind
sudo firewall-cmd --reload
```

Check active NFS mounts on the client:

``` bash
mount | grep nfs
```

If a mount hangs, verify the server is running:

``` bash
sudo systemctl status nfs-server
sudo exportfs -v
```

### LDAP Connection Debugging

Test LDAP connectivity directly from a client:

``` bash
ldapwhoami -x -D 'cn=manager,dc=lgcpu1' -W -H ldap://10.0.0.2/
```

Check nslcd logs for authentication issues:

``` bash
sudo journalctl -u nslcd -f
```

### Automount Debugging

Monitor automount in real time:

``` bash
sudo journalctl -u autofs -f
```

Verify the automount map is loaded correctly:

``` bash
ldapsearch -x -b 'ou=auto.home,dc=lgcpu1'
```

If automount times out, adjust the timeout in `/etc/auto.master` or increase it for slower networks. Common values are 300 seconds for local networks, 600+ for WAN connections.
