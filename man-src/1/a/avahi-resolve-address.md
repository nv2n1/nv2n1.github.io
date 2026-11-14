---
title: "avahi-resolve-address(1)"
name: "avahi-resolve-address"
section: "1"
letter: "a"
url: "/docs/linux/man/1-avahi-resolve-address/"
description: "avahi-resolve – Resolve one or more mDNS/DNS host name(s) to IP address(es) (and vice versa) using the Avahi daemon"
---

<h2 class="name">NAME</h2>
<p> avahi-resolve &#8211; Resolve one or more mDNS/DNS host name(s) to IP address(es) (and vice versa) using the Avahi daemon </p>
<h2>SYNOPSIS</h2>
<p> <code>avahi-resolve &#8211;name </code><i>host-name &#8230;</i><code> </p>
<p> avahi-resolve-host-name </code><i>host-name &#8230;</i><code> </p>
<p> avahi-resolve &#8211;address </code><i>address &#8230;</i><code> </p>
<p> avahi-resolve-address </code><i>address &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> Resolve one or more mDNS/DNS host name(s) to IP address(es) (and vice versa) using the Avahi daemon.</p>
<h2>OPTIONS</h2>
<p> When passing -n, specify one or more fully qualified mDNS/DNS host name(s) (e.g. &quot;foo.local&quot;) to resolve into IP addresses on the command line. When passing -a, specify one or more IP address to resolve into host names. </p>
<p> avahi-resolve-host-name is equivalent to avahi-resolve &#8211;name. </p>
<p> avahi-resolve-address is equivalent to avahi-resolve &#8211;address.</p>
<dl>
<dt><code>-n | &#8211;name</code></p>
<dd> Translate one or more fully qualified host names into addresses.</p>
<dt><code>-a | &#8211;address</code></p>
<dd> Translate one or more addresses into fully qualified host names.</p>
<dt><code>-v | &#8211;verbose</code></p>
<dd> Enable verbose mode.</p>
<dt><code>-6</code></p>
<dd> When resolving a host name, look for IPv6 addresses exclusively.</p>
<dt><code>-4</code></p>
<dd> When resolving a host name, look for IPv4 addresses exclusively.</p>
<dt><code>-h | &#8211;help</code></p>
<dd> Show help.</p>
<dt><code>-V | &#8211;version</code></p>
<dd> Show version information.</dl>
<h2>AUTHORS</h2>
<p> The Avahi Developers &lt;avahi (at) lists (dot) freedesktop (dot) org&gt;; Avahi is available from <code><a rel="nofollow" href="http://avahi.org/">http://avahi.org/</a></code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-avahi-publish-address/">avahi-publish-address</a>(1)</code>, <code><a href="/docs/linux/man/8-avahi-daemon/">avahi-daemon</a>(8)</code></p>
<h2>COMMENTS</h2>
<p> This man page was written using <code><a href="/docs/linux/man/1-xml2man/">xml2man</a>(1)</code> by Oliver Kurth. </p>
<h2>Index</h2>
