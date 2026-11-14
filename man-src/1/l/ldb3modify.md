---
title: "ldb3modify(1)"
name: "ldb3modify"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldb3modify/"
---

ldbmodify - Modify records in a LDB database

<h2>Synopsis</h2>

<dl>
<dt> FCldbmodifyF[] [-H LDB-URL] [ldif-file]</dl>

<h2>DESCRIPTION</h2>

 

<dd>ldbmodify changes, adds and deletes records in a LDB database. The changes that should be made to the LDB database are read from the specified LDIF-file. If - is specified as the filename, input is read from stdin. 

 For now, see <a HREF="/docs/linux/man/1-ldapmodify/">ldapmodify</a>(1) for details on the LDIF file format.

<h2>OPTIONS</h2>

 

 -H &lt;ldb-url&gt;
<dl>
<dt>
<dd> LDB URL to connect to. See <a HREF="/docs/linux/man/7-ldb/">ldb</a>(7) for details.</dl>

<h2>ENVIRONMENT</h2>

 

 LDB_URL
<dl>
<dt>
<dd> LDB URL to connect to (can be overrided by using the -H command-line option.)</dl>

<h2>VERSION</h2>

 

 This man page is correct for version 4.0 of the Samba suite.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/7-ldb/">ldb</a>(7), ldbedit

<h2>AUTHOR</h2>

 

 ldb was written by Andrew Tridgell. 

 If you wish to report a problem or make a suggestion then please see the : <a rel="nofollow" HREF="http://ldb.samba.org/">http://ldb.samba.org/</a> web site for current contact and maintainer information. 

 This manpage was written by Jelmer Vernooij. 

<h2>Index</h2>


