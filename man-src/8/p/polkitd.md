---
title: "polkitd(8)"
name: "polkitd"
section: "8"
letter: "p"
url: "/docs/linux/man/8-polkitd/"
description: "polkitd – PolicyKit daemon"
---

<p>polkitd &#8211; PolicyKit daemon</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>polkitd</code></dl>
<h2>Description</h2>
<p><code>polkitd</code></p>
<dd>provides the <i>org.freedesktop.PolicyKit1</i> D-Bus service on the system message bus. Users or administrators should never need to start this daemon as it will be automatically started by <code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a></code>(1) whenever an application calls into the service.</p>
<h2>Author</h2>
<p>Written by David Zeuthen &lt;davidz [at] redhat.com&gt; with a lot of help from many others.</p>
<h2>Bugs</h2>
<p>Please send bug reports to either the distribution or the polkit-devel mailing list, see the link m[blue]<code><a rel="nofollow" href="http://lists.freedesktop.org/mailman/listinfo/polkit-devel">http://lists.freedesktop.org/mailman/listinfo/polkit-devel</a></code>m[] on how to subscribe.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-polkit/">polkit</a></code>(8) </p>
