---
title: "git-verify-tag(1)"
name: "git-verify-tag"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-verify-tag/"
description: "git-verify-tag – Check the GPG signature of tags"
---

<h2 class="name">NAME</h2>
<p> git-verify-tag &#8211; Check the GPG signature of tags </p>
<h2>SYNOPSIS</h2>
<pre>
<i>git verify-tag</i> [--format=&lt;format&gt;] &lt;tag&gt;...
</pre>
<h2>DESCRIPTION</h2>
<p> Validates the gpg signature created by <i>git tag</i>.</p>
<h2>OPTIONS</h2>
<p> &#8211;raw</p>
<dl>
<dt>
<dd> Print the raw gpg status output to standard error instead of the normal human-readable output.</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Print the contents of the tag object before validating it.</dl>
<p> &lt;tag&gt;&#8230;</p>
<dl>
<dt>
<dd> SHA-1 identifiers of Git tag objects.</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
