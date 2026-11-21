---

title: "avahi-resolve-host-name(1)"
name: "avahi-resolve-host-name"
section: "1"
letter: "a"
url: "/docs/linux/man/1-avahi-resolve-host-name/"
description: "avahi-resolve – Resolve one or more mDNS/DNS host name(s) to IP address(es) (and vice versa) using the Avahi daemon"
---

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
<dt><code>-n | &#8211;name</code></dt>
<dd> Translate one or more fully qualified host names into addresses.</dd>
<dt><code>-a | &#8211;address</code></dt>
<dd> Translate one or more addresses into fully qualified host names.</dd>
<dt><code>-v | &#8211;verbose</code></dt>
<dd> Enable verbose mode.</dd>
<dt><code>-6</code></dt>
<dd> When resolving a host name, look for IPv6 addresses exclusively.</dd>
<dt><code>-4</code></dt>
<dd> When resolving a host name, look for IPv4 addresses exclusively.</dd>
<dt><code>-h | &#8211;help</code></dt>
<dd> Show help.</dd>
<dt><code>-V | &#8211;version</code></dt>
<dd> Show version information.</dd></dl>
<h2>AUTHORS</h2>
<p> The Avahi Developers &lt;avahi (at) lists (dot) freedesktop (dot) org&gt;; Avahi is available from <code><a rel="nofollow" href="http://avahi.org/">http://avahi.org/</a></code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-avahi-publish-address/">avahi-publish-address</a>(1)</code>, <code><a href="/docs/linux/man/8-avahi-daemon/">avahi-daemon</a>(8)</code></p>
<h2>COMMENTS</h2>
<p> This man page was written using <code>xml2man(1)</code> by Oliver Kurth. </p>
