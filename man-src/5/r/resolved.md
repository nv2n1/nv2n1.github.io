---
title: "resolved(5)"
name: "resolved"
section: "5"
letter: "r"
url: "/docs/linux/man/5-resolved/"
description: "resolved.conf – Network Name Resolution configuration file"
---

<p>resolved.conf &#8211; Network Name Resolution configuration file</p>
<h2>Synopsis</h2>
<p>/etc/systemd/resolved.conf</p>
<h2>Description</h2>
<p>When starting, systemd-resolved will read the configuration file resolved.conf. This configuration file controls local DNS and LLMNR name resolving.</p>
<h2>Options</h2>
<p><i>DNS=</i></p>
<dl>
<dd>A space separated list of IPv4 and IPv6 addresses to be used as system DNS servers. DNS requests are sent to one of the listed DNS servers in parallel to any per-interface DNS servers acquired from <code><a href="/docs/linux/man/8-systemd-networkd-service/">systemd-networkd.service</a></code>(8). For compatibility reasons, if set to the empty list the DNS servers listed in /etc/resolv.conf are used, if any are configured there. This setting defaults to the empty list.</dl>
<p> <i>FallbackDNS=</i></p>
<dl>
<dd>A space separated list of IPv4 and IPv6 addresses to be used as the fallback DNS servers. Any per-interface DNS servers obtained from <code><a href="/docs/linux/man/8-systemd-networkd-service/">systemd-networkd.service</a></code>(8) take precedence over this setting, as do any servers set via <i>DNS=</i> above or /etc/resolv.conf. This setting is hence only used if no other DNS server information is known. If this option is not given, a compiled-in list of DNS servers is used instead.</dl>
<p> <i>LLMNR=</i></p>
<dl>
<dd>Takes a boolean argument or &quot;resolve&quot;. Controls Link-Local Multicast Name Resolution support (m[blue]<code>RFC 4794</code>m[]<font SIZE="-2">[1]</font>) on the local host. If true enables full LLMNR responder and resolver support. If false disable both. If set to &quot;resolve&quot; only resolving support is enabled, but responding is disabled. Note that <code><a href="/docs/linux/man/8-systemd-networkd-service/">systemd-networkd.service</a></code>(8) also maintains per-interface LLMNR settings. LLMNR will be enabled on an interface only if the per-interface and the global setting is on.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-resolved-service/">systemd-resolved.service</a></code>(8), <code><a href="/docs/linux/man/8-systemd-networkd-service/">systemd-networkd.service</a></code>(8), <code><a href="/docs/linux/man/4-resolv-conf/">resolv.conf</a></code>(4)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>RFC 4794</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc4795">https://tools.ietf.org/html/rfc4795</a></dl>
