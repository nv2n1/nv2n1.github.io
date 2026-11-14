---
title: "ntdbrestore(8)"
name: "ntdbrestore"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntdbrestore/"
description: "ntdbrestore – tool for creating a NTDB file out of a ntdbdump output"
---

<p>ntdbrestore &#8211; tool for creating a NTDB file out of a ntdbdump output</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ntdbrestore</code> {ntdbfilename}</dl>
<h2>Description</h2>
<dd>This tool is part of the <code><a href="/docs/linux/man/1-samba/">samba</a></code>(1) suite. </p>
<p> <code>ntdbrestore</code> is a very simple utility that &#8216;restores&#8217; the contents of dump file into NTDB (New Trivial DataBase) file. The dump file is obtained from the ntdbdump or tdbdump commands. </p>
<p> This tool wait on the standard input for the content of the dump and will write the ntdb in the ntdbfilename parameter. </p>
<p> This tool can be used to translate between ntdb and tdb files by dumping and restoring.</p>
<h2>Version</h2>
<p>This man page is correct for version 4 of the Samba suite.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ntdbdump/">ntdbdump</a>(8), <a href="/docs/linux/man/8-tdbrestore/">tdbrestore</a>(8)</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. ntdbrestore was written by Rusty Russell based on tdbrestore, which was initially written by Volker Lendecke based on an idea by Simon McVittie. </p>
<p> The ntdbrestore man page was written by Rusty Russell, based on the tdbrestore man page by Matthieu Patou.</p>
