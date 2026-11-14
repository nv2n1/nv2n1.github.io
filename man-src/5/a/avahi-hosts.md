---
title: "avahi-hosts(5)"
name: "avahi-hosts"
section: "5"
letter: "a"
url: "/docs/linux/man/5-avahi-hosts/"
description: "avahi.hosts – avahi-daemon static host name file"
---

<p>avahi.hosts &#8211; avahi-daemon static host name file</p>
<h2>Synopsis</h2>
<p><code>/etc/avahi/hosts </code></p>
<h2>Description</h2>
<p><i>/etc/avahi/hosts</i> is a file which may be used to define static host name to IP address mappings for multicast DNS. This is especially useful when publishing DNS-SD services on behalf of other hosts. See <code><a href="/docs/linux/man/5-avahi-service/">avahi.service</a>(5)</code> for more information. </p>
<p> The file format is similar to the one of <i>/etc/hosts</i>: on each line an IP address and the corresponding host name. The host names should be in FQDN form, i.e. with appended .local suffix.</p>
<h2>Authors</h2>
<p>The Avahi Developers &lt;avahi (at) lists (dot) freedesktop (dot) org&gt;; Avahi is available from <code><a rel="nofollow" href="http://avahi.org/">http://avahi.org/</a></code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-avahi-daemon/">avahi-daemon</a>(8)</code>, <code><a href="/docs/linux/man/5-avahi-service/">avahi.service</a>(5)</code></p>
<h2>Comments</h2>
<p>This man page was written using <code><a href="/docs/linux/man/1-xml2man/">xml2man</a>(1)</code> by Oliver Kurth.</p>
