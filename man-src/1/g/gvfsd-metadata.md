---
title: "gvfsd-metadata(1)"
name: "gvfsd-metadata"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gvfsd-metadata/"
description: "gvfsd-metadata – Metadata daemon for gvfs"
---

<h2 class="name">NAME</h2>
<p> gvfsd-metadata &#8211; Metadata daemon for gvfs </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gvfs-metadata</code> [OPTION&#8230;]</dt></dl>
<h2>DESCRIPTION</h2>
<p> <code>gvfsd-metadata</code></p>
<dd>is a daemon acting as a write serialiser to the internal gvfs metadata storage. It is autostarted by GIO clients when they make metadata changes. Read operations are done by client-side GIO code directly, and don&#8217;t require the daemon to be running. </dd>
<p> The gvfs metadata capabilities are used by the nautilus file manager, for example.</p>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Prints a short help text and exits.</dd></dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
</dt><dd> Shows the version number and exits.</dd></dl>
<p> <code>-r</code>, <code>&#8211;replace</code></p>
<dl>
<dt>
</dt><dd> Replace the currently running instance.</dd></dl>
<h2>EXIT STATUS</h2>
<p> On success 0 is returned, a non-zero failure code otherwise.</p>
<h2>FILES</h2>
<p> <code>$XDG_DATA_HOME</code>/gvfs-metadata</p>
<dl>
<dt>
</dt><dd> The directory where the gvfs metadata database files are stored</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gvfs/">gvfs</a></code>(7), <code><a href="/docs/linux/man/1-nautilus/">nautilus</a></code>(1) </p>
<h2>Index</h2>
