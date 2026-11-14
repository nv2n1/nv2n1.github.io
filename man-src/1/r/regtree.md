---
title: "regtree(1)"
name: "regtree"
section: "1"
letter: "r"
url: "/docs/linux/man/1-regtree/"
description: "regtree – Text-mode registry viewer"
---

<h2 class="name">NAME</h2>
<p> regtree &#8211; Text-mode registry viewer </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>regtree</code> [&#8211;help] [&#8211;backend=BACKEND] [&#8211;fullpath] [&#8211;no-values] [&#8211;credentials=CREDENTIALS] [location]</dl>
<h2>DESCRIPTION</h2>
<dd>The regtree utility prints out all the contents of a Windows registry file. Subkeys are printed with one level more indentation than their parents.</p>
<h2>OPTIONS</h2>
<p> &#8211;help</p>
<dl>
<dt>
<dd> Show list of available options.</dl>
<p> &#8211;backend BACKEND</p>
<dl>
<dt>
<dd> Name of backend to load. Possible values are: creg, regf, dir and rpc. The default is <i>dir</i>.</dl>
<p> &#8211;credentials=CREDENTIALS</p>
<dl>
<dt>
<dd> Credentials to use, if any. Password should be separated from user name by a percent sign.</dl>
<p> &#8211;fullpath</p>
<dl>
<dt>
<dd> Print the full path to each key instead of only its name.</dl>
<p> &#8211;no-values</p>
<dl>
<dt>
<dd> Don&#8217;t print values, just keys.</dl>
<h2>VERSION</h2>
<p> This man page is correct for version 4.0 of the Samba suite.</p>
<h2>SEE ALSO</h2>
<p> gregedit, regshell, regdiff, regpatch, samba</p>
<h2>AUTHOR</h2>
<p> This utility is part of the m[blue]<code>Samba</code>m[]<font SIZE="-2">[1]</font> suite, which is developed by the global m[blue]<code>Samba Team</code>m[]<font SIZE="-2">[2]</font>. </p>
<p> This manpage and regtree were written by Jelmer Vernooij.</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Samba</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.samba.org/">http://www.samba.org/</a></dl>
<dt> 2.</p>
<dd> Samba Team</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.samba.org/samba/team/">http://www.samba.org/samba/team/</a></dl>
</dl>
<h2>Index</h2>
