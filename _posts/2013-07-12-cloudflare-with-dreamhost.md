---
title: "Configuring Cloudflare DNS with DreamHost"
date: 2013-07-12 16:46:16 +0000
author: "Eric Ma"
layout: post
categories: [system-administration-cloud]
canonical: /cloudflare-with-dreamhost/
---

Cloudflare is a widely-used CDN and DDoS mitigation service that caches content globally and improves performance. DreamHost offers native integration, though understanding the DNS setup—particularly for apex domains—is critical for avoiding routing issues.

## Quick Setup Through DreamHost Control Panel

The fastest path for most domains:

1.  Log into your DreamHost account
2.  Navigate to **Domains → Manage Domains**
3.  Click **Edit** in the Web Hosting column for your domain
4.  Enable Cloudflare and click **Change settings**
5.  DreamHost automatically updates nameservers

You’ll receive a confirmation email from Cloudflare once provisioned. Log into your Cloudflare account to configure caching rules, security settings, and additional features.

## Understanding DNS Propagation

DNS changes typically propagate within 24 hours globally, though major nameserver changes can take up to 48 hours in some regions. You can check propagation status with:

``` bash
dig example.com NS +short
nslookup -type=NS example.com
```

Both commands should return Cloudflare’s nameservers after setup completes.

## The Apex Domain Problem: CNAME vs. Nameserver Setup

DreamHost’s default integration uses CNAME records, which creates a significant limitation. RFC standards prohibit CNAME records at the DNS apex (root domain):

    www.example.com CNAME example.com.cloudflare.net  ✓ Valid
    example.com CNAME example.com.cloudflare.net       ✗ Invalid per RFC 1035

If you only need `www.example.com` proxied through Cloudflare, DreamHost’s default setup works fine. However, if you need the bare apex domain (`example.com`) cached and secured by Cloudflare, you must use full nameserver delegation instead of CNAME.

## Full Cloudflare Setup for Apex Domain Support

To proxy both `example.com` and `www.example.com`:

1.  In your domain registrar (or DreamHost if they’re your registrar), change your nameservers to Cloudflare’s:

    - `ben.ns.cloudflare.com`
    - `lara.ns.cloudflare.com`

2.  In your Cloudflare dashboard, add DNS records pointing to DreamHost:

        Type  | Name           | Content              | TTL
        A     | example.com    | <DreamHost IP>       | Auto
        A     | www            | <DreamHost IP>       | Auto
        CNAME | mail           | mail.dreamhost.com   | Auto (if needed)

3.  Find your DreamHost IP address by:

    - Checking the DreamHost control panel under **Domains → Manage Domains → Edit**
    - Looking for “Web Server IP”
    - Or running: `dig example.com A +short` before changing nameservers

4.  Wait 24-48 hours for nameserver propagation

5.  Verify with:

    ``` bash
    dig example.com NS +short
    # Should return Cloudflare nameservers
    dig example.com A +short
    # Should return your DreamHost IP
    ```

## Performance and Security Configuration

Once active, configure Cloudflare’s features:

**Caching:**

- Enable **Auto Minify** for CSS, JavaScript, and HTML
- Enable **Brotli compression** for text-based assets
- Set **Cache Level** to “Cache Everything” for static sites, or “Standard” for dynamic content
- Configure **Browser Cache TTL** based on your update frequency

**Security:**

- Set **Security Level** to “Medium” or “High”
- Enable **WAF (Web Application Firewall)** rules
- Configure **Rate Limiting** to prevent brute-force attacks
- Review **Security Events** in the dashboard regularly

**Performance:**

- Verify **HTTP/2** and **HTTP/3** are enabled under **Network**
- Test with: `curl -I --http2 https://example.com`

## Cache Management

Cloudflare caches static assets automatically. Purge cache after deployments:

``` bash
# Manual purge via API (requires API token from Cloudflare dashboard)
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '{"files":["https://example.com/style.css"]}'

# Purge everything
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '{"purge_everything":true}'
```

Find your `zone_id` in the Cloudflare dashboard under **Account Home → API Tokens**.

## Monitoring and Troubleshooting

Check Cloudflare’s **Analytics** dashboard for cache hit rates, DDoS events, and performance metrics. A healthy setup shows cache hit ratios above 70% for static-heavy sites.

If traffic isn’t being routed correctly after setup, verify:

- Nameservers are fully propagated: `dig example.com NS +short`
- DreamHost IP is correct in Cloudflare DNS records
- SSL/TLS mode is set appropriately (Full for DreamHost-hosted sites)
- No conflicting DNS records in both systems

If you revert to DreamHost nameservers, remove all Cloudflare DNS records from the nameserver setup to avoid conflicts.
