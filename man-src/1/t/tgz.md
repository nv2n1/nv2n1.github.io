---
title: "tgz(1)"
name: "tgz"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tgz/"
description: "tgz – makes a gzip’d tar archive"
---

<h2 class="name">NAME</h2>
<p> tgz &#8211; makes a gzip&#8217;d tar archive </p>
<h2>SYNOPSIS</h2>
<p> <code>tgz</code> [ <i>destination</i> [ <i>source &#8230;</i> ] ]</p>
<h2>DESCRIPTION</h2>
<p> Make a gzip&#8217;d tar archive with the name of the first parameter out of specified files or, if no source files are specified, from everything in the current directory. If the first parameter is omitted as well, the archive will be written to stdout.</p>
<h2>BUGS</h2>
<p> <code>tgz</code> requires gzip in the user&#8217;s path. It also needs gnu tar or something close due to use of &#8211;exclude, &#8211;totals and -S.</p>
<h2>AUTHOR</h2>
<p> Filip Van Raemdonck (mechanix [at] debian.org) wrote this page for the <i>Debian/GNU</i> mtools package.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1), <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1) </p>
<h2>Index</h2>
