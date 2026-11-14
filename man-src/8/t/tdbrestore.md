---
title: "tdbrestore(8)"
name: "tdbrestore"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tdbrestore/"
description: "tdbrestore – tool for creating a TDB file out of a tdbdump output"
---

<p>tdbrestore &#8211; tool for creating a TDB file out of a tdbdump output</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>tdbrestore</code> {tdbfilename}</dl>
<h2>Description</h2>
<dd>This tool is part of the <code><a href="/docs/linux/man/1-samba/">samba</a></code>(1) suite. </p>
<p> <code>tdbrestore</code> is a very simple utility that &#8216;restores&#8217; the contents of dump file into TDB (Trivial DataBase) file. The dump file is obtained from the tdbdump command. </p>
<p> This tool wait on the standard input for the content of the dump and will write the tdb in the tdbfilename parameter. </p>
<p> This tool can be used for unpacking the content of tdb as backup mean.</p>
<h2>Version</h2>
<p>This man page is correct for version 3 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. This tool was initially written by Volker Lendecke based on an idea by Simon McVittie. </p>
<p> The tdbrestore man page was written by Matthieu Patou.</p>
