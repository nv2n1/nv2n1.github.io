---
title: "ldb3del(1)"
name: "ldb3del"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldb3del/"
---

ldbdel - Command-line program for deleting LDB records

<h2>Synopsis</h2>

<dl>
<dt> FCldbdelF[] [-h] [-H LDB-URL] [dn] [...]</dt></dl>

<h2>DESCRIPTION</h2>

 

<dd>ldbdel deletes records from an ldb(7) database. It deletes the records identified by the dn's specified on the command-line. 

 ldbdel uses either the database that is specified with the -H option or the database specified by the LDB_URL environment variable.

<h2>OPTIONS</h2>

 

 -h
</dd><dl>
<dt>
</dt><dd> Show list of available options.</dd></dl>
 

 -H &lt;ldb-url&gt;
<dl>
<dt>
</dt><dd> LDB URL to connect to. See ldb(7) for details.</dd></dl>

<h2>ENVIRONMENT</h2>

 

 LDB_URL
<dl>
<dt>
</dt><dd> LDB URL to connect to (can be overrided by using the -H command-line option.)</dd></dl>

<h2>VERSION</h2>

 

 This man page is correct for version 4.0 of the Samba suite.

<h2>SEE ALSO</h2>

 

 ldb(7), ldbmodify, ldbadd, <a HREF="/docs/linux/man/5-ldif/">ldif</a>(5)

<h2>AUTHOR</h2>

 

 ldb was written by Andrew Tridgell. 

 If you wish to report a problem or make a suggestion then please see the : <a rel="nofollow" HREF="http://ldb.samba.org/">http://ldb.samba.org/</a> web site for current contact and maintainer information. 

 ldbdel was written by Andrew Tridgell. 

 This manpage was written by Jelmer Vernooij.
