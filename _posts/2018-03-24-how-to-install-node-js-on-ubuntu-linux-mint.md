---
title: "Installing Node.js on Ubuntu and Linux Mint"
date: 2018-03-24 11:43:34 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-install-node-js-on-ubuntu-linux-mint/
---

Node.js installation on Ubuntu and Linux Mint has evolved significantly. The approach depends on your use case — whether you need the latest stable version, multiple Node versions for different projects, or just a quick setup.

## Using the NodeSource Repository (Recommended)

The NodeSource repository provides current, well-maintained Node.js packages. This is the best approach for most production systems.

First, add the NodeSource repository. For Node.js 20 LTS (the current stable long-term support version):

``` bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt update
sudo apt install nodejs
```

For Node.js 22 (current release):

``` bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt update
sudo apt install nodejs
```

This installs both `node` and `npm`. The `node` command works directly without requiring a separate legacy package.

## Using Ubuntu’s Default Repositories

If you prefer to avoid third-party repositories:

``` bash
sudo apt update
sudo apt install nodejs npm
```

This works, but the packages are typically 1–2 versions behind. It’s suitable for development machines where you don’t need cutting-edge features.

## Managing Multiple Node Versions with nvm

For development work with multiple projects requiring different Node versions, use the Node Version Manager:

``` bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.bashrc
nvm install 20
nvm install 22
nvm use 20
```

Check your active version:

``` bash
node --version
npm --version
```

Switch between versions as needed:

``` bash
nvm use 22
```

## Verifying Your Installation

After installation, confirm everything works:

``` bash
node -v
npm -v
npm list -g
```

The last command shows globally installed packages.

## Updating Node.js

**With NodeSource repository:**

``` bash
sudo apt update
sudo apt upgrade nodejs
```

**With nvm:**

``` bash
nvm install node  # installs latest
nvm install 20    # installs latest 20.x
nvm alias default 20
```

**With default packages:**

``` bash
sudo apt update
sudo apt upgrade nodejs npm
```

## Installing Global Packages

Once installed, you can install global tools like PM2 for process management or Yarn for package management:

``` bash
npm install -g pm2
npm install -g yarn
```

View globally installed packages:

``` bash
npm list -g --depth=0
```

## Cleaning Up

If you’ve installed Node multiple ways and want to remove it:

``` bash
sudo apt remove nodejs npm
```

Then, if you used NodeSource or nvm, remove those configurations from your shell profile (`~/.bashrc` or `~/.zshrc`).

## Quick Comparison

- **NodeSource repository**: Best for production servers; recent versions; easy updates
- **Default packages**: Simpler setup; stable but older versions
- **nvm**: Essential for developers working with multiple Node versions; project-specific version management

Choose NodeSource for most server deployments, and nvm if you juggle multiple projects with varying requirements.

## 2026 Best Practices and Advanced Techniques

For Installing Node.js on Ubuntu and Linux Mint, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling and keep-alive for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for system resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for real-time monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
