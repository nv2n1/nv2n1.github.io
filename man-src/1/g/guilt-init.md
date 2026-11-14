---
title: "guilt-init(1)"
name: "guilt-init"
section: "1"
letter: "g"
url: "/docs/linux/man/1-guilt-init/"
description: "guilt-init – Initialize guilt for use in a git repository"
---

<h2 class="name">NAME</h2>
<p> guilt-init &#8211; Initialize guilt for use in a git repository </p>
<h2>SYNOPSIS</h2>
<p> <i>guilt-init</i></p>
<h2>DESCRIPTION</h2>
<p> Initialize a git repository for use with guilt</p>
<h2>EXAMPLES</h2>
<p> First, get a repository to work on. Herecqs one that wecqll use as an example: </p>
<dl>
<dt>
<dd>
<pre>
$ git-clone <a href="git://git.kernel.org/pub/scm/linux/kernel/jsipek/guilt-hello.git">git://git.kernel.org/pub/scm/linux/kernel/jsipek/guilt-hello.git</a>
</pre>
</dl>
<p> Now, it initialize the patches directory using guiltcqs init command: </p>
<dl>
<dt>
<dd>
<pre>
$ cd hello
$ guilt-init
</pre>
</dl>
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
