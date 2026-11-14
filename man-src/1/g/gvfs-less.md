---
title: "gvfs-less(1)"
name: "gvfs-less"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gvfs-less/"
description: "gvfs-less – Execute less on the output of gvfs-cat"
---

<h2 class="name">NAME</h2>
<p> gvfs-less &#8211; Execute less on the output of gvfs-cat </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gvfs-less </code><code>[OPTION&#8230;]</code><code>[LOCATION&#8230;]</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>gvfs-less</code></p>
<dd>executes <code>less</code> on the output of <code>gvfs-cat</code>. </p>
<p> <code>gvfs-less</code> works just like the traditional less utility, but using gvfs locations instead of local files: for example you can use something like <a href="smb://server/resource/file.txt">smb://server/resource/file.txt</a> as location.</p>
<h2>OPTIONS</h2>
<p> See <code><a href="/docs/linux/man/1-less/">less</a></code>(1) for the options.</p>
<h2>EXIT STATUS</h2>
<p> On success 0 is returned, a non-zero failure code otherwise.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-less/">less</a></code>(1), <code><a href="/docs/linux/man/1-gvfs-cat/">gvfs-cat</a></code>(1) </p>
<h2>Index</h2>
