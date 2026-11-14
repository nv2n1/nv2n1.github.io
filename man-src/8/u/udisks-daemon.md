---
title: "udisks-daemon(8)"
name: "udisks-daemon"
section: "8"
letter: "u"
url: "/docs/linux/man/8-udisks-daemon/"
description: "udisks-daemon – udisks Daemon"
---

<p>udisks-daemon &#8211; udisks Daemon</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>udisks-daemon</code> [<code>&#8211;help</code>]</dl>
<h2>Description</h2>
<p><i>udisks-daemon</i></p>
<dd>provides the <i>org.freedesktop.UDisks</i> service on the system message bus. Users or administrators should never need to start this daemon as it will be automatically started by <code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a></code>(1) whenever an application calls into the <i>org.freedesktop.UDisks</i> service. </p>
<p> See the <code><a href="/docs/linux/man/7-udisks/">udisks</a></code>(7) man page for information on how to customize how <i>udisks-daemon</i> works.</p>
<h2>Options</h2>
<p><code>&#8211;help</code></p>
<dl>
<dd>Show help options.</dl>
<h2>Author</h2>
<p>Written by David Zeuthen &lt;david [at] fubar.dk&gt; with a lot of help from many others.</p>
<h2>Bugs</h2>
<p>Please send bug reports to either the distribution bug tracker or the upstream bug tracker at m[blue]<code><a rel="nofollow" href="https://bugs.freedesktop.org/enter_bug.cgi?product=udisks">https://bugs.freedesktop.org/enter_bug.cgi?product=udisks</a></code>m[].</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-udisks/">udisks</a></code>(7), <code><a href="/docs/linux/man/1-udisks/">udisks</a></code>(1), <code><a href="/docs/linux/man/1-udisks-tcp-bridge/">udisks-tcp-bridge</a></code>(1), <code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a></code>(1) </p>
