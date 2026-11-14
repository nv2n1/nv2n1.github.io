---
title: "ldbedit(1)"
name: "ldbedit"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldbedit/"
description: "ldbedit – Edit LDB databases using your preferred editor"
---

<h2 class="name">NAME</h2>
<p> ldbedit &#8211; Edit LDB databases using your preferred editor </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ldbedit</code> [-?] [&#8211;usage] [-s base|one|sub] [-b basedn] [-a] [-e editor] [-H LDB-URL] [expression] [attributes&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>ldbedit is a utility that allows you to edit LDB entries (in tdb files, sqlite files or LDAP servers) using your preferred editor. ldbedit generates an LDIF file based on your query, allows you to edit the LDIF, and then merges that LDIF back into the LDB backend.</p>
<h2>OPTIONS</h2>
<p> -?, &#8211;help</p>
<dl>
<dt>
<dd> Show list of available options, and a phrase describing what that option does.</dl>
<p> &#8211;usage</p>
<dl>
<dt>
<dd> Show list of available options. This is similar to the help option, however it does not provide any description, and is hence shorter.</dl>
<p> -H &lt;ldb-url&gt;</p>
<dl>
<dt>
<dd> LDB URL to connect to. For a tdb database, this will be of the form tdb://<i>filename</i>. For a LDAP connection over unix domain sockets, this will be of the form ldapi://<i>socket</i>. For a (potentially remote) LDAP connection over TCP, this will be of the form ldap://<i>hostname</i>. For an SQLite database, this will be of the form sqlite://<i>filename</i>.</dl>
<p> -s one|sub|base</p>
<dl>
<dt>
<dd> Search scope to use. One-level, subtree or base.</dl>
<p> -a, -all</p>
<dl>
<dt>
<dd> Edit all records. This allows you to apply the same change to a number of records at once. You probably want to combine this with an expression of the form &quot;objectclass=*&quot;.</dl>
<p> -e editor, &#8211;editor editor</p>
<dl>
<dt>
<dd> Specify the editor that should be used (overrides the VISUAL and EDITOR environment variables). If this option is not used, and neither VISUAL nor EDITOR environment variables are set, then the vi editor will be used.</dl>
<p> -b basedn</p>
<dl>
<dt>
<dd> Specify Base Distinguished Name to use.</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Make ldbedit more verbose about the operations that are being performed. Without this option, ldbedit will only provide a summary change line.</dl>
<h2>ENVIRONMENT</h2>
<p> LDB_URL</p>
<dl>
<dt>
<dd> LDB URL to connect to. This can be overridden by using the -H command-line option.)</dl>
<p> VISUAL and EDITOR</p>
<dl>
<dt>
<dd> Environment variables used to determine what editor to use. VISUAL takes precedence over EDITOR, and both are overridden by the -e command-line option.</dl>
<h2>VERSION</h2>
<p> This man page is correct for version 1.1 of LDB.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-ldb/">ldb</a>(3), <a href="/docs/linux/man/1-ldbmodify/">ldbmodify</a>(1), <a href="/docs/linux/man/1-ldbdel/">ldbdel</a>(1), <a href="/docs/linux/man/5-ldif/">ldif</a>(5), <a href="/docs/linux/man/1-vi/">vi</a>(1)</p>
<h2>AUTHOR</h2>
<p> ldb was written by m[blue]<code>Andrew Tridgell</code>m[]<font SIZE="-2">[1]</font>. </p>
<p> If you wish to report a problem or make a suggestion then please see the m[blue]<code><a rel="nofollow" href="http://ldb.samba.org/">http://ldb.samba.org/</a></code>m[] web site for current contact and maintainer information. </p>
<p> This manpage was written by Jelmer Vernooij and updated by Brad Hards.</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Andrew Tridgell</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://samba.org/~tridge/">http://samba.org/~tridge/</a></dl>
</dl>
<h2>Index</h2>
