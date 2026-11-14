---
title: "regshell(1)"
name: "regshell"
section: "1"
letter: "r"
url: "/docs/linux/man/1-regshell/"
description: "regshell – Windows registry file browser using readline"
---

<h2 class="name">NAME</h2>
<p> regshell &#8211; Windows registry file browser using readline </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>regshell</code> [&#8211;help] [&#8211;backend=BACKEND] [&#8211;credentials=CREDENTIALS] [location]</dl>
<h2>DESCRIPTION</h2>
<dd>regshell is a utility that lets you browse thru a Windows registry file as if you were using a regular unix shell to browse thru a file system.</p>
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
<h2>COMMANDS</h2>
<p> ck|cd &lt;keyname&gt;</p>
<dl>
<dt>
<dd> Go to the specified subkey.</dl>
<p> ch|predef [predefined-key-name]</p>
<dl>
<dt>
<dd> Go to the specified predefined key.</dl>
<p> list|ls</p>
<dl>
<dt>
<dd> List subkeys and values of the current key.</dl>
<p> mkkey|mkdir &lt;keyname&gt;</p>
<dl>
<dt>
<dd> Create a key with the specified <i>keyname</i> as a subkey of the current key.</dl>
<p> rmval|rm &lt;valname&gt;</p>
<dl>
<dt>
<dd> Delete the specified value.</dl>
<p> rmkey|rmdir &lt;keyname&gt;</p>
<dl>
<dt>
<dd> Delete the specified subkey recursively.</dl>
<p> pwd|pwk</p>
<dl>
<dt>
<dd> Print the full name of the current key.</dl>
<p> set|update</p>
<dl>
<dt>
<dd> Update the value of a key value. Not implemented at the moment.</dl>
<p> help|?</p>
<dl>
<dt>
<dd> Print a list of available commands.</dl>
<p> exit|quit</p>
<dl>
<dt>
<dd> Leave regshell.</dl>
<h2>EXAMPLES</h2>
<p> Browsing thru a nt4 registry file </p>
<dl>
<dt>
<dd>
<pre>
<code>regshell -b nt4 NTUSER.DAT</code>
$$$PROTO.HIV&gt; <code>ls</code>
K AppEvents
K Console
K Control Panel
K Environment
K Identities
K Keyboard Layout
K Network
K Printers
K Software
K UNICODE Program Groups
K Windows 3.1 Migration Status
$$$PROTO.HIV&gt; <code>exit</code>
</pre>
</dl>
<p> Listing the subkeys of HKEY_CURRENT_USER\AppEvents on a remote computer: </p>
<dl>
<dt>
<dd>
<pre>
<code>regshell --remote=ncacn_np:aurelia -c &quot;jelmer%secret&quot;</code>
HKEY_CURRENT_MACHINE&gt; <code>predef HKEY_CURRENT_USER</code>
HKEY_CURRENT_USER&gt; <code>cd AppEvents</code>
Current path is: HKEY_CURRENT_USER\AppEvents
HKEY_CURRENT_USER\AppEvents&gt; <code>ls</code>
K EventLabels
K Schemes
HKEY_CURRENT_USER\AppEvents&gt; <code>exit</code>
</pre>
</dl>
<h2>VERSION</h2>
<p> This man page is correct for version 4.0 of the Samba suite.</p>
<h2>SEE ALSO</h2>
<p> regtree, regdiff, regpatch, gregedit, samba</p>
<h2>AUTHOR</h2>
<p> This utility is part of the m[blue]<code>Samba</code>m[]<font SIZE="-2">[1]</font> suite, which is developed by the global m[blue]<code>Samba Team</code>m[]<font SIZE="-2">[2]</font>. </p>
<p> This manpage and regshell were written by Jelmer Vernooij.</p>
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
