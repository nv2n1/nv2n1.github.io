---
title: "fuse-zip(1)"
name: "fuse-zip"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fuse-zip/"
description: "fuse-zip – a FUSE filesystem for zip archives with write support"
---

<h2>NAME</h2>
<p> fuse-zip &#8211; a FUSE filesystem for zip archives with write support</p>
<h2>SYNOPSIS</h2>
<p> <code>fuse-zip</code> zip-file [<i>fusermount</i> <i>options</i>] mount-point</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> print help</p>
<dt><code>-V</code></p>
<dd> print version</p>
<dt><code>-o opt[,opt&#8230;]</code></p>
<dd> mount options</p>
<dt><code>-q</code></p>
<dd> quiet</p>
<dt><code>-f</code></p>
<dd> don&#8217;t detach from terminal</p>
<dt><code>-d</code></p>
<dd> turn on debugging, also implies -f</dl>
<p> If you want to specify character set conversion for file names in archive, use the following fusermount options: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-omodules=iconv,from_code=$charset1,to_code=$charset2 </p>
<p> See FUSE documentation for details.</p>
<h2>DESCRIPTION</h2>
<p> <code>fuse-zip</code> is a fuse filesystem, that enables any program to work with a ZIP archive as though it is a plain directory. Unlike KIO or Gnome VFS, it can be used in any application without modifications. </p>
<p> Unlike other FUSE filesystems, only fuse-zip provides write support to ZIP archives. Also, fuse-zip is faster that all known implementations on large archives with many files.</p>
<h2>USAGE</h2>
<p> General usage would look like this </p>
<table>
<tr VALIGN=top>
<td>1</td>
<td>mkdir&nbsp;<wbr>/tmp/zipArchive
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td>fuse-zip foobar.zip /tmp/zipArchive
</td>
</tr>
<tr VALIGN=top>
<td>3</td>
<td>(do something with the mounted file system)
</td>
</tr>
<tr VALIGN=top>
<td>4</td>
<td>fusermount -u /tmp/zipArchive
</td>
</tr>
</table>
<p> Be patient. Wait for fuse-zip process finish after unmounting, especially on a big archives.</p>
<h2>FILES</h2>
<dl>
<dt><i>/var/log/user.log</i></p>
<dd> see this file in case any errors occur</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fusermount/">fusermount</a></code>(1).</p>
<h2>LICENSE</h2>
<p> This is Free Software; this software is licensed under the LGPL version 2, as published by the Free Software Foundation, or later. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>AUTHORS</h2>
<p> Alexander Galanin &lt;gaa.nnov [at] mail.ru&gt;.<br />
 This manual page was originally written by Kirill Zaitsev &lt;teferiincub [at] gmail.com&gt;. Updated by Alexander Galanin. </p>
<h2>Index</h2>
