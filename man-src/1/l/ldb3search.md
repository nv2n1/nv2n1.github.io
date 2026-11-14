---
title: "ldb3search(1)"
name: "ldb3search"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldb3search/"
---

ldbsearch - Search for records in a LDB database

<h2>Synopsis</h2>

<dl>
<dt> FCldbsearchF[] [-h] [-s base|one|sub] [-b basedn] [-i] [-H LDB-URL] [expression] [attributes]</dl>

<h2>DESCRIPTION</h2>

 

<dd>ldbsearch searches a LDB database for records matching the specified expression (see the <a HREF="/docs/linux/man/1-ldapsearch/">ldapsearch</a>(1) manpage for a description of the expression format). For each record, the specified attributes are printed.

<h2>OPTIONS</h2>

 

 -h
<dl>
<dt>
<dd> Show list of available options.</dl>
 

 -H &lt;ldb-url&gt;
<dl>
<dt>
<dd> LDB URL to connect to. See <a HREF="/docs/linux/man/7-ldb/">ldb</a>(7) for details.</dl>
 

 -s one|sub|base
<dl>
<dt>
<dd> Search scope to use. One-level, subtree or base.</dl>
 

 -i
<dl>
<dt>
<dd> Read search expressions from stdin.</dl>
 

 -b basedn
<dl>
<dt>
<dd> Specify Base DN to use.</dl>

<h2>ENVIRONMENT</h2>

 

 LDB_URL
<dl>
<dt>
<dd> LDB URL to connect to (can be overrided by using the -H command-line option.)</dl>

<h2>VERSION</h2>

 

 This man page is correct for version 4.0 of the Samba suite.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/7-ldb/">ldb</a>(7), <a HREF="/docs/linux/man/1-ldbedit/">ldbedit</a>(1)

<h2>AUTHOR</h2>

 

 ldb was written by Andrew Tridgell. 

 If you wish to report a problem or make a suggestion then please see the : <a rel="nofollow" HREF="http://ldb.samba.org/">http://ldb.samba.org/</a> web site for current contact and maintainer information. 

 This manpage was written by Jelmer Vernooij. 

<h2>Index</h2>


