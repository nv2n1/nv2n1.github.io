---
title: "ldbmodify(1)"
name: "ldbmodify"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldbmodify/"
description: "ldbmodify – Modify records in a LDB database"
---

<h2 class="name">NAME</h2>
<p> ldbmodify &#8211; Modify records in a LDB database </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ldbmodify</code> [-H LDB-URL] [ldif-file]</dl>
<h2>DESCRIPTION</h2>
<dd>ldbmodify changes, adds and deletes records in a LDB database. The changes that should be made to the LDB database are read from the specified LDIF-file. If &#8211; is specified as the filename, input is read from stdin. </p>
<p> For now, see <a href="/docs/linux/man/1-ldapmodify/">ldapmodify</a>(1) for details on the LDIF file format.</p>
<h2>OPTIONS</h2>
<p> -H &lt;ldb-url&gt;</p>
<dl>
<dt>
<dd> LDB URL to connect to. See <a href="/docs/linux/man/3-ldb/">ldb</a>(3) for details.</dl>
<h2>ENVIRONMENT</h2>
<p> LDB_URL</p>
<dl>
<dt>
<dd> LDB URL to connect to (can be overrided by using the -H command-line option.)</dl>
<h2>VERSION</h2>
<p> This man page is correct for version 1.1 of LDB.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-ldb/">ldb</a>(3), ldbedit</p>
<h2>AUTHOR</h2>
<p> ldb was written by m[blue]<code>Andrew Tridgell</code>m[]<font SIZE="-2">[1]</font>. </p>
<p> If you wish to report a problem or make a suggestion then please see the m[blue]<code><a rel="nofollow" href="http://ldb.samba.org/">http://ldb.samba.org/</a></code>m[] web site for current contact and maintainer information. </p>
<p> This manpage was written by Jelmer Vernooij.</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Andrew Tridgell</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://samba.org/~tridge/">http://samba.org/~tridge/</a></dl>
</dl>
<h2>Index</h2>
