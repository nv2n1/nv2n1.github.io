---
title: "cdiff(1)"
name: "cdiff"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cdiff/"
description: "cdiff – a wrapper tool for colordiff"
---

<h2 class="name">NAME</h2>
<p> cdiff &#8211; a wrapper tool for colordiff </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>cdiff</code> {<i>URL|FILE</i>}</dl>
<h2>DESCRIPTION</h2>
<dd>cdiff is a wrapper for colordiff and will add colour to a diff given in a URL or a file, e.g. </p>
<dl>
<dt>
<dd>
<pre>
cdiff <a rel="nofollow" href="http://some.url.com/foo/thing.patch">http://some.url.com/foo/thing.patch</a>
</pre>
</dl>
<p> It also adds support for reading gzip, bzip2, xz, and lzma compressed diffs, and like colordiff, also supports reading diffs from standard input if URL or a filename is not specified. cdiff pipes colordiff&#8217;s output through less -R.</p>
<h2>SEE ALSO</h2>
<p> cdiff is part of the colordiff package, which should be consulted for further reference.</p>
<h2>AUTHORS</h2>
<p> <code>Ville Skytt&auml;</code></p>
<dl>
<dt>
<dd> cdiff author</dl>
<p> <code>Dave Ewart</code></p>
<dl>
<dt>
<dd> colordiff author, packager for colordiff/cdiff</dl>
<h2>Index</h2>
