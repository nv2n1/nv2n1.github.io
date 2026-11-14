---
title: "storaged-lvm(8)"
name: "storaged-lvm"
section: "8"
letter: "s"
url: "/docs/linux/man/8-storaged-lvm/"
description: "storaged-lvm – The storaged command line tool"
---

<p>storaged-lvm &#8211; The storaged command line tool</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>storaged-lvm</code> [<code>-b</code>] [<code>-f</code>] <i>COMMAND</i></dl>
<h2>Description</h2>
<p><code>storaged-lvm</code></p>
<dd>is a helper program used by Storaged to query <i>the state of LVM2</i> via the lvm2app library.</p>
<h2>Options</h2>
<p><code>-h</code></p>
<dl>
<dd>Show help options.</dl>
<p> <code>-b</code></p>
<dl>
<dd>Print the result of <i>COMMAND</i> in binary form (serialized).</dl>
<p> <code>-f</code></p>
<dl>
<dd>Use an alternative LVM system directory; no lock.</dl>
<h2>Author</h2>
<p>Written by Marius Vollmer &lt;marius.vollmer [at] gmail.com&gt;.</p>
<h2>Bugs</h2>
<p>Please send bug reports to either the distribution bug tracker or the upstream bug tracker at m[blue]<code><a rel="nofollow" href="https://github.com/storaged-project/storaged/issues">https://github.com/storaged-project/storaged/issues</a></code>m[].</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-storaged/">storaged</a></code>(8), <code><a href="/docs/linux/man/1-storagectl/">storagectl</a></code>(1), <code><a href="/docs/linux/man/8-umount-storaged/">umount.storaged</a></code>(8), <code><a href="/docs/linux/man/8-polkit/">polkit</a></code>(8), <code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a></code>(1), <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) </p>
