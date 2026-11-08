---
title: "SSH Tunneling on Windows: Creating a SOCKS Proxy with OpenSSH"
date: 2013-07-15 13:01:08 +0000
modified: 2026-04-11 17:41:32 +0000
author: "Eric Ma"
layout: post
categories: [scripting-utilities]
canonical: /proxy-using-ssh-tunnel-on-windows/
---

SSH tunneling on Windows routes your traffic through a remote server over an encrypted connection, letting you bypass network restrictions and access resources as if you were on the remote network. The setup creates a SOCKS proxy that listens locally and forwards all traffic through the SSH tunnel.

The traffic flow is straightforward:

Your application → localhost:8080 (SOCKS proxy) → SSH tunnel → Remote server → Internet

## Native OpenSSH (Recommended)

Windows 10/11 includes OpenSSH natively, making it the simplest option. No additional software needed.

Open PowerShell or Command Prompt and run:

``` bash
ssh -D 8080 -C -N user@example.com
```

Flag breakdown:

- `-D 8080`: Creates a SOCKS proxy listening on localhost:8080
- `-C`: Enables compression (reduces bandwidth usage)
- `-N`: Doesn’t execute a remote command, just forwards ports
- `-p 2222`: Use this if your SSH server runs on a non-standard port

The terminal will hang — this is expected. Keep it running to maintain the tunnel.

Using a private key instead of a password:

``` bash
ssh -D 8080 -C -N -i C:\Users\YourName\.ssh\id_rsa user@example.com
```

For non-standard ports:

``` bash
ssh -D 8080 -C -N -p 2222 user@example.com
```

### Running in the Background

To avoid keeping a terminal open indefinitely, create a batch file:

```batch
@echo off
start "" ssh -D 8080 -C -N -o ServerAliveInterval=60 user@example.com
```

Save as `tunnel.bat`. The `start` command launches SSH in a background process. The `ServerAliveInterval=60` sends keepalive packets every 60 seconds to prevent idle disconnections.

Alternatively, use Windows Task Scheduler to run the SSH command at startup with the “Run whether user is logged in or not” option, though this requires storing credentials carefully.

## Using PuTTY (GUI Alternative)

If you prefer a graphical interface, PuTTY still works well:

1.  Download from <a href="https://www.chiark.greenend.org.uk/~sgtatham/putty/" rel="nofollow noopener" target="_blank">the official site</a>
2.  Launch PuTTY and configure:
    - **Session tab**: Enter hostname and port (default 22)
    - **Connection → SSH → Tunnels**:
      - Source port: `8080`
      - Destination: Leave blank
      - Type: Select `Dynamic`
      - Click `Add` (shows `D8080` in the list)
3.  **Session tab**: Save the configuration with a name like “SSH Tunnel” for reuse
4.  Click `Open` and authenticate

The tunnel runs as long as PuTTY stays open. For persistent background operation, use PuTTY’s command-line mode or switch to native OpenSSH.

## Configuring Applications to Use the Proxy

Once the tunnel is active on localhost:8080, configure your applications:

### Firefox

Settings → Network Settings → Manual proxy configuration:

- SOCKS Host: `localhost`
- Port: `8080`
- SOCKS v5: enabled

### Chrome, Chromium, Edge

These browsers ignore Windows proxy settings. Launch with a command-line flag instead:

``` bash
chrome.exe --proxy-server="socks5://localhost:8080"
```

Create a shortcut with this target:

    C:\Program Files\Google\Chrome\Application\chrome.exe --proxy-server="socks5://localhost:8080"

For Chromium:

``` bash
chromium.exe --proxy-server="socks5://localhost:8080"
```

### Command-Line Tools

**curl:**

``` bash
curl --socks5 localhost:8080 https://example.com
```

**wget:**

``` bash
wget -e https_proxy=socks5://localhost:8080 https://example.com
```

**git:**

``` bash
git config --global http.proxy socks5://localhost:8080
git config --global https.proxy socks5://localhost:8080
```

To unset git proxy:

``` bash
git config --global --unset http.proxy
git config --global --unset https.proxy
```

## Keeping the Tunnel Alive

SSH connections idle out after extended periods. Add keepalive to prevent disconnections:

``` bash
ssh -D 8080 -C -N -o ServerAliveInterval=60 -o ServerAliveCountMax=3 user@example.com
```

- `ServerAliveInterval=60`: Sends a keepalive packet every 60 seconds
- `ServerAliveCountMax=3`: Closes the connection if 3 keepalive packets go unanswered

In PuTTY, set this under Connection → Seconds between keepalives.

## Generating SSH Keys for Automation

For scripts or permanent setups, use key-based authentication:

``` bash
ssh-keygen -t ed25519 -f C:\Users\YourName\.ssh\id_rsa -N ""
```

The `-N ""` flag skips the passphrase (useful for automation). Then add the public key to your remote server:

``` bash
cat C:\Users\YourName\.ssh\id_rsa.pub | ssh user@example.com "cat >> ~/.ssh/authorized_keys"
```

Now connect without a password:

``` bash
ssh -D 8080 -C -N -i C:\Users\YourName\.ssh\id_rsa user@example.com
```

## Troubleshooting

### Port 8080 already in use

Check what’s using the port:

``` bash
netstat -ano | findstr :8080
```

Use a different port (9090, 1080, etc.) in both your SSH command and application settings.

### Connection fails immediately

Verify SSH connectivity first with verbose output:

``` bash
ssh -v user@example.com
```

Check that:

- Port 22 isn’t blocked by your firewall
- The remote server is reachable and accepts SSH connections
- Your credentials are correct

### Application ignores proxy settings

Some apps have their own proxy configuration separate from Windows settings. Check the application’s preferences directly — Firefox, for example, has its own proxy settings that override system defaults. Chrome requires the command-line flag; it won’t read Windows proxy settings.

### No internet through the proxy

Test with a command-line tool first:

``` bash
curl --socks5 localhost:8080 https://httpbin.org/ip
```

If this returns your remote server’s IP, the tunnel works. If it fails, the tunnel is misconfigured. If it works but your browser doesn’t, the issue is with application proxy settings.

## Security Considerations

- Only tunnel through SSH servers you fully trust — unencrypted proxied traffic is visible to the remote server’s operator
- SSH keys are more secure than passwords for remote access
- If the remote server is compromised, so is your proxied traffic — don’t treat this as a VPN replacement for sensitive work on untrusted networks
- For public WiFi, a proper VPN is more appropriate than SSH tunneling alone
- Monitor your tunnel connection and close it when not needed — leaving it open indefinitely increases your exposure window
- Consider using a bastion host or jump server as an intermediary for additional security

SSH tunneling is lightweight, requires no additional software on modern Windows, and works reliably for temporary proxy needs or accessing resources on remote networks.
