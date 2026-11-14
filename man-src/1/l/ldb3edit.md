---
title: "ldb3edit(1)"
name: "ldb3edit"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldb3edit/"
---

ldbedit - Edit LDB databases using your preferred editor

<h2>Synopsis</h2>

<dl>
<dt> FCldbeditF[] [-?] [--usage] [-s base|one|sub] [-b basedn] [-a] [-e editor] [-H LDB-URL] [expression] [attributes...]</dl>

<h2>DESCRIPTION</h2>

 

<dd>ldbedit is a utility that allows you to edit LDB entries (in tdb files, sqlite files or LDAP servers) using your preferred editor. ldbedit generates an LDIF file based on your query, allows you to edit the LDIF, and then merges that LDIF back into the LDB backend.

<h2>OPTIONS</h2>

 

 -?, --help
<dl>
<dt>
<dd> Show list of available options, and a phrase describing what that option does.</dl>
 

 --usage
<dl>
<dt>
<dd> Show list of available options. This is similar to the help option, however it does not provide any description, and is hence shorter.</dl>
 

 -H &lt;ldb-url&gt;
<dl>
<dt>
<dd> LDB URL to connect to. For a tdb database, this will be of the form tdb://<i>filename</i>. For a LDAP connection over unix domain sockets, this will be of the form ldapi://<i>socket</i>. For a (potentially remote) LDAP connection over TCP, this will be of the form ldap://<i>hostname</i>. For an SQLite database, this will be of the form sqlite://<i>filename</i>.</dl>
 

 -s one|sub|base
<dl>
<dt>
<dd> Search scope to use. One-level, subtree or base.</dl>
 

 -a, -all
<dl>
<dt>
<dd> Edit all records. This allows you to apply the same change to a number of records at once. You probably want to combine this with an expression of the form &quot;objectclass=*&quot;.</dl>
 

 -e editor, --editor editor
<dl>
<dt>
<dd> Specify the editor that should be used (overrides the VISUAL and EDITOR environment variables). If this option is not used, and neither VISUAL nor EDITOR environment variables are set, then the vi editor will be used.</dl>
 

 -b basedn
<dl>
<dt>
<dd> Specify Base Distinguished Name to use.</dl>
 

 -v, --verbose
<dl>
<dt>
<dd> Make ldbedit more verbose about the operations that are being performed. Without this option, ldbedit will only provide a summary change line.</dl>

<h2>ENVIRONMENT</h2>

 

 LDB_URL
<dl>
<dt>
<dd> LDB URL to connect to. This can be overridden by using the -H command-line option.)</dl>
 

 VISUAL and EDITOR
<dl>
<dt>
<dd> Environment variables used to determine what editor to use. VISUAL takes precedence over EDITOR, and both are overridden by the -e command-line option.</dl>

<h2>VERSION</h2>

 

 This man page is correct for version 4.0 of the Samba suite.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/7-ldb/">ldb</a>(7), <a HREF="/docs/linux/man/1-ldbmodify/">ldbmodify</a>(1), <a HREF="/docs/linux/man/1-ldbdel/">ldbdel</a>(1), <a HREF="/docs/linux/man/5-ldif/">ldif</a>(5), <a HREF="/docs/linux/man/1-vi/">vi</a>(1)

<h2>AUTHOR</h2>

 

 ldb was written by Andrew Tridgell. 

 If you wish to report a problem or make a suggestion then please see the : <a rel="nofollow" HREF="http://ldb.samba.org/">http://ldb.samba.org/</a> web site for current contact and maintainer information. 

 This manpage was written by Jelmer Vernooij and updated by Brad Hards. 

<h2>Index</h2>


