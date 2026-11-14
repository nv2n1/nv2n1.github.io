---
title: "ldbdel(1)"
name: "ldbdel"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldbdel/"
description: "ldbdel – Command-line program for deleting LDB records"
---

<h2 class="name">NAME</h2>
<p> ldbdel &#8211; Command-line program for deleting LDB records </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ldbdel</code> [-h] [-H LDB-URL] [dn] [&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>ldbdel deletes records from an <a href="/docs/linux/man/3-ldb/">ldb</a>(3) database. It deletes the records identified by the dn&#8217;s specified on the command-line. </p>
<p> ldbdel uses either the database that is specified with the -H option or the database specified by the LDB_URL environment variable.</p>
<h2>OPTIONS</h2>
<p> -h</p>
<dl>
<dt>
<dd> Show list of available options.</dl>
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
<p> <a href="/docs/linux/man/3-ldb/">ldb</a>(3), ldbmodify, ldbadd, <a href="/docs/linux/man/5-ldif/">ldif</a>(5)</p>
<h2>AUTHOR</h2>
<p> ldb was written by m[blue]<code>Andrew Tridgell</code>m[]<font SIZE="-2">[1]</font>. </p>
<p> If you wish to report a problem or make a suggestion then please see the m[blue]<code><a rel="nofollow" href="http://ldb.samba.org/">http://ldb.samba.org/</a></code>m[] web site for current contact and maintainer information. </p>
<p> ldbdel was written by Andrew Tridgell. </p>
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
