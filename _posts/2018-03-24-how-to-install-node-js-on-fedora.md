---
title: "Installing Node.js on Fedora: DNF and Alternative Methods"
date: 2018-03-24 11:43:34 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-install-node-js-on-fedora/
---

Node.js is available on Fedora through the DNF package manager and several alternative methods. Here’s how to install it using each approach.

## Method 1: DNF (System Package Manager)

The simplest method — install Node.js directly from Fedora’s repositories:

```wp-block-code
sudo dnf install nodejs npm
```

Check the installed version:

```wp-block-code
node --version
npm --version
```

Fedora’s repositories typically include a recent but not always latest version of Node.js. For the current LTS or latest release, use one of the alternative methods below.

## Method 2: NodeSource Repository

NodeSource provides up-to-date Node.js packages for Fedora:

```wp-block-code
# Install Node.js 22.x (current LTS)
sudo dnf install -y curl
curl -fsSL https://rpm.nodesource.com/setup_22.x | sudo bash -
sudo dnf install -y nodejs

# Or install Node.js 20.x (previous LTS)
curl -fsSL https://rpm.nodesource.com/setup_20.x | sudo bash -
sudo dnf install -y nodejs
```

This method gives you the latest patch releases within the selected major version.

## Method 3: NVM (Node Version Manager)

NVM lets you install and switch between multiple Node.js versions per user — no root required:

```wp-block-code
# Install NVM
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash

# Reload shell
source ~/.bashrc

# Install latest LTS
nvm install --lts

# Install specific version
nvm install 22.0.0

# Switch versions
nvm use 20

# Set default version
nvm alias default 22

# List installed versions
nvm ls
```

NVM is ideal for developers who work on multiple projects requiring different Node.js versions.

## Method 4: FnM (Fast Node Manager)

FnM is a Rust-based alternative to NVM with faster version switching:

```wp-block-code
# Install FnM
curl -fsSL https://fnm.vercel.app/install | bash

# Install and use latest LTS
fnm install --lts
fnm use --lts

# Use .node-version or .nvmrc for per-project versions
fnm use
```

## Method 5: Flatpak

For sandboxed Node.js development:

```wp-block-code
flatpak install flathub org.freedesktop.Sdk.Extension.node22
```

## Global npm Packages Without Sudo

When using DNF-installed Node.js, global npm installs require sudo. Fix this by changing npm’s prefix:

```wp-block-code
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

Now `npm install -g` works without root and installs to your home directory.

## Choosing the Right Method

- **DNF** — Simple, system-wide, good for servers running a single Node.js version
- **NodeSource** — Latest versions, system-wide, good for production servers
- **NVM/FnM** — Multiple versions, per-user, best for development workstations
- **Flatpak** — Sandboxed, least common, for security-sensitive environments

For most Fedora users, NVM provides the best development experience. For production servers, NodeSource gives you controlled, up-to-date system-wide installations.

## Running Node.js as a System Service

For production deployments, run Node.js applications as systemd services:

```wp-block-code
# /etc/systemd/system/myapp.service
[Unit]
Description=My Node.js Application
After=network.target

[Service]
Type=simple
User=nodeapp
WorkingDirectory=/opt/myapp
ExecStart=/usr/bin/node /opt/myapp/server.js
Restart=on-failure
RestartSec=10
Environment=NODE_ENV=production
Environment=PORT=3000

[Install]
WantedBy=multi-user.target
```

Enable and start the service:

```wp-block-code
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
sudo systemctl status myapp
```

View application logs:

```wp-block-code
sudo journalctl -u myapp -f
```

## Using PM2 for Process Management

PM2 provides advanced process management for Node.js applications with clustering, monitoring, and zero-downtime reloads:

```wp-block-code
# Install PM2
npm install -g pm2

# Start an application with cluster mode
pm2 start server.js -i max --name "myapp"

# Enable auto-restart on system reboot
pm2 startup systemd
pm2 save

# Monitor processes
pm2 monit

# Zero-downtime reload
pm2 reload myapp

# View logs
pm2 logs myapp
```

PM2’s cluster mode spawns multiple Node.js processes across all CPU cores, significantly improving throughput for CPU-bound workloads.
