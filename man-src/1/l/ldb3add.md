---
title: "ldb3add(1)"
name: "ldb3add"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldb3add/"
---

ldbadd - Command-line utility for adding records to an LDB

<h2>Synopsis</h2>

<dl>
<dt> FCldbaddF[] [-h] [-H LDB-URL] [ldif-file1] [ldif-file2] [...]</dl>

<h2>DESCRIPTION</h2>

 

<dd>ldbadd adds records to an <a HREF="/docs/linux/man/7-ldb/">ldb</a>(7) database. It reads the <a HREF="/docs/linux/man/5-ldif/">ldif</a>(5) files specified on the command line and adds the records from these files to the LDB database, which is specified by the -H option or the LDB_URL environment variable. 

 If - is specified as a ldb file, the ldif input is read from standard input.

<h2>OPTIONS</h2>

 

 -h
<dl>
<dt>
<dd> Show list of available options.</dl>
 

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

 

 <a HREF="/docs/linux/man/7-ldb/">ldb</a>(7), ldbmodify, ldbdel, <a HREF="/docs/linux/man/5-ldif/">ldif</a>(5)

<h2>AUTHOR</h2>

 

 ldb was written by Andrew Tridgell. 

 If you wish to report a problem or make a suggestion then please see the : <a rel="nofollow" HREF="http://ldb.samba.org/">http://ldb.samba.org/</a> web site for current contact and maintainer information. 

 This manpage was written by Jelmer Vernooij. 

<h2>Index</h2>


