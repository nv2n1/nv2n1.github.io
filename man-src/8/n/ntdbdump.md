---
title: "ntdbdump(8)"
name: "ntdbdump"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntdbdump/"
description: "ntdbdump – tool for printing the contents of an NTDB file"
---

<p>ntdbdump &#8211; tool for printing the contents of an NTDB file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ntdbdump</code> [-k&nbsp;<wbr><i>keyname</i>] [-e] [-h] {filename}</dl>
<h2>Description</h2>
<dd>This tool is part of the <code><a href="/docs/linux/man/1-samba/">samba</a></code>(1) suite. </p>
<p> <code>ntdbdump</code> is a very simple utility that &#8216;dumps&#8217; the contents of a NTDB (New Trivial DataBase) file to standard output in a human-readable format. </p>
<p> This tool can be used when debugging problems with NTDB files. It is intended for those who are somewhat familiar with Samba internals.</p>
<h2>Options</h2>
<p>-h</p>
<dl>
<dd>Get help information.</dl>
<p> -k <i>keyname</i></p>
<dl>
<dd>The <code>-k</code> option restricts dumping to a single key, if found.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-tdbdump/">tdbdump</a>(8), <a href="/docs/linux/man/8-ntdbtool/">ntdbtool</a>(8)</p>
<h2>Version</h2>
<p>This man page is correct for version 4 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> The ntdbdump man page was written by Rusty Russell, base on the tdbdump man page by Jelmer Vernooij.</p>
