---
title: "tdbdump(8)"
name: "tdbdump"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tdbdump/"
description: "tdbdump – tool for printing the contents of a TDB file"
---

<p>tdbdump &#8211; tool for printing the contents of a TDB file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>tdbdump</code> [-k&nbsp;<wbr><i>keyname</i>] [-e] [-h] {filename}</dl>
<h2>Description</h2>
<dd>This tool is part of the <code><a href="/docs/linux/man/1-samba/">samba</a></code>(1) suite. </p>
<p> <code>tdbdump</code> is a very simple utility that &#8216;dumps&#8217; the contents of a TDB (Trivial DataBase) file to standard output in a human-readable format. </p>
<p> This tool can be used when debugging problems with TDB files. It is intended for those who are somewhat familiar with Samba internals.</p>
<h2>Options</h2>
<p>-h</p>
<dl>
<dd>Get help information.</dl>
<p> -k <i>keyname</i></p>
<dl>
<dd>The <code>-k</code> option restricts dumping to a single key, if found.</dl>
<p> -e</p>
<dl>
<dd>The <code>-e</code> tries to dump out from a corrupt database. Naturally, such a dump is unreliable, at best.</dl>
<h2>Version</h2>
<p>This man page is correct for version 3 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> The tdbdump man page was written by Jelmer Vernooij.</p>
