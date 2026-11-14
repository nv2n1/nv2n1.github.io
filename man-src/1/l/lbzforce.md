---
title: "lbzforce(1)"
name: "lbzforce"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lbzforce/"
description: "lbzforce – force a ‘.bz2’ extension on all lbzip2 files"
---

<h2>NAME</h2>
<p> lbzforce &#8211; force a &#8216;.bz2&#8217; extension on all lbzip2 files</p>
<h2>SYNOPSIS</h2>
<p> <code>lbzforce</code> [ name &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> <i>lbzforce</i> forces a .bz2 extension on all <i>lbzip2</i> files so that <i>lbzip2</i> will not compress them twice. This can be useful for files with names truncated after a file transfer. On systems with a 14 char limitation on file names, the original name is truncated to make room for the .bz2 suffix. For example, 12345678901234 is renamed to 12345678901.bz2. A file name such as foo.tbz is left intact.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-lbzip2/">lbzip2</a>(1), <a href="/docs/linux/man/1-lbzmore/">lbzmore</a>(1), <a href="/docs/linux/man/1-lbzgrep/">lbzgrep</a>(1), <a href="/docs/linux/man/1-lbzdiff/">lbzdiff</a>(1), <a href="/docs/linux/man/1-lbzexe/">lbzexe</a>(1) </p>
<h2>Index</h2>
