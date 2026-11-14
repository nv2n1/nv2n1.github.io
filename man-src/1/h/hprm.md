---
title: "hprm(1)"
name: "hprm"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hprm/"
description: "hprm — remove a file or directory on an HFS+ volume"
---

<h2>NAME</h2>
<p> hprm &#8212; remove a file or directory on an HFS+ volume</p>
<h2>SYNOPSIS</h2>
<p> <code>hprm</code> [<code>-R</code>] [<code>-f</code>] <i>hfs-path</i></p>
<h2>Description</h2>
<p> <code>hprm</code> removes the file or directory specified by <code>hfs-path</code>. Since write access to HFS+ volumes is still experimental, the program prints a warning message and prompts the user before writing anything to the file system.<br />
&nbsp; </p>
<p> <code>hprm</code> accepts the following options:<br />
&nbsp;</p>
<dl>
<dt><code>-R</code></p>
<dd> recursively remove the contents of a directory.<br />
&nbsp;</p>
<dt><code>-f</code></p>
<dd> one day, this option will probably disable prompting. For the time being, prompting is always enabled.<br />
&nbsp;</dl>
<h2>See also</h2>
<p> <a href="/docs/linux/man/7-hfsplus/">hfsplus</a>(7), <a href="/docs/linux/man/1-hpmount/">hpmount</a>(1), <a href="/docs/linux/man/1-hpls/">hpls</a>(1), <a href="/docs/linux/man/1-hppwd/">hppwd</a>(1), <a href="/docs/linux/man/1-hpmkdir/">hpmkdir</a>(1), <a href="/docs/linux/man/1-hpcd/">hpcd</a>(1), <a href="/docs/linux/man/1-hpcopy/">hpcopy</a>(1), <a href="/docs/linux/man/1-hpumount/">hpumount</a>(1), <a href="/docs/linux/man/1-hpfsck/">hpfsck</a>(1).<br />
&nbsp;</p>
<h2>Author</h2>
<p> This manual page was written by Jens Schmalzing &lt;jensen [at] debian.org&gt; for <code>Debian GNU/Linux</code> using the manual page by Klaus Halfmann &lt;halfmann [at] libra.de&gt; that comes with the source code and documentation from the <code>Tech Info Library</code>.<br />
&nbsp; </p>
<h2>Index</h2>
