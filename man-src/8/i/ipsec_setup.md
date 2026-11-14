---
title: "ipsec_setup(8)"
name: "ipsec_setup"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipsec_setup/"
description: "ipsec_setup – wrapper routine to the Libreswan init system"
---

<p>ipsec_setup &#8211; wrapper routine to the Libreswan init system</p>
<h2>Description</h2>
<p><i>setup</i> is called (via <i>ipsec setup</i>) by the system administrator to perform init system related tasks to Libreswan, such as start, stop, status, reload, etc for the Internet Keying Exchange (IKE) daemon pluto. It is available for backwards compatibility with Openswan and FreeS/WAN.</p>
<h2>Supported Init Systems</h2>
<p>Currently, the classic initscripts (sysv) and systemd are supported. Support for upstart will be added soon.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-systemd/">systemd</a></code>(8), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/8-ipsec/">ipsec</a></code>(8), <code><a href="/docs/linux/man/8-ipsec__realsetup/">ipsec__realsetup</a></code>(8), <code><a href="/docs/linux/man/8-ipsec__plutorun/">ipsec__plutorun</a></code>(8) .</p>
<h2>History</h2>
<p>Man page written for the Linux FreeS/WAN project by Michael Richardson. Original program by Henry Spencer. Updated to m[blue]<code><a rel="nofollow" href="http://www.libreswan.org/">http://www.libreswan.org/</a></code>m[]&gt; by Paul Wouters</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
