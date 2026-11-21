---
title: "ldbsearch(1)"
name: "ldbsearch"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldbsearch/"
description: "ldbsearch – Search for records in a LDB database"
---

<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ldbsearch</code> [-h] [-s base|one|sub] [-b basedn] [-i] [-H LDB-URL] [expression] [attributes]</dt></dl>
<h2>DESCRIPTION</h2>
<dd>ldbsearch searches a LDB database for records matching the specified expression (see the <a href="/docs/linux/man/1-ldapsearch/">ldapsearch</a>(1) manpage for a description of the expression format). For each record, the specified attributes are printed.</dd>
<h2>OPTIONS</h2>
<p> -h</p>
<dl>
<dt>
</dt><dd> Show list of available options.</dd></dl>
<p> -H &lt;ldb-url&gt;</p>
<dl>
<dt>
</dt><dd> LDB URL to connect to. See <a href="/docs/linux/man/3-ldb/">ldb</a>(3) for details.</dd></dl>
<p> -s one|sub|base</p>
<dl>
<dt>
</dt><dd> Search scope to use. One-level, subtree or base.</dd></dl>
<p> -i</p>
<dl>
<dt>
</dt><dd> Read search expressions from stdin.</dd></dl>
<p> -b basedn</p>
<dl>
<dt>
</dt><dd> Specify Base DN to use.</dd></dl>
<h2>ENVIRONMENT</h2>
<p> LDB_URL</p>
<dl>
<dt>
</dt><dd> LDB URL to connect to (can be overrided by using the -H command-line option.)</dd></dl>
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
<dt> 1.</dt>
<dd> Andrew Tridgell</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://samba.org/~tridge/">http://samba.org/~tridge/</a></dd></dl>
</dl>
