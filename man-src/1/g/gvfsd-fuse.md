---
title: "gvfsd-fuse(1)"
name: "gvfsd-fuse"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gvfsd-fuse/"
description: "gvfsd-fuse – Fuse daemon for gvfs"
---

<h2 class="name">NAME</h2>
<p> gvfsd-fuse &#8211; Fuse daemon for gvfs </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gvfsd-fuse</code> PATH</dl>
<h2>DESCRIPTION</h2>
<p> <code>gvfsd-fuse</code></p>
<dd>maintains a fuse mount to make gvfs backends available to POSIX applications. The mount point for the fuse filesystem is provided by the [PATH] argument. </p>
<p> <code>gvfsd-fuse</code> is normally started by <code><a href="/docs/linux/man/1-gvfsd/">gvfsd</a></code>(1). In this case, the mount point is <code>$XDG_RUNTIME_DIR</code>/gvfs or <code>$HOME</code>/.gvfs.</p>
<h2>OPTIONS</h2>
<p> <code>-d</code></p>
<dl>
<dt>
<dd> Enable fuse debug output. This implies <code>-f</code>.</dl>
<p> <code>-f</code></p>
<dl>
<dt>
<dd> Run in the foreground.</dl>
<p> <code>-s</code></p>
<dl>
<dt>
<dd> Run single-threaded.</dl>
<p> <code>-o OPTION</code></p>
<dl>
<dt>
<dd> Set a fuse-specific option. See the fuse documentation for a list of these.</dl>
<h2>EXIT STATUS</h2>
<p> On success 0 is returned, a non-zero failure code otherwise.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gvfs/">gvfs</a></code>(7) </p>
<h2>Index</h2>
