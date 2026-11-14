---
title: "hpmount(1)"
name: "hpmount"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hpmount/"
description: "hpmount — change directory on an HFS+ volume"
---

<h2>NAME</h2>
<p> hpmount &#8212; change directory on an HFS+ volume</p>
<h2>SYNOPSIS</h2>
<p> <code>hpmount</code> [<code>-r</code>] [<code>-p</code><i>n</i>] <i>source-path</i></p>
<h2>Description</h2>
<p> <code>hpmount</code> introduces a new HFS+ volume. The source path may specify a block device or a regular file containing an HFS+ volume image. Furthermore, <code>hpmount</code> creates the file <code>.hfsplusvolume</code> in the user&#8217;s home directory, where the source path and the catalogue ID of the current working directory are stored.<br />
&nbsp; </p>
<p> <code>hpmount</code> accepts the following options:<br />
&nbsp;</p>
<dl>
<dt><code>-r</code></p>
<dd> mount the volume read-only. The default is to allow write-access.<br />
&nbsp;</p>
<dt><code>-p</code><i>n</i></p>
<dd> mount partition number <code>n</code>. The default is to mount the first partition that looks like it contains an HFS+ volume.<br />
&nbsp;</dl>
<h2>See also</h2>
<p> <a href="/docs/linux/man/7-hfsplus/">hfsplus</a>(7), <a href="/docs/linux/man/1-hpls/">hpls</a>(1), <a href="/docs/linux/man/1-hpcd/">hpcd</a>(1), <a href="/docs/linux/man/1-hppwd/">hppwd</a>(1), <a href="/docs/linux/man/1-hpcopy/">hpcopy</a>(1), <a href="/docs/linux/man/1-hprm/">hprm</a>(1), <a href="/docs/linux/man/1-hpmkdir/">hpmkdir</a>(1), <a href="/docs/linux/man/1-hpumount/">hpumount</a>(1), <a href="/docs/linux/man/1-hpfsck/">hpfsck</a>(1).<br />
&nbsp;</p>
<h2>Author</h2>
<p> This manual page was written by Jens Schmalzing &lt;jensen [at] debian.org&gt; for <code>Debian GNU/Linux</code> using the manual page by Klaus Halfmann &lt;halfmann [at] libra.de&gt; that comes with the source code and documentation from the <code>Tech Info Library</code>.<br />
&nbsp; </p>
<h2>Index</h2>
