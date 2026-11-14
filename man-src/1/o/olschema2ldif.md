---
title: "olschema2ldif(1)"
name: "olschema2ldif"
section: "1"
letter: "o"
url: "/docs/linux/man/1-olschema2ldif/"
description: "oLschema2ldif – Converts LDAP schema’s to LDB-compatible LDIF"
---

<p>oLschema2ldif &#8211; Converts LDAP schema&#8217;s to LDB-compatible LDIF </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>oLschema2ldif</code> [-I INPUT-FILE] [-O OUTPUT-FILE]</dl>
<h2>Description</h2>
<dd>oLschema2ldif is a simple tool that converts standard OpenLDAP schema files to a LDIF format that is understood by LDB.</p>
<h2>Options</h2>
<p>-I input-file</p>
<dl COMPACT>
<dd>OpenLDAP schema to read. If none are specified, the schema file will be read from standard input.</dl>
<p> -O output-file</p>
<dl COMPACT>
<dd>File to write ldif version of schema to.</dl>
<h2>Version</h2>
<p>This man page is correct for version 4.0 of the Samba suite.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/7-ldb/">ldb</a>(7), ldbmodify, ldbdel, <a href="/docs/linux/man/5-ldif/">ldif</a>(5)</p>
<h2>Author</h2>
<p>ldb was written by m[blue]<code>Andrew Tridgell</code>m[]<font SIZE="-2">[1]</font>. oLschema2ldif was written by m[blue]<code>Simo Sorce</code>m[]<font SIZE="-2">[2]</font>. </p>
<p> If you wish to report a problem or make a suggestion then please see the m[blue]<code><a rel="nofollow" href="http://ldb.samba.org/">http://ldb.samba.org/</a></code>m[] web site for current contact and maintainer information.</p>
<h2>Notes</h2>
<dl COMPACT>
<dt> 1.</p>
<dd>Andrew Tridgell</p>
<dl COMPACT>
<dd><a rel="nofollow" href="https://www.samba.org/~tridge/">https://www.samba.org/~tridge/</a></dl>
<dt> 2.</p>
<dd>Simo Sorce</p>
<dl COMPACT>
<dd>mailto:idra [at] samba.org</dl>
</dl>
