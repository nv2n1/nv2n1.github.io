---
title: "guilt-init(1)"
name: "guilt-init"
section: "1"
letter: "g"
url: "/docs/linux/man/1-guilt-init/"
description: "guilt-init – Initialize guilt for use in a git repository"
---

<h2>SYNOPSIS</h2>
<p> <i>guilt-init</i></p>
<h2>DESCRIPTION</h2>
<p> Initialize a git repository for use with guilt</p>
<h2>EXAMPLES</h2>
<p> First, get a repository to work on. Herecqs one that wecqll use as an example: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ git-clone <a href="git://git.kernel.org/pub/scm/linux/kernel/jsipek/guilt-hello.git">git://git.kernel.org/pub/scm/linux/kernel/jsipek/guilt-hello.git</a>
</pre>
</dd></dl>
<p> Now, it initialize the patches directory using guiltcqs init command: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ cd hello
$ guilt-init
</pre>
</dd></dl>
<h2>AUTHOR</h2>
<p> Written by Josef &quot;Jeff&quot; Sipek &lt;m[blue]<code>jeffpc [at] josefsipek.net</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>DOCUMENTATION</h2>
<p> Documentation by Brandon Philips &lt;m[blue]<code>brandon [at] ifup.org</code>m[]<font SIZE="-2">[2]</font>&gt;</p>
<h2>GUILT</h2>
<p> Part of the linkguilt:guilt[7] suite (Generated for Guilt v0.33)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> jeffpc [at] josefsipek.net</dd>
<dl>
<dt>
</dt><dd> mailto:jeffpc [at] josefsipek.net</dd></dl>
<dt> 2.</dt>
<dd> brandon [at] ifup.org</dd>
<dl>
<dt>
</dt><dd> mailto:brandon [at] ifup.org</dd></dl>
</dl>
