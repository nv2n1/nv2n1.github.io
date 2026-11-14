---
title: "devkit-power-daemon(8)"
name: "devkit-power-daemon"
section: "8"
letter: "d"
url: "/docs/linux/man/8-devkit-power-daemon/"
description: "devkit-power-daemon – DeviceKit-power Daemon"
---

<p>devkit-power-daemon &#8211; DeviceKit-power Daemon</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>devkit-power-daemon</code> [<code>&#8211;help</code>]</dl>
<h2>Description</h2>
<p><i>devkit-power-daemon</i></p>
<dd>provides the <i>org.freedesktop.DeviceKit.Power</i> service on the system message bus. Users or administrators should never need to start this daemon as it will be automatically started by <code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a></code>(1) whenever an application calls into the <i>org.freedesktop.DeviceKit.Power</i> service.</p>
<h2>Options</h2>
<p><code>&#8211;help</code></p>
<dl>
<dd>Show help options.</dl>
<h2>Author</h2>
<p>Written by David Zeuthen davidz [at] redhat.com with a lot of help from many others.</p>
<h2>Bugs</h2>
<p>Please send bug reports to either the distribution or the DeviceKit mailing list, see m[blue]<code><a rel="nofollow" href="http://lists.freedesktop.org/mailman/listinfo/devkit-devel">http://lists.freedesktop.org/mailman/listinfo/devkit-devel</a></code>m[] on how to subscribe.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-devicekit-power/">DeviceKit-power</a></code>(7), <code><a href="/docs/linux/man/1-devkit-power/">devkit-power</a></code>(1), <code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a></code>(1), </p>
