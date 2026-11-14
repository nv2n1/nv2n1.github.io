---
title: "git-verify-commit(1)"
name: "git-verify-commit"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-verify-commit/"
description: "git-verify-commit – Check the GPG signature of commits"
---

<h2 class="name">NAME</h2>
<p> git-verify-commit &#8211; Check the GPG signature of commits </p>
<h2>SYNOPSIS</h2>
<pre>
<i>git verify-commit</i> &lt;commit&gt;...
</pre>
<h2>DESCRIPTION</h2>
<p> Validates the GPG signature created by <i>git commit -S</i>.</p>
<h2>OPTIONS</h2>
<p> &#8211;raw</p>
<dl>
<dt>
<dd> Print the raw gpg status output to standard error instead of the normal human-readable output.</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Print the contents of the commit object before validating it.</dl>
<p> &lt;commit&gt;&#8230;</p>
<dl>
<dt>
<dd> SHA-1 identifiers of Git commit objects.</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
