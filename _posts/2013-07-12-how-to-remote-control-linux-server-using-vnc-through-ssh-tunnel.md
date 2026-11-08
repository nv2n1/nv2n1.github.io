---
title: "Securing Linux VNC Access with SSH Tunneling"
date: 2013-07-12 16:31:51 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-remote-control-linux-server-using-vnc-through-ssh-tunnel/
---

Accessing a remote desktop environment on a Linux server securely requires proper tunneling. While SSH X11 forwarding works for single applications, VNC provides a full graphical desktop session. By combining VNC with an SSH tunnel, you encrypt all traffic and can work around firewall restrictions that only allow port 22.

## Why VNC Over SSH?

VNC (Virtual Network Computing) sends unencrypted traffic by default, making it unsuitable for untrusted networks. Tunneling through SSH solves this:

- All VNC traffic is encrypted within the SSH connection
- Works when only SSH port (22) is open on the server
- Maintains persistent desktop sessions across disconnects
- Supports multiple simultaneous displays on one server

## Installation

On the remote server, install a VNC server. Distributions vary in packaging:

**Ubuntu/Debian:**

``` bash
sudo apt update
sudo apt install tigervnc-server
```

**RHEL/CentOS/Fedora:**

``` bash
sudo dnf install tigervnc-server
```

**Arch:**

``` bash
sudo pacman -S tigervnc
```

TigerVNC is the modern standard, offering better performance and security than older options. It replaces the deprecated TightVNC.

On your client machine, install a VNC viewer:

``` bash
# Ubuntu/Debian
sudo apt install tigervnc-viewer

# macOS (via Homebrew)
brew install tigervnc-viewer

# Or use platform-independent options like RealVNC Viewer
```

## Setting Up the SSH Tunnel and VNC Server

### Step 1: Create SSH Tunnel with Port Forwarding

The SSH tunnel forwards a local port to the remote VNC server. Here’s the command:

``` bash
ssh -L 5901:localhost:5901 username@remote-server.com
```

Breaking this down:

- `-L 5901:localhost:5901` creates a local tunnel
- Port 5901 on your client forwards to port 5901 on the remote server
- Traffic passes through SSH, encrypted end-to-end

Keep this terminal open while using VNC. For background operation, add the `-N` flag:

``` bash
ssh -L 5901:localhost:5901 -N username@remote-server.com
```

To create multiple displays, forward additional ports:

``` bash
ssh -L 5901:localhost:5901 -L 5902:localhost:5902 -N username@remote-server.com
```

### Step 2: Start VNC Server on Remote Machine

SSH to the remote server separately (or in another terminal if not using `-N`):

``` bash
ssh username@remote-server.com
```

Set a VNC password if you haven’t already:

``` bash
vncpasswd
```

Start the VNC server:

``` bash
vncserver
```

Output will show:

    New 'remote-server:1 (username)' desktop is remote-server:1

    Starting applications specified in /home/username/.vnc/xstartup
    Log file is /home/username/.vnc/remote-server:1.log

Each display gets a port: display 1 uses port 5901, display 2 uses 5902, and so on (port = 5900 + display number).

To specify display number and resolution explicitly:

``` bash
vncserver :1 -geometry 1920x1080 -depth 24
```

### Step 3: Connect with VNC Viewer

From your client machine, connect to the forwarded port:

``` bash
vncviewer localhost:5901
```

When prompted, enter the VNC password you set earlier. Your remote desktop now appears locally.

## Configuration Best Practices

### Custom Window Manager

The default FVWM is minimal. Configure `~/.vnc/xstartup` for a better environment:

``` bash
#!/bin/bash
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
exec startxfce4 &
```

Make it executable:

``` bash
chmod +x ~/.vnc/xstartup
```

Then kill and restart the VNC server:

``` bash
vncserver -kill :1
vncserver :1
```

### Persistent VNC Sessions

For VNC to start on reboot, use systemd:

Create `/etc/systemd/system/vncserver@.service`:

``` ini
[Unit]
Description=Remote desktop service (VNC)
After=syslog.target network-online.target remote-fs.target nss-lookup.target
Wants=network-online.target

[Service]
Type=forking
User=%i
WorkingDirectory=%h

ExecStartPre=-/usr/bin/vncserver -kill :%i > /dev/null 2>&1
ExecStart=/usr/bin/vncserver -autokill -SecurityTypes VncAuth -PasswordFile %h/.vnc/passwd :%i
ExecStop=/usr/bin/vncserver -kill :%i

[Install]
WantedBy=multi-user.target
```

Enable and start:

``` bash
sudo systemctl enable vncserver@1
sudo systemctl start vncserver@1
```

## Security Considerations

- **SSH keys:** Use SSH key authentication instead of passwords for better security
- **Firewall:** Never expose VNC ports directly; always use SSH tunneling
- **VNC password:** Set a strong password with `vncpasswd`
- **Display permissions:** VNC displays inherit user permissions; don’t run as root unless necessary

## Troubleshooting

**Connection refused:**

``` bash
# Verify SSH tunnel is active
ss -tlnp | grep 5901

# Check VNC server is running on remote
ps aux | grep vnc
```

**Slow performance:**

- Reduce color depth: `vncserver -depth 8`
- Lower resolution: `-geometry 1280x720`
- Compress with SSH: `ssh -C` flag

**Port already in use:**

``` bash
# Find which process owns the port
lsof -i :5901

# Use different display number
vncserver :2  # creates port 5902
```

## Cleanup

When finished, disconnect the VNC viewer, then stop the server:

``` bash
vncserver -kill :1
```

Substitute the correct display number if using a different one. The SSH tunnel closes when you exit the shell or terminate the `-N` process.
