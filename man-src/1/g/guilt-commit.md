---

title: "guilt-commit(1)"
name: "guilt-commit"
section: "1"
letter: "g"
url: "/docs/linux/man/1-guilt-commit/"
description: "guilt-commit – Commit specified number of patches"
---

<p> guilt-commit &#8211; Commit specified number of patches </p>
<h2>SYNOPSIS</h2>
<p> <i>guilt-commit</i> -n &lt;num&gt; | -a | &#8211;all </p>
<p> Turn specified number of bottom most patches into Git commits. This removes the the patches from the series, and status file.</p>
<h2>OPTIONS</h2>
<p> &#8211;all, -a</p>
<dl>
<dt>
</dt><dd> Commit all applied patches</dd></dl>
<p> -n &lt;num&gt;</p>
<dl>
<dt>
</dt><dd> Commit &lt;num&gt; bottom most patches</dd></dl>
<h2>AUTHOR</h2>
<p> Written by Josef &quot;Jeff&quot; Sipek &lt;m[blue]<code>jeffpc [at] josefsipek.net</code>m[][1]&gt;</p>
<h2>DOCUMENTATION</h2>
<p> Documentation by Josef &quot;Jeff&quot; Sipek &lt;m[blue]<code>jeffpc [at] josefsipek.net</code>m[][1]&gt;</p>
<h2>GUILT</h2>
<p> Part of the linkguilt:guilt[7] suite (Generated for Guilt v0.33)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> jeffpc [at] josefsipek.net</dd>
<dl>
<dt>
</dt><dd> mailto:jeffpc [at] josefsipek.net</dd></dl>
</dl>
