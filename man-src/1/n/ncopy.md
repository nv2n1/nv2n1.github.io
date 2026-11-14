---
title: "ncopy(1)"
name: "ncopy"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncopy/"
description: "ncopy – NetWare file copy"
---

<h2>NAME</h2>
<p> ncopy &#8211; NetWare file copy </p>
<h2>SYNOPSIS</h2>
<p> <code>ncopy -V</code> </p>
<p> <code>ncopy</code> [ <code>-vmMnpptu</code> ] [ <code>-s</code> <i>amount</i> ] <code>file</code> <code>destinationfile</code>|<code>directory</code> </p>
<p> <code>ncopy</code> [ <code>-vmMnpptu</code> ] [ <code>-s</code> <i>amount</i> ] <code>file1</code> [ <code>file2 &#8230;</code> ] <code>directory</code> </p>
<p> <code>ncopy</code> <code>-r</code> [ <code>-vmMnpptu</code> ] [ <code>-s</code> <i>amount</i> ] <code>srcdir</code> <code>dstdir</code> </p>
<h2>DESCRIPTION</h2>
<p> With <code>ncopy</code> you can copy files to different locations on a single NetWare file server without generating excess network traffic. The program uses a NetWare function to do the copy rather than transferring the file across the network for both the read and write. </p>
<p> If the last argument is a directory, <code>ncopy</code> will copy the source file(s) into the directory. If only two files are given and the last argument is not a directory, it will copy the source file to the destination file. </p>
<p> If the source and destination files are not on the same NetWare server (or are not on NetWare servers at all), <code>ncopy</code> will do a normal file copy.</p>
<h2>OPTIONS</h2>
<p> <code>-V</code></p>
<dl>
<dt>
<dd> Show version number and exit</dl>
<p> <code>-v</code></p>
<dl>
<dt>
<dd> Verbose copy. Will show current file and percentage completion.</dl>
<p> <code>-m</code></p>
<dl>
<dt>
<dd> Copy MAC resource fork. Copies MAC resource fork together with data fork.</dl>
<p> <code>-M</code></p>
<dl>
<dt>
<dd> Copy MAC resource fork to/from non-MAC filesystem. It expects/creates resource forks in subdirectory <i>.rsrc</i> of each directory copied. </p>
<p> If you want to copy files from MAC volume to <i>.rsrc</i> scheme, you must specify both options, <code>-mM</code>. It is not possible to create <i>.rsrc</i> directory on MAC-aware volume in one step, you must first copy data to non-MAC media using <code>ncopy -mM</code> and then copy them back using <code>ncopy -M</code>. </p>
<p> If you want to copy files from <i>.rsrc</i> scheme on MAC volume to real MAC multiple-forks file, you must first copy data to non-MAC filesystem using <code>ncopy -M</code> and then copy them back using <code>ncopy -mM</code>.</dl>
<p> <code>-n</code></p>
<dl>
<dt>
<dd> Nice NetWare copy. Will sleep for a second between copying blocks on the NetWare server. Gives other people a chance to do some work on the NetWare server when you are copying large files. This has no effect if you are not copying on a NetWare server.</dl>
<p> <code>-s</code> <i>amount</i></p>
<dl>
<dt>
<dd> Nice time slice factor. Used in conjunction with the <code>-n</code> option, this specifies the number of 100K blocks to copy before sleeping. Default is 10. (1 Megabyte)</dl>
<p> <code>-p</code></p>
<dl>
<dt>
<dd> Preserve file attributes and date/time during copy.</dl>
<p> <code>-pp</code></p>
<dl>
<dt>
<dd> Preserve file attributes, date/time and owner during copy. Name of owner is preserved, not owner ID.</dl>
<p> <code>-t</code></p>
<dl>
<dt>
<dd> Preserve trustees during copy. Trustee name is preserved, not ID.</dl>
<p> <code>-r</code></p>
<dl>
<dt>
<dd> Perform recursive copy.</dl>
<p> <code>-u</code></p>
<dl>
<dt>
<dd> Perform copy only if mtime or size differs.</dl>
<h2>BUGS</h2>
<p> <code>ncopy</code> does not preserve long (MAC, NFS, FTAM, OS2) names during copy. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-ncpmount/">ncpmount</a>(8), <a href="/docs/linux/man/8-ncpumount/">ncpumount</a>(8)</code> </p>
<h2>CREDITS</h2>
<p> ncopy was written by Brian G. Reid (breid [at] tim.com) and Tom C. Henderson (thenderson [at] tim.com). Many thanks to Volker Lendecke (lendecke [at] math.uni-goettingen.de) for the ncpfs and ncplib which made ncopy possible. Some further work was done by Petr Vandrovec (vandrove [at] vc.cvut.cz). </p>
<h2>Index</h2>
