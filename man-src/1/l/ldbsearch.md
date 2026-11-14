---
title: "ldbsearch(1)"
name: "ldbsearch"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldbsearch/"
description: "ldbsearch – Search for records in a LDB database"
---

<h2 class="name">NAME</h2>
<p> ldbsearch &#8211; Search for records in a LDB database </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ldbsearch</code> [-h] [-s base|one|sub] [-b basedn] [-i] [-H LDB-URL] [expression] [attributes]</dl>
<h2>DESCRIPTION</h2>
<dd>ldbsearch searches a LDB database for records matching the specified expression (see the <a href="/docs/linux/man/1-ldapsearch/">ldapsearch</a>(1) manpage for a description of the expression format). For each record, the specified attributes are printed.</p>
<h2>OPTIONS</h2>
<p> -h</p>
<dl>
<dt>
<dd> Show list of available options.</dl>
<p> -H &lt;ldb-url&gt;</p>
<dl>
<dt>
<dd> LDB URL to connect to. See <a href="/docs/linux/man/3-ldb/">ldb</a>(3) for details.</dl>
<p> -s one|sub|base</p>
<dl>
<dt>
<dd> Search scope to use. One-level, subtree or base.</dl>
<p> -i</p>
<dl>
<dt>
<dd> Read search expressions from stdin.</dl>
<p> -b basedn</p>
<dl>
<dt>
<dd> Specify Base DN to use.</dl>
<h2>ENVIRONMENT</h2>
<p> LDB_URL</p>
<dl>
<dt>
<dd> LDB URL to connect to (can be overrided by using the -H command-line option.)</dl>
<h2>VERSION</h2>
<p> This man page is correct for version 1.1 of LDB.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-ldb/">ldb</a>(3), <a href="/docs/linux/man/1-ldbedit/">ldbedit</a>(1)</p>
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
