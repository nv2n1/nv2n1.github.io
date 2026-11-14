---
title: "devkit-disks-daemon(8)"
name: "devkit-disks-daemon"
section: "8"
letter: "d"
url: "/docs/linux/man/8-devkit-disks-daemon/"
description: "devkit-disks-daemon – DeviceKit-disks Daemon"
---

<p>devkit-disks-daemon &#8211; DeviceKit-disks Daemon</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>devkit-disks-daemon</code> [<code>&#8211;help</code>]</dl>
<h2>Description</h2>
<p><i>devkit-disks-daemon</i></p>
<dd>provides the <i>org.freedesktop.DeviceKit.Disks</i> service on the system message bus. Users or administrators should never need to start this daemon as it will be automatically started by <code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a></code>(1) whenever an application calls into the <i>org.freedesktop.DeviceKit.Disks</i> service. </p>
<p> See the <code><a href="/docs/linux/man/7-devicekit-disks/">DeviceKit-disks</a></code>(7) man page for information on how to customize how <i>devkit-disks-daemon</i> works.</p>
<h2>Options</h2>
<p><code>&#8211;help</code></p>
<dl>
<dd>Show help options.</dl>
<h2>Author</h2>
<p>Written by David Zeuthen david [at] fubar.dk with a lot of help from many others.</p>
<h2>Bugs</h2>
<p>Please send bug reports to either the distribution or the hal mailing list, see m[blue]<code><a rel="nofollow" href="http://lists.freedesktop.org/mailman/listinfo/hal">http://lists.freedesktop.org/mailman/listinfo/hal</a></code>m[] on how to subscribe.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-devicekit-disks/">DeviceKit-disks</a></code>(7), <code><a href="/docs/linux/man/1-devkit-disks/">devkit-disks</a></code>(1), <code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a></code>(1), </p>
