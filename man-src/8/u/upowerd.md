---
title: "upowerd(8)"
name: "upowerd"
section: "8"
letter: "u"
url: "/docs/linux/man/8-upowerd/"
description: "upowerd – UPower Daemon"
---

<p>upowerd &#8211; UPower Daemon</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>upowerd</code> [<code>&#8211;help</code>]</dl>
<h2>Description</h2>
<p><i>upowerd</i></p>
<dd>provides the <i>org.freedesktop.UPower</i> service on the system message bus. Users or administrators should never need to start this daemon as it will be automatically started by <code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a></code>(1) whenever an application calls into the <i>org.freedesktop.UPower</i> service.</p>
<h2>Options</h2>
<p><code>&#8211;help</code></p>
<dl>
<dd>Show help options.</dl>
<h2>Author</h2>
<p>Written by David Zeuthen &lt;davidz [at] redhat.com&gt; with a lot of help from many others.</p>
<h2>Bugs</h2>
<p>Please send bug reports to either the distribution or the DeviceKit mailing list, see m[blue]<code><a rel="nofollow" href="http://lists.freedesktop.org/mailman/listinfo/devkit-devel">http://lists.freedesktop.org/mailman/listinfo/devkit-devel</a></code>m[] on how to subscribe.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-upower/">UPower</a></code>(7), <code><a href="/docs/linux/man/1-upower/">upower</a></code>(1), <code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a></code>(1), </p>
