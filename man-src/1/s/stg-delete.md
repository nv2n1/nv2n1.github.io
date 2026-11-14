---
title: "stg-delete(1)"
name: "stg-delete"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-delete/"
description: "stg-delete – Delete patches"
---

<h2 class="name">NAME</h2>
<p> stg-delete &#8211; Delete patches </p>
<h2>SYNOPSIS</h2>
<pre><code>
stg delete[options][--]&lt;patch1&gt;[&lt;patch2&gt;][&lt;patch3&gt;..&lt;patch4&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Delete the patches passed as arguments.</p>
<h2>OPTIONS</h2>
<p> &#8211;spill</p>
<dl>
<dt>
<dd> Delete the patches, but do not touch the index and worktree. This only works with applied patches at the top of the stack. The effect is to &quot;spill&quot; the patch contents into the index and worktree. This can be useful e.g. if you want to split a patch into several smaller pieces.</dl>
<p> -b BRANCH, &#8211;branch BRANCH</p>
<dl>
<dt>
<dd> Use BRANCH instead of the default branch.</dl>
<p> -t, &#8211;top</p>
<dl>
<dt>
<dd> Delete top patch.</dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
<h2>Index</h2>
