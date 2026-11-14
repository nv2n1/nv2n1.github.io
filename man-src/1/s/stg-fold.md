---
title: "stg-fold(1)"
name: "stg-fold"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-fold/"
description: "stg-fold – Integrate a GNU diff patch into the current patch"
---

<h2 class="name">NAME</h2>
<p> stg-fold &#8211; Integrate a GNU diff patch into the current patch </p>
<h2>SYNOPSIS</h2>
<pre><code>
stg fold[options][--][&lt;file&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Apply the given GNU diff file (or the standard input) onto the top of the current patch. With the <i>&#8211;threeway</i> option, the patch is applied onto the bottom of the current patch and a three-way merge is performed with the current top. With the &#8211;base option, the patch is applied onto the specified base and a three-way merged is performed with the current top.</p>
<h2>OPTIONS</h2>
<p> -t, &#8211;threeway</p>
<dl>
<dt>
<dd> Perform a three-way merge with the current patch.</dl>
<p> -b BASE, &#8211;base BASE</p>
<dl>
<dt>
<dd> Use BASE instead of HEAD when applying the patch.</dl>
<p> -p N, &#8211;strip N</p>
<dl>
<dt>
<dd> Remove N leading slashes from diff paths (default 1).</dl>
<p> &#8211;reject</p>
<dl>
<dt>
<dd> Leave the rejected hunks in corresponding *.rej files.</dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
<h2>Index</h2>
