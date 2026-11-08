---
title: "Configuring Zimbra Web Service Hostname and Port"
date: 2018-03-24 11:52:43 +0000
author: "Eric Ma"
layout: post
categories: [web-development]
canonical: /how-to-set-zimbra-web-services-hostname-and-port/
---

Zimbra’s web interface needs proper hostname and port configuration to function correctly, especially when you’re deploying behind load balancers, reverse proxies, or in clustered environments.

## Viewing Current Configuration

Check your current Zimbra web service hostname and port settings:

``` bash
zmprov getServer $(zmhostname) zimbraMailPort
zmprov getServer $(zmhostname) zimbraMailSSLPort
zmprov getServer $(zmhostname) zimbraAdminPort
```

You can also query the hostname:

``` bash
zmprov getServer $(zmhostname) zimbraServiceHostname
```

## Setting the Hostname

To set the hostname that clients will use to connect to your Zimbra server:

``` bash
zmprov modifyServer $(zmhostname) zimbraServiceHostname mail.example.com
```

Replace `mail.example.com` with your actual hostname. This value appears in Zimbra’s auto-discovery responses and client configuration.

## Changing the Web Service Port

Zimbra uses port 80 for HTTP and 443 for HTTPS by default. To change the HTTP port:

``` bash
zmprov modifyServer $(zmhostname) zimbraMailPort 8080
```

For HTTPS (recommended for production):

``` bash
zmprov modifyServer $(zmhostname) zimbraMailSSLPort 8443
```

For the admin interface (default 7071):

``` bash
zmprov modifyServer $(zmhostname) zimbraAdminPort 7071
```

## Restarting Services

After making changes, restart Zimbra services to apply the new configuration:

``` bash
zmcontrol stop
zmcontrol start
```

Or restart only the web service:

``` bash
zmcontrol restart mailbox
```

Monitor the startup with:

``` bash
tail -f /var/log/zimbra.log
```

## Proxy and Load Balancer Scenarios

When running Zimbra behind a reverse proxy (nginx, Apache, HAProxy), you often need to:

1.  Keep the internal port unchanged (or document it clearly)
2.  Set `zimbraServiceHostname` to the external hostname clients will use
3.  Configure your proxy to forward requests appropriately

For example, if your external hostname is `mail.example.com:443` but Zimbra listens on `127.0.0.1:8080` internally:

``` bash
zmprov modifyServer $(zmhostname) zimbraServiceHostname mail.example.com
zmprov modifyServer $(zmhostname) zimbraMailPort 8080
```

Then configure your reverse proxy to listen on the external port and forward to the internal port.

## Verifying Changes

Confirm the settings took effect:

``` bash
zmprov getServer $(zmhostname) zimbraServiceHostname zimbraMailPort zimbraMailSSLPort
```

Test client connectivity using the hostname and port:

``` bash
curl -v https://mail.example.com:443/
```

Or from the Zimbra server itself:

``` bash
curl -v http://localhost:8080/
```

## Common Issues

**SSL certificate mismatches**: Ensure your certificate matches the hostname in `zimbraServiceHostname`. Zimbra’s auto-discovery checks this.

**Firewall rules**: Verify ports are open between clients and the Zimbra server. If running behind a proxy, ensure the proxy port is open externally.

**CAfile errors**: If using a custom certificate, ensure it’s properly installed in Zimbra’s keystore and the configuration points to it correctly.

Document any non-standard port assignments in your runbooks — future troubleshooting will be easier when ports are explicitly noted rather than assumed.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
