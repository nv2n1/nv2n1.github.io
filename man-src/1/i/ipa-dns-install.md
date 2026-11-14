---
title: "ipa-dns-install(1)"
name: "ipa-dns-install"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-dns-install/"
description: "ipa-dns-install – Add DNS as a service to an IPA server"
---

<h2>NAME</h2>
<p> ipa-dns-install &#8211; Add DNS as a service to an IPA server</p>
<h2>SYNOPSIS</h2>
<p> ipa-dns-install [<i>OPTION</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Adds DNS as an IPA-managed service. This requires that the IPA server is already installed and configured.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> Enable debug logging when more verbose output is needed</p>
<dt><code>&#8211;ip-address</code>=<i>IP_ADDRESS</i></p>
<dd> The IP address of the IPA server. If not provided then this is determined based on the hostname of the server. This this option can be used multiple times to specify more IP addresses of the server (e.g. multihomed and/or dualstacked server).</p>
<dt><code>&#8211;forwarder</code>=<i>FORWARDER</i></p>
<dd> A forwarder is a DNS server where queries for a specific non-resolvable address can be directed. To define multiple forwarders use multiple instances of <code>&#8211;forwarder</code></p>
<dt><code>&#8211;no-forwarders</code></p>
<dd> Do not add any DNS forwarders, send non-resolvable addresses to the DNS root servers.</p>
<dt><code>&#8211;auto-forwarders</code></p>
<dd> Add DNS forwarders configured in /etc/resolv.conf to the list of forwarders used by IPA DNS.</p>
<dt><code>&#8211;forward-policy</code>=<i>first|only</i></p>
<dd> DNS forwarding policy for global forwarders specified using other options. Defaults to first if no IP address belonging to a private or reserved ranges is detected on local interfaces (RFC 6303). Defaults to only if a private IP address is detected.</p>
<dt><code>&#8211;reverse-zone</code>=<i>REVERSE_ZONE</i></p>
<dd> The reverse DNS zone to use. This option can be used multiple times to specify multiple reverse zones.</p>
<dt><code>&#8211;no-reverse</code></p>
<dd> Do not create new reverse DNS zone. If used on a replica and a reverse DNS zone already exists for the subnet, it will be used.</p>
<dt><code>&#8211;auto-reverse</code></p>
<dd> Try to resolve reverse records and reverse zones for server IP addresses and if neither is resolvable creates these reverse zones.</p>
<dt><code>&#8211;no-dnssec-validation</code></p>
<dd> Disable DNSSEC validation on this server.</p>
<dt><code>&#8211;dnssec-master</code></p>
<dd> Setup server to be DNSSEC key master.</p>
<dt><code>&#8211;disable-dnssec-master</code></p>
<dd> Disable the DNSSEC master on this server.</p>
<dt><code>&#8211;kasp-db</code>=<i>KASP_DB</i></p>
<dd> Copy OpenDNSSEC metadata from the specified kasp.db file. This will not create a new kasp.db file.</p>
<dt><code>&#8211;zonemgr</code></p>
<dd> The e-mail address of the DNS zone manager. Defaults to hostmaster [at] DOMAIN</p>
<dt><code>&#8211;allow-zone-overlap</code></p>
<dd> Allow creatin of (reverse) zone even if the zone is already resolvable. Using this option is discouraged as it result in later problems with domain name resolution.</p>
<dt><code>-U</code>, <code>&#8211;unattended</code></p>
<dd> An unattended installation that will never prompt for user input</dl>
<h2>DEPRECATED OPTIONS</h2>
<dl>
<dt><code>-p</code> <i>DM_PASSWORD</i>, <code>&#8211;ds-password</code>=<i>DM_PASSWORD</i></p>
<dd> The password to be used by the Directory Server for the Directory Manager user</dl>
<h2>EXIT STATUS</h2>
<p> 0 if the installation was successful </p>
<p> 1 if an error occurred </p>
<h2>Index</h2>
