---
title: "Setting Up a SOCKS5 Proxy on iOS via SSH Tunnel"
date: 2013-08-03 08:09:04 +0000
modified: 2026-04-11 16:40:58 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-configure-ios-for-iphone-and-ipad-to-use-socks-proxy-created-by-ssh/
---

iOS doesn’t expose SOCKS proxy settings in the Settings UI, but it supports Proxy Auto-Config (PAC) files natively. This lets you route iOS traffic through an SSH tunnel on a Linux/Unix host without installing a VPN app.

## Prerequisites

- iOS device (iPhone/iPad) on WiFi
- Linux/Unix host (same network or internet-accessible) with SSH access
- Web server to host the PAC file
- SSH SOCKS tunnel listening on a network-accessible interface

## Set Up the SSH SOCKS Tunnel

First, create a SOCKS5 proxy on your Linux/Unix host. For local testing on the same network:

``` bash
ssh -D 0.0.0.0:1080 -f -C -q -N user@remote-host
```

This opens port 1080 on all interfaces. The flags mean:

- `-D 0.0.0.0:1080` — bind SOCKS proxy to all interfaces on port 1080
- `-f` — fork to background
- `-C` — enable compression
- `-q` — quiet mode
- `-N` — don’t execute a remote command

For better security, use the server’s `GatewayPorts` SSH option instead of binding to 0.0.0.0, or restrict to specific IPs with firewall rules.

If your iOS device and Linux host are on different networks, tunnel through a jump host or use `-L` for local port forwarding and expose that locally.

## Create a PAC File

Proxy Auto-Config is JavaScript that tells clients which proxy to use. Create `proxy.pac`:

``` javascript
function FindProxyForURL(url, host) {
    return "SOCKS5 proxy-host:1080";
}
```

Replace `proxy-host` with the actual IP or hostname of your Linux box.

For selective routing (only certain domains through the proxy):

``` javascript
function FindProxyForURL(url, host) {
    var proxy = "SOCKS5 proxy-host:1080";
    var direct = "DIRECT";

    // Route internal domains through proxy
    if (host.indexOf("internal.example.com") !== -1 ||
        host.indexOf("api.internal") !== -1) {
        return proxy;
    }

    // Skip private networks
    if (host.match(/^(10\.|192\.168\.|172\.1[6-9]\.|172\.2[0-9]\.|172\.3[01]\.)/)) {
        return direct;
    }

    // Everything else direct
    return direct;
}
```

## Host the PAC File

Deploy the PAC file on any web server accessible from your iOS device.

**Python 3 (quick local testing):**

``` bash
python3 -m http.server 8000 --directory /path/to/pac/files
```

**Nginx (production):**

``` nginx
server {
    listen 80;
    server_name proxy.local;

    location / {
        root /var/www;
        types {
            application/x-ns-proxy-autoconfig pac;
            text/plain txt;
        }
    }
}
```

**Node.js alternative:**

``` bash
npx http-server -p 8000 -c-1
```

Verify the PAC file is accessible at `http://proxy-host:8000/proxy.pac` or whatever URL you’re using.

## Configure iOS WiFi to Use the PAC File

On your iOS device:

1.  Go to **Settings → Wi-Fi**
2.  Tap the **ⓘ** icon next to your connected network
3.  Scroll to **HTTP Proxy**
4.  Select **Automatic**
5.  Enter the PAC URL: `http://proxy-host:8000/proxy.pac`
6.  Tap **Save**

iOS fetches and applies the PAC immediately. The configuration applies to all traffic on that WiFi network only.

## Verify the Setup

Check that traffic routes through the proxy:

**From the iOS device:**

- Visit `https://whatismyipaddress.com` or `https://ipleak.net` and confirm the IP matches your SSH tunnel origin
- Use a test app that shows your outbound IP

**From the Linux host:**

- Monitor the SSH tunnel: `watch -n 1 'ss -tuln | grep 1080'`
- Check active SSH connections: `ps aux | grep socks`
- Monitor SSH logs: `journalctl -u ssh -f` (if using systemd)

**From another device on the network:**

``` bash
curl -x socks5://proxy-host:1080 https://example.com
```

## Troubleshooting

**PAC file won’t load**

- Open the PAC URL directly in Safari. If it fails, the server isn’t reachable.
- Confirm the URL format (use `http://`, not `https://`, unless you’ve configured TLS)
- Check firewall rules on the Linux host blocking the web server port

**Wrong MIME type errors**

- Ensure your web server sends `application/x-ns-proxy-autoconfig` for `.pac` files, or fallback to `text/plain`
- Test with curl: `curl -i http://proxy-host:8000/proxy.pac | head -5`

**Proxy not actually being used**

- Verify `proxy-host:1080` in the PAC file is reachable from the iOS device: `nslookup proxy-host` and `nc -zv proxy-host 1080` from another device on the same network
- PAC files control HTTP/HTTPS traffic only. Other protocols (DNS, app-specific) may bypass the proxy.

**DNS leaks**

- PAC files don’t intercept DNS queries by default. If privacy is critical, also configure DNS over HTTPS in iOS Settings → Privacy, or tunnel all traffic through the SSH connection with a VPN wrapper.

**IPv6 compatibility**

- If `proxy-host` resolves to IPv6, ensure your SOCKS tunnel listens on IPv6:

``` bash
ssh -D [::]:1080 -f -C -q -N user@remote-host
```

Or bind to both:

``` bash
ssh -D 0.0.0.0:1080 -D [::]:1080 -f -C -q -N user@remote-host
```

## Production Considerations

- **HTTPS PAC delivery:** Host the PAC file behind TLS to prevent interception, especially on untrusted networks
- **SSH key authentication:** Use SSH keys instead of passwords. Configure SSH to not require a password prompt:

``` bash
ssh -i /path/to/key -D 0.0.0.0:1080 -f -C -q -N user@remote-host
```

- **MDM deployment:** For fleet management, use Mobile Device Management to distribute the PAC URL automatically
- **Persistence:** The PAC configuration persists per WiFi network. You’ll need to reconfigure for other networks.
- **Monitoring:** Log SOCKS5 traffic with tools like `tcpdump` or enable verbose SSH logging if needed
