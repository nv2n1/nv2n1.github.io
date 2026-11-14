---
title: "guilt-rebase(1)"
name: "guilt-rebase"
section: "1"
letter: "g"
url: "/docs/linux/man/1-guilt-rebase/"
description: "guilt-rebase – Rebase pushed patches"
---

<h2 class="name">NAME</h2>
<p> guilt-rebase &#8211; Rebase pushed patches </p>
<h2>SYNOPSIS</h2>
<p> <i>guilt-rebase</i> &lt;upstream&gt;</p>
<h2>DESCRIPTION</h2>
<p> Rebase pushed patches against an upstream branch.</p>
<h2>OPTIONS</h2>
<p> &lt;upstream&gt;</p>
<dl>
<dt>
<dd> Branch, tag, or a commit hash identifying upstream repository history.</dl>
<h2>EXAMPLES</h2>
<p> Rebase current tree against Linuscqs 2.6 tree </p>
<dl>
<dt>
<dd>
<pre>
$ git-fetch <a href="git://git.kernel.org/pub/scm/linux/kernel/git/tovalds/linux-2.6.git">git://git.kernel.org/pub/scm/linux/kernel/git/tovalds/linux-2.6.git</a>
$ guilt-rebase FETCH_HEAD
</pre>
</dl>
<h2>AUTHOR</h2>
<p> Written by Josef &quot;Jeff&quot; Sipek &lt;m[blue]<code>jeffpc [at] josefsipek.net</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>DOCUMENTATION</h2>
<p> Documentation by Josef &quot;Jeff&quot; Sipek &lt;m[blue]<code>jeffpc [at] josefsipek.net</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>GUILT</h2>
<p> Part of the linkguilt:guilt[7] suite (Generated for Guilt v0.33)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> jeffpc [at] josefsipek.net</p>
<dl>
<dt>
<dd> mailto:jeffpc [at] josefsipek.net</dl>
</dl>
<h2>Index</h2>
