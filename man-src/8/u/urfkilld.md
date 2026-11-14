---
title: "urfkilld(8)"
name: "urfkilld"
section: "8"
letter: "u"
url: "/docs/linux/man/8-urfkilld/"
description: "urfkilld – urfkill Daemon"
---

<p>urfkilld &#8211; urfkill Daemon</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>urfkilld</code> [<code>&#8211;help</code>]</dl>
<h2>Description</h2>
<p><i>urfkilld</i></p>
<dd>provides the <i>org.freedesktop.URfkill</i> service on the system message bus. Users or administrators should never need to start this daemon as it will be automatically started by <code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a></code>(1) whenever an application calls into the <i>org.freedesktop.URfkill</i> service.</p>
<h2>Options</h2>
<p><code>&#8211;help</code></p>
<dl>
<dd>Show help options.</dl>
<h2>Author</h2>
<p>Written by Gary Ching-Pang Lin &lt;glin [at] novell.com&gt; with a lot of help from many others.</p>
<h2>Bugs</h2>
<p>Please send bug reports to either the distribution or the DeviceKit mailing list, see m[blue]<code><a rel="nofollow" href="http://lists.freedesktop.org/mailman/listinfo/devkit-devel">http://lists.freedesktop.org/mailman/listinfo/devkit-devel</a></code>m[] on how to subscribe.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-urfkill/">urfkill</a></code>(7), <code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a></code>(1), </p>
