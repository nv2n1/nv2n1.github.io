---
title: "udisks-tcp-bridge(1)"
name: "udisks-tcp-bridge"
section: "1"
letter: "u"
url: "/docs/linux/man/1-udisks-tcp-bridge/"
description: "udisks-tcp-bridge – udisks TCP/IP bridge"
---

<h2 class="name">NAME</h2>
<p> udisks-tcp-bridge &#8211; udisks TCP/IP bridge </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>udisks-tcp-bridge </code> [<code>&#8211;port</code>&nbsp;<wbr><i>port</i>] [<code>&#8211;help</code>]</dl>
<h2>DESCRIPTION</h2>
<dd>This program is used by remote clients to connect to the <i>org.freedesktop.UDisks</i> D-Bus service on the system bus. </p>
<p> Users or administrators never needs to start this program as it started automatically by a remote client connecting via <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1). See the <code><a href="/docs/linux/man/7-udisks/">udisks</a></code>(7) manual page for information about the higher level connection protocol used.</p>
<h2>AUTHOR</h2>
<p> Written by David Zeuthen &lt;david [at] fubar.dk&gt; with a lot of help from many others.</p>
<h2>BUGS</h2>
<p> Please send bug reports to either the distribution bug tracker or the upstream bug tracker at m[blue]<code><a rel="nofollow" href="http://bugs.freedesktop.org/enter_bug.cgi?product=udisks">http://bugs.freedesktop.org/enter_bug.cgi?product=udisks</a></code>m[].</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-udisks-daemon/">udisks-daemon</a></code>(8), <code><a href="/docs/linux/man/7-udisks/">udisks</a></code>(7), <code><a href="/docs/linux/man/1-udisks/">udisks</a></code>(1), <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1) </p>
<h2>Index</h2>
