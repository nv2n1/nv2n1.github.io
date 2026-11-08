---
title: "Enable SSH on Fedora Linux"
date: 2018-03-24 11:47:35 +0000
modified: 2026-04-12 08:03:29 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-enable-ssh-service-on-fedora-linux/
---

\[md\]
By default, Fedora doesn’t enable SSH access. You’ll need to install OpenSSH server, start the service, and configure your firewall to allow connections.

\## Install OpenSSH Server

```wp-block-code
sudo dnf install openssh-server openssh-clients
```

The `openssh-clients` package provides the `ssh` command for connecting to other machines, while `openssh-server` allows incoming connections.

\## Start and Enable the SSH Service

```wp-block-code
sudo systemctl start sshd
sudo systemctl enable sshd
```

The `enable` command makes SSH start automatically on boot. Verify it’s running:

```wp-block-code
sudo systemctl status sshd
```

You should see “active (running)” in the output.

\## Configure the Firewall

Fedora uses `firewalld` by default. Open port 22 for SSH:

```wp-block-code
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
```

Verify the rule is active:

```wp-block-code
sudo firewall-cmd --list-services
```

You should see `ssh` in the list.

\## Test Your SSH Connection

From another machine on the same network:

```wp-block-code
ssh username@fedora-host-ip
```

Find your Fedora machine’s IP address:

```wp-block-code
ip addr show | grep 'inet '
```

\## SSH Configuration Hardening

For production use, edit `/etc/ssh/sshd_config` to improve security:

\*\*Disable root login:\*\*

```wp-block-code
PermitRootLogin no
```

\*\*Disable password authentication (use keys only):\*\*

```wp-block-code
PasswordAuthentication no
PubkeyAuthentication yes
```

\*\*Change the default port (optional):\*\*

```wp-block-code
Port 2222
```

If you change the port, update the firewall:

```wp-block-code
sudo firewall-cmd --permanent --add-port=2222/tcp
sudo firewall-cmd --permanent --remove-service=ssh
sudo firewall-cmd --reload
```

\*\*Limit access to specific users:\*\*

```wp-block-code
AllowUsers alice bob
```

After any configuration change, restart the service:

```wp-block-code
sudo systemctl restart sshd
```

\## Set Up SSH Key Authentication

Generate a key pair on your client machine:

```wp-block-code
ssh-keygen -t ed25519 -C "your-email@example.com"
```

Copy the public key to your Fedora server:

```wp-block-code
ssh-copy-id username@fedora-host-ip
```

Or manually if `ssh-copy-id` isn’t available:

```wp-block-code
cat ~/.ssh/id_ed25519.pub | ssh username@fedora-host-ip "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

Test the connection — you should log in without a password prompt.

\## SELinux Considerations

Fedora enforces SELinux by default. SSH generally works out of the box, but if you encounter issues:

Check SELinux status:

```wp-block-code
getenforce
```

If SSH can’t read authorized_keys:

```wp-block-code
sudo restorecon -Rv ~/.ssh
```

If you changed the SSH port, tell SELinux:

```wp-block-code
sudo semanage port -a -t ssh_port_t -p tcp 2222
```

\## Troubleshooting

\*\*Connection refused:\*\*

```wp-block-code
sudo systemctl status sshd        # Is it running?
sudo firewall-cmd --list-services  # Is SSH allowed?
```

\*\*Permission denied:\*\*

Check file permissions:

```wp-block-code
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

\*\*Slow connection:\*\*

DNS reverse lookup can cause delays. Add to `sshd_config`:

```wp-block-code
UseDNS no
```

\*\*Check SSH logs:\*\*

```wp-block-code
sudo journalctl -u sshd --since "1 hour ago"
```

\## SSH Host Keys

When you first connect to a Fedora server, SSH verifies the host fingerprint:

```wp-block-code
The authenticity of host '192.168.1.100' can't be established.
ED25519 key fingerprint is SHA256:xxxxx.
Are you sure you want to continue connecting (yes/no)?
```

Type `yes` to accept. The fingerprint is saved in `~/.ssh/known_hosts`.

If you reinstall Fedora or change the host keys, you’ll see a warning:

```wp-block-code
WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!
```

Remove the old key:

```wp-block-code
ssh-keygen -R 192.168.1.100
```

Then reconnect and accept the new fingerprint.

\## Using SSH Config for Convenience

Instead of typing full connection strings every time, configure shortcuts in `~/.ssh/config`:

```wp-block-code
Host fedora
    HostName 192.168.1.100
    User alice
    Port 2222
    IdentityFile ~/.ssh/id_ed25519
    ForwardAgent yes
```

Now connect with just:

```wp-block-code
ssh fedora
```

You can also configure multiplexing to reuse connections:

```wp-block-code
Host *
    ControlMaster auto
    ControlPath ~/.ssh/sockets/%r@%h-%p
    ControlPersist 600
```

```wp-block-code
mkdir -p ~/.ssh/sockets
```

This keeps connections alive for 10 minutes after you disconnect, making subsequent connections instant.
