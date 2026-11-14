---
title: "ldb3rename(1)"
name: "ldb3rename"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldb3rename/"
---

ldbrename - Edit LDB databases using your favorite editor

<h2>Synopsis</h2>

<dl>
<dt> FCldbrenameF[] [-h] [-o options] {olddn} {newdb}</dl>

<h2>DESCRIPTION</h2>

 

<dd>ldbrename is a utility that allows you to rename trees in an LDB database based by DN. This utility takes two arguments: the original DN name of the top element and the DN to change it to.

<h2>OPTIONS</h2>

 

 -h
<dl>
<dt>
<dd> Show list of available options.</dl>
 

 -H &lt;ldb-url&gt;
<dl>
<dt>
<dd> LDB URL to connect to. See <a HREF="/docs/linux/man/7-ldb/">ldb</a>(7) for details.</dl>
 

 -o options
<dl>
<dt>
<dd> Extra ldb options, such as modules.</dl>

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


