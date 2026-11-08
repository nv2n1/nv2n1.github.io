---
title: "Setting Up SSH Server on Windows 10, 11, and Server 2019"
date: 2013-07-12 16:54:47 +0000
layout: post
canonical: https://www.systutorials.com/set-up-ssh-server-on-windows-xp/
---

Running an SSH server on Windows enables remote administration, port forwarding, and integration with Unix-like workflows. Modern Windows provides native OpenSSH support that’s far superior to legacy third-party solutions.

## Installation

Windows 10 (build 1809+), Windows 11, and Windows Server 2019+ include OpenSSH as an optional feature.

**Via Settings:**

1.  Open Settings → System → Optional features
2.  Click “Add an optional feature”
3.  Search for “OpenSSH Server”
4.  Click Install

**Via PowerShell (as Administrator):**

``` powershell
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
```

## Starting the Service

Enable and start OpenSSH Server:

``` powershell
Set-Service -Name sshd -StartupType Automatic
Start-Service -Name sshd
```

Verify it’s running:

``` powershell
Get-Service sshd
```

## Firewall Configuration

Allow SSH through Windows Defender Firewall:

``` powershell
New-NetFirewallRule -Name sshd -DisplayName "OpenSSH Server" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 22
```

Or manually: Settings → Privacy & Security → Firewall & network protection → Allow an app through firewall, then select OpenSSH Server.

## Basic Configuration

OpenSSH configuration lives in `C:\ProgramData\ssh\sshd_config`. Edit this file as Administrator to customize behavior.

**Default port:**

    Port 22

**Authentication methods:**

    PasswordAuthentication yes
    PubkeyAuthentication yes

**Default shell (PowerShell 7+ recommended):**

    Subsystem powershell C:\Program Files\PowerShell\7\pwsh.exe

For Windows PowerShell (built-in):

    Subsystem powershell C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe

After editing, validate syntax:

``` powershell
sshd -T
```

Then restart the service:

``` powershell
Restart-Service sshd
```

## Testing the Connection

From any client machine (Linux, macOS, or Windows):

``` bash
ssh username@windows-ip-address
```

Accept the host key fingerprint on first connection. This adds the host key to your local `known_hosts` file.

Check what port sshd is listening on:

``` powershell
netstat -ano | findstr :22
```

## Key-Based Authentication

**On your client machine, generate an Ed25519 key pair (if you don’t have one):**

``` bash
ssh-keygen -t ed25519 -C "your-email@example.com"
```

**Copy the public key to Windows:**

``` bash
cat ~/.ssh/id_ed25519.pub | ssh username@windows-ip-address "mkdir -p .ssh && cat >> .ssh/authorized_keys"
```

If that fails, manually place the public key content into `C:\Users\USERNAME\.ssh\authorized_keys` on Windows.

**Fix permissions on the .ssh directory and authorized_keys file:**

``` powershell
icacls C:\Users\USERNAME\.ssh /inheritance:r /grant:r "$env:USERNAME`:F"
icacls C:\Users\USERNAME\.ssh\authorized_keys /inheritance:r /grant:r "$env:USERNAME`:F"
```

OpenSSH on Windows enforces strict permission checking—overly permissive ACLs on `.ssh` or `authorized_keys` will cause authentication to fail silently.

## Disabling Password Authentication

For security-conscious deployments, disable passwords entirely and require key-based authentication:

    PasswordAuthentication no
    PubkeyAuthentication yes
    PermitEmptyPasswords no

Restart the service after editing:

``` powershell
Restart-Service sshd
```

## Restricting Login to Specific Users

    AllowUsers user1 user2 domain\user3

## Changing the Default Port

    Port 2222

Update your firewall rule:

``` powershell
Remove-NetFirewallRule -Name sshd
New-NetFirewallRule -Name sshd -DisplayName "OpenSSH Server" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 2222
```

Connect on the new port:

``` bash
ssh -p 2222 username@windows-ip-address
```

## Using Different Shells Per User

Define shell overrides with Match blocks:

    Match User adminuser
        Subsystem powershell C:\Program Files\PowerShell\7\pwsh.exe

    Match User serviceaccount
        Subsystem powershell C:\Windows\System32\cmd.exe /c

## Port Forwarding

**Local port forwarding** (access a remote service from your local machine):

``` bash
ssh -L 9000:internal-server:9000 username@windows-ip-address
```

Keep the tunnel alive without an interactive shell:

``` bash
ssh -N -L 9000:internal-server:9000 username@windows-ip-address
```

**Reverse port forwarding** (expose a local Windows service to a remote machine):

``` bash
ssh -R 8080:localhost:3000 username@remote-ip-address
```

This binds port 8080 on the remote machine to port 3000 on your local Windows box.

## Troubleshooting

**Connection refused or timeout:**

Verify the service is running and listening:

``` powershell
Get-Service sshd
netstat -ano | findstr :22
```

Check the firewall rule allows traffic on your configured port.

**Permission denied (publickey):**

Ensure `.ssh` directory and `authorized_keys` file have correct NTFS permissions. Re-run the `icacls` commands above. Verify that only your user owns these files:

``` powershell
icacls C:\Users\USERNAME\.ssh
icacls C:\Users\USERNAME\.ssh\authorized_keys
```

**Wrong shell launching:**

Verify the shell path exists and is specified correctly in `sshd_config`. Test the subsystem:

``` powershell
C:\Program Files\PowerShell\7\pwsh.exe
```

**sshd_config syntax error:**

Validate the config file:

``` powershell
sshd -T
```

This parses the config without starting the service and reports any syntax errors.

**Slow connection or timeout on login:**

Check for reverse DNS or GSSAPI issues. Disable GSSAPI authentication if not needed:

    GSSAPIAuthentication no

## Unsupported Windows Versions

Windows XP, Vista, Server 2003, and other versions beyond mainstream support should not run SSH. These systems lack security updates and are unsuitable for any network-facing service.

If upgrading is impossible and SSH is absolutely necessary, third-party options like Bitvise SSH Server exist but lack the security maintenance and hardening of native OpenSSH. This should only be a temporary workaround in isolated environments.

For Linux-based SSH alternatives, consider running a lightweight Linux VM or WSL2 (Windows Subsystem for Linux 2) on supported Windows hosts.
