---
title: "storaged(8)"
name: "storaged"
section: "8"
letter: "s"
url: "/docs/linux/man/8-storaged/"
description: "storaged – The storaged system daemon"
---

<p>storaged &#8211; The storaged system daemon</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>storaged</code> [<code>&#8211;help</code>] [<code>&#8211;replace</code>] [<code>&#8211;no-debug</code>] [<code>&#8211;no-sigint</code>] [<code>&#8211;force-load-modules</code>]</dl>
<h2>Description</h2>
<dd>The <code>storaged</code> program provides the <i>org.storaged.Storaged</i> name on the system message bus. Users or administrators should never need to start this daemon as it will be automatically started by <code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a></code>(1) or <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) whenever an application tries to access its D-Bus interfaces. </p>
<p> See the <code><a href="/docs/linux/man/8-storaged/">storaged</a></code>(8) man page for more information.</p>
<h2>Options</h2>
<p><code>&#8211;help</code></p>
<dl>
<dd>Show help options.</dl>
<p> <code>&#8211;replace</code></p>
<dl>
<dd>Replace existing daemon.</dl>
<p> <code>&#8211;no-debug</code></p>
<dl>
<dd>Do not print debug or informational messages on stdout/stderr.</dl>
<p> <code>&#8211;no-sigint</code></p>
<dl>
<dd>Do not handle SIGINT for controlled shutdown.</dl>
<p> <code>&#8211;force-load-modules</code></p>
<dl>
<dd>Activate modules on startup</dl>
<h2>Author</h2>
<p>This man page was originally written for UDisks2 by David Zeuthen &lt;zeuthen [at] gmail.com&gt; with a lot of help from many others.</p>
<h2>Bugs</h2>
<p>Please send bug reports to either the distribution bug tracker or the upstream bug tracker at m[blue]<code><a rel="nofollow" href="https://github.com/storaged-project/storaged/issues">https://github.com/storaged-project/storaged/issues</a></code>m[].</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-storaged/">storaged</a></code>(8), <code><a href="/docs/linux/man/1-storagectl/">storagectl</a></code>(1), <code><a href="/docs/linux/man/8-umount-storaged/">umount.storaged</a></code>(8), <code><a href="/docs/linux/man/8-polkit/">polkit</a></code>(8), <code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a></code>(1), <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) </p>
