---
title: "zforce(1)"
name: "zforce"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zforce/"
description: "zforce – force a ‘.gz’ extension on all gzip files"
---

<h2 class="name">NAME</h2>
<p> zforce &#8211; force a &#8216;.gz&#8217; extension on all gzip files </p>
<h2>SYNOPSIS</h2>
<p> <code>zforce</code> [ name &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> <i>zforce</i> forces a .gz extension on all <i>gzip</i> files so that <i>gzip</i> will not compress them twice. This can be useful for files with names truncated after a file transfer. On systems with a 14 char limitation on file names, the original name is truncated to make room for the .gz suffix. For example, 12345678901234 is renamed to 12345678901.gz. A file name such as foo.tgz is left intact.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gzip/">gzip</a>(1), <a href="/docs/linux/man/1-znew/">znew</a>(1), <a href="/docs/linux/man/1-zmore/">zmore</a>(1), <a href="/docs/linux/man/1-zgrep/">zgrep</a>(1), <a href="/docs/linux/man/1-zdiff/">zdiff</a>(1), <a href="/docs/linux/man/1-gzexe/">gzexe</a>(1) </p>
<h2>Index</h2>
