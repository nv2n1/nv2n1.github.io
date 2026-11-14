---
title: "hpcopy(1)"
name: "hpcopy"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hpcopy/"
description: "hpcopy — copy files from an HFS+ volume"
---

<h2>NAME</h2>
<p> hpcopy &#8212; copy files from an HFS+ volume</p>
<h2>SYNOPSIS</h2>
<p> <code>hpcopy</code> [<code>-m</code> | <code>-b</code> | <code>-t</code> | <code>-r</code> | <code>-a</code> ] <i>source-path</i> &#8230; <i>target-path</i></p>
<h2>Description</h2>
<p> <code>hpcopy</code> copies files and directories from an HFS+ volume. If multiple files are to be copied, the target path must be a directory.<br />
&nbsp; </p>
<p> Since Macintosh files contain two forks, which are not representably in Unix file systems, copies use one of several translation modes:<br />
&nbsp;</p>
<dl>
<dt><code>-m</code></p>
<dd> <code>Mac Binary II</code> is a format for binary file transfer. Both forks of the Macintosh file are preserved. This is the recommended mode for transferring arbitrary Macintosh files.<br />
&nbsp;</p>
<dt><code>-b</code></p>
<dd> <code>BinHex</code> also preserves both forks of the Macintosh file. In addition, the encoded file contains only ASCII characters, making it suitable for electronic mail transmission.<br />
&nbsp;</p>
<dt><code>-t</code></p>
<dd> <code>Text</code> copies only the data fork of the Macintosh file, while the contents of the resource fork are lost. In addition, this mode translates end-of-line characters. This translation should be used for text files.<br />
&nbsp;</p>
<dt><code>-r</code></p>
<dd> <code>Raw Data</code> copies only the data fork of the Macintosh file, while the contents of the resource fork are lost.<br />
&nbsp;</p>
<dt><code>-a</code></p>
<dd> <code>Automatic</code> mode applies a set of predefined heuristics to determine the appropriate translation. This is the default if no mode is specified.<br />
&nbsp;</dl>
<h2>See also</h2>
<p> <a href="/docs/linux/man/7-hfsplus/">hfsplus</a>(7), <a href="/docs/linux/man/1-hpmount/">hpmount</a>(1), <a href="/docs/linux/man/1-hpls/">hpls</a>(1), <a href="/docs/linux/man/1-hpcd/">hpcd</a>(1), <a href="/docs/linux/man/1-hprm/">hprm</a>(1), <a href="/docs/linux/man/1-hpmkdir/">hpmkdir</a>(1), <a href="/docs/linux/man/1-hppwd/">hppwd</a>(1), <a href="/docs/linux/man/1-hpumount/">hpumount</a>(1), <a href="/docs/linux/man/1-hpfsck/">hpfsck</a>(1).<br />
&nbsp;</p>
<h2>Author</h2>
<p> This manual page was written by Jens Schmalzing &lt;jensen [at] debian.org&gt; for <code>Debian GNU/Linux</code> using the manual page by Klaus Halfmann &lt;halfmann [at] libra.de&gt; that comes with the source code and documentation from the <code>Tech Info Library</code>.<br />
&nbsp; </p>
<h2>Index</h2>
