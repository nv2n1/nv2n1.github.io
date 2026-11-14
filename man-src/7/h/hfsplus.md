---
title: "hfsplus(7)"
name: "hfsplus"
section: "7"
letter: "h"
url: "/docs/linux/man/7-hfsplus/"
description: "hfsplus — a set of tools to access HFS+ file systems"
---

<p>hfsplus &#8212; a set of tools to access HFS+ file systems</p>
<h2>Description</h2>
<p>HFS+, also known as the Macintosh Extended Format, was introduced by Apple Computer in 1998 with the release of MacOS 8.1. It contains many improvements over the old HFS file system, most notably the ability to allocate up to 2^64 blocks, resulting in much more efficient storage of many small files on large disks.<br />
&nbsp; </p>
<p> The <code>hfsplus</code> collection allows one to access volumes formatted with the HFS+ file system from <code>Debian GNU/Linux</code> and related operating systems. The collection contains tools to mount and unmount HFS+ volumes, to change and list directories, and to copy files to and from HFS+ volumes.<br />
&nbsp; </p>
<p> Note that unlike its cousin, the <code>hfsutils</code> collection used for accessing HFS file systems, <code>hfsplus</code> does not use the Macintosh pathname syntax with &quot;:&quot; as delimiter. Instead, it mimics the unix notation, delimiting the names of volumes, directories and files in a path with &quot;/&quot;, and also understands &quot;.&quot; and &quot;..&quot; to some extent.<br />
&nbsp;</p>
<h2>See also</h2>
<p><a href="/docs/linux/man/1-hpmount/">hpmount</a>(1), <a href="/docs/linux/man/1-hpls/">hpls</a>(1), <a href="/docs/linux/man/1-hpcd/">hpcd</a>(1), <a href="/docs/linux/man/1-hppwd/">hppwd</a>(1), <a href="/docs/linux/man/1-hpcopy/">hpcopy</a>(1), <a href="/docs/linux/man/1-hprm/">hprm</a>(1), <a href="/docs/linux/man/1-hpmkdir/">hpmkdir</a>(1), <a href="/docs/linux/man/1-hpumount/">hpumount</a>(1), <a href="/docs/linux/man/1-hpfsck/">hpfsck</a>(1).<br />
&nbsp;</p>
<h2>Author</h2>
<p>This manual page was written by Jens Schmalzing &lt;jensen [at] debian.org&gt; for <code>Debian GNU/Linux</code> using the manual page by Klaus Halfmann &lt;halfmann [at] libra.de&gt; that comes with the source code and documentation from the <code>Tech Info Library</code>.<br />
&nbsp;</p>
