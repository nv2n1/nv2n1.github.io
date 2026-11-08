---
title: "Query DNS Records from a Specific Server with dig"
date: 2018-03-24 11:46:25 +0000
author: "Eric Ma"
layout: post
categories: [programming-languages]
canonical: /how-to-resolve-a-domain-name-from-a-specific-dns-server-instead-of-the-configured-one-in-linux/
---

When you need to check DNS records from a particular server—especially to verify changes on authoritative nameservers before they propagate through cached resolvers—use `dig` with the `@` syntax to specify the target DNS server.

## Basic Syntax

``` bash
dig @DNS_SERVER domain.com
```

Replace `DNS_SERVER` with the IP address of the nameserver you want to query, and `domain.com` with your target domain.

## Practical Example

Query Google’s public DNS (8.8.8.8) for example.com:

``` bash
dig @8.8.8.8 example.com
```

This returns output similar to:

    ; <<>> DiG 9.18.24 <<>> @8.8.8.8 example.com
    ; (1 server found)
    ;; global options: +cmd
    ;; Got answer:
    ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 12345
    ;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

    ;; OPT PSEUDOSECTION:
    ; EDNS: version: 0, flags:; udp: 512
    ;; QUESTION SECTION:
    ;example.com.           IN  A

    ;; ANSWER SECTION:
    example.com.        3600    IN  A   93.184.216.34

    ;; Query time: 42 msec
    ;; SERVER: 8.8.8.8#53(8.8.8.8)
    ;; WHEN: Wed Jan 15 10:22:15 UTC 2026
    ;; MSG SIZE  rcvd: 55

The **ANSWER SECTION** shows the resolved IP address. The TTL (3600 in this example) indicates how long the record is cached.

## Querying Authoritative Nameservers

To check if a domain change has propagated to the authoritative nameserver, first find the authoritative servers:

``` bash
dig example.com NS +short
```

Then query one of those servers directly:

``` bash
dig @ns1.example.com example.com
```

## Useful dig Flags for Specific Record Types

Query specific DNS record types instead of defaulting to A records:

``` bash
# MX records (mail servers)
dig @8.8.8.8 example.com MX

# CNAME records
dig @8.8.8.8 example.com CNAME

# TXT records
dig @8.8.8.8 example.com TXT

# All records
dig @8.8.8.8 example.com ANY
```

## Simplifying Output

For cleaner output when you only care about the answer:

``` bash
dig @8.8.8.8 example.com +short
```

This returns just the IP address:

    93.184.216.34

Or get just the authoritative nameservers:

``` bash
dig @8.8.8.8 example.com NS +short
```

## Querying on Non-Standard Ports

If your DNS server runs on a non-standard port (not 53), specify it with `-p`:

``` bash
dig @192.168.1.1 -p 5053 example.com
```

## Checking Propagation Across Multiple Resolvers

Compare responses from different DNS servers to verify propagation:

``` bash
dig @8.8.8.8 example.com +short
dig @1.1.1.1 example.com +short
dig @your-local-resolver example.com +short
```

## Reverse DNS Lookups

Query a specific server for reverse DNS lookups:

``` bash
dig @8.8.8.8 -x 93.184.216.34
```

This is particularly useful when troubleshooting mail server configurations or verifying that reverse DNS matches forward records.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
