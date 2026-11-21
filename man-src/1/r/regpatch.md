---

title: "regpatch(1)"
name: "regpatch"
section: "1"
letter: "r"
url: "/docs/linux/man/1-regpatch/"
description: "regpatch – Applies registry patches to registry files"
---

<dl>
<dt> <code>regpatch</code> [&#8211;help] [&#8211;backend=BACKEND] [&#8211;credentials=CREDENTIALS] [location] [patch-file]</dt></dl>
<dd>The regpatch utility applies registry patches to Windows registry files. The patch files should have the same format as is being used by the regdiff utility and regedit32.exe from Windows. </dd>
<p> If no patch file is specified on the command line, regpatch attempts to read it from standard input.</p>
<h2>OPTIONS</h2>
<p> &#8211;help</p>
<dl>
<dt>
</dt><dd> Show list of available options.</dd></dl>
<p> &#8211;backend BACKEND</p>
<dl>
<dt>
</dt><dd> Name of backend to load. Possible values are: creg, regf, dir and rpc. The default is <i>dir</i>.</dd></dl>
<p> &#8211;credentials=CREDENTIALS</p>
<dl>
<dt>
</dt><dd> Credentials to use, if any. Password should be separated from user name by a percent sign.</dd></dl>
<h2>VERSION</h2>
<p> This man page is correct for version 4.0 of the Samba suite.</p>
<h2>SEE ALSO</h2>
<p> regdiff, regtree, regshell, gregedit, samba, diff, patch</p>
<h2>AUTHOR</h2>
<p> This utility is part of the m[blue]<code>Samba</code>m[]<font SIZE="-2">[1]</font> suite, which is developed by the global m[blue]<code>Samba Team</code>m[]<font SIZE="-2">[2]</font>. </p>
<p> This manpage and regpatch were written by Jelmer Vernooij.</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> Samba</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.samba.org/">http://www.samba.org/</a></dd></dl>
<dt> 2.</dt>
<dd> Samba Team</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.samba.org/samba/team/">http://www.samba.org/samba/team/</a></dd></dl>
</dl>
