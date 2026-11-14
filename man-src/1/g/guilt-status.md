---
title: "guilt-status(1)"
name: "guilt-status"
section: "1"
letter: "g"
url: "/docs/linux/man/1-guilt-status/"
description: "guilt-status – Print the status of files since the last refresh"
---

<h2 class="name">NAME</h2>
<p> guilt-status &#8211; Print the status of files since the last refresh </p>
<h2>SYNOPSIS</h2>
<p> <i>guilt-status</i> [-a|-A] [-c|-C] [-d|-D] [-m|-M] [-r|-R] [-t|-T] [-u|-U] [-x|-X] [-n]</p>
<h2>DESCRIPTION</h2>
<p> Each file is printed with a prefix that describes itcqs status. </p>
<dl>
<dt>
<dd>
<pre>
A   added
C   copied
D   deleted
M   modified
R   renamed
T   type change (e.g., mode)
U   unmerged
?   untracked
</pre>
</dl>
<h2>OPTIONS</h2>
<p> -n</p>
<dl>
<dt>
<dd> Hide status prefix in the output</dl>
<p> -a, -A</p>
<dl>
<dt>
<dd> Display only added files</dl>
<p> -c, -C</p>
<dl>
<dt>
<dd> Display only copied files</dl>
<p> -d, -D</p>
<dl>
<dt>
<dd> Display only deleted files</dl>
<p> -m, -M</p>
<dl>
<dt>
<dd> Display only modified files</dl>
<p> -r, -R</p>
<dl>
<dt>
<dd> Display only renamed files</dl>
<p> -t, -T</p>
<dl>
<dt>
<dd> Display only files with a status change (e.g., mode)</dl>
<p> -u, -U</p>
<dl>
<dt>
<dd> Display only unmerged files</dl>
<p> -x, -X</p>
<dl>
<dt>
<dd> Display only unknown files</dl>
<h2>AUTHOR</h2>
<p> Written by Josef &quot;Jeff&quot; Sipek &lt;m[blue]<code>jeffpc [at] josefsipek.net</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>DOCUMENTATION</h2>
<p> Documentation by Brandon Philips &lt;m[blue]<code>brandon [at] ifup.org</code>m[]<font SIZE="-2">[2]</font>&gt;</p>
<h2>GUILT</h2>
<p> Part of the linkguilt:guilt[7] suite (Generated for Guilt v0.33)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> jeffpc [at] josefsipek.net</p>
<dl>
<dt>
<dd> mailto:jeffpc [at] josefsipek.net</dl>
<dt> 2.</p>
<dd> brandon [at] ifup.org</p>
<dl>
<dt>
<dd> mailto:brandon [at] ifup.org</dl>
</dl>
<h2>Index</h2>
