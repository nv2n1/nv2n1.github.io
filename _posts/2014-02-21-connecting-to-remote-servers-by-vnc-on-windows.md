---
title: "Securing VNC Access to Linux Servers Using SSH Tunneling"
date: 2014-02-21 07:36:37 +0000
author: "Weiwei Jia"
layout: post
categories: [linux-systems-administration]
canonical: /connecting-to-remote-servers-by-vnc-on-windows/
---

VNC provides graphical remote access to Linux servers. For security, tunnel VNC traffic through SSH rather than expose it directly to the network. This guide covers Windows client setup with SSH tunneling.

## Prerequisites

**Windows client:**

- SSH client: Native OpenSSH (built into Windows 10/11) or PuTTY
- VNC viewer: RealVNC Viewer, TigerVNC Viewer, or TightVNC Viewer

**Linux server:**

- SSH server running and accessible
- VNC server: TigerVNC or TightVNC
- Lightweight desktop environment: XFCE, LXDE, or Openbox

## Server Installation

Install the VNC server and desktop environment.

**Fedora/RHEL/CentOS:**

``` bash
sudo dnf install tigervnc-server xfce4-session xfce4-terminal xfce4-panel
```

**Debian/Ubuntu:**

``` bash
sudo apt install tigervnc-server xfce4-session xfce4-terminal xfce4-panel
```

**Arch:**

``` bash
sudo pacman -S tigervnc xfce4
```

## Server Configuration

Set a VNC password:

``` bash
vncpasswd
```

Create the VNC startup script:

``` bash
mkdir -p ~/.vnc
cat > ~/.vnc/xstartup << 'EOF'
#!/bin/bash
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
exec startxfce4 &
EOF
chmod +x ~/.vnc/xstartup
```

Start the VNC server on display `:1`:

``` bash
vncserver :1 -geometry 1920x1080 -depth 24
```

Verify it’s listening on localhost:5901 (port 5900 + display number):

``` bash
ss -tlnp | grep vnc
```

## SSH Tunnel from Windows

### Using OpenSSH (Built-in, Windows 10/11+)

Open PowerShell and create the SSH tunnel:

``` powershell
ssh -L 5901:localhost:5901 user@your.server.com -N
```

The `-N` flag prevents remote command execution. Keep this terminal open while using VNC.

In another PowerShell window or directly in your VNC viewer, connect to `localhost:5901` and enter your VNC password.

### Using PuTTY (Alternative)

1.  Open PuTTY and enter server hostname and SSH port
2.  Navigate to **Connection → SSH → Tunnels**
3.  In “Source port”, enter `5901`
4.  In “Destination”, enter `localhost:5901`
5.  Click **Add**
6.  Click **Open** and authenticate

## Connecting with VNC Viewer

Once the SSH tunnel is active, open your VNC viewer:

1.  Set connection address to `localhost:5901`
2.  Enter your VNC password
3.  Click **Connect**

## Auto-Starting VNC with Systemd

For unattended servers or to auto-start VNC on boot, create a user-level systemd service:

``` bash
mkdir -p ~/.config/systemd/user
cat > ~/.config/systemd/user/vncserver.service << 'EOF'
[Unit]
Description=TigerVNC Server
After=syslog.target network.target

[Service]
Type=forking
ExecStart=/usr/bin/vncserver :1 -geometry 1920x1080 -depth 24
ExecStop=/usr/bin/vncserver -kill :1
Restart=on-failure

[Install]
WantedBy=default.target
EOF
```

Enable and start:

``` bash
systemctl --user enable vncserver
systemctl --user start vncserver
```

For system-wide startup (requires root), place the service in `/etc/systemd/system/` instead.

## Stopping VNC

Kill the VNC session:

``` bash
vncserver -kill :1
```

## Troubleshooting

Check the VNC log for connection errors:

``` bash
cat ~/.vnc/localhost:1.log
```

If VNC server fails to start, verify the display isn’t already in use:

``` bash
ps aux | grep vncserver
```

## Security Best Practices

- **Always tunnel through SSH** — never expose VNC directly to the network

- **Use strong VNC passwords** — treat them like SSH passphrases

- **Disable password SSH authentication** — use key-based authentication instead:

  ``` bash
  ssh -i ~/.ssh/id_ed25519 -L 5901:localhost:5901 user@your.server.com -N
  ```

- **Restrict SSH access** — use firewall rules or security groups to limit SSH connections

- **Monitor logs** — check `~/.vnc/localhost:*.log` and `/var/log/auth.log` regularly

- **Set VNC display timeout** — add `-SecurityTypes VncAuth` to require authentication and consider using VNC-only mode with limited idle timeouts

## Multiple Concurrent Sessions

To run multiple VNC sessions on the same server, use different display numbers:

``` bash
vncserver :2 -geometry 1920x1080 -depth 24
vncserver :3 -geometry 1920x1080 -depth 24
```

Tunnel each to a different local port from Windows:

``` powershell
ssh -L 5901:localhost:5901 -L 5902:localhost:5902 user@your.server.com -N
```

Then connect VNC viewers to `localhost:5901` and `localhost:5902` respectively.
