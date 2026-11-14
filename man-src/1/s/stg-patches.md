---
title: "stg-patches(1)"
name: "stg-patches"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-patches/"
description: "stg-patches – Show the applied patches modifying a file"
---

<h2 class="name">NAME</h2>
<p> stg-patches &#8211; Show the applied patches modifying a file </p>
<h2>SYNOPSIS</h2>
<pre><code>
stg patches[options][--][ &lt; files or dirs &gt; ]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Show the applied patches modifying the given files. Without arguments, it shows the patches affected by the local tree modifications. The <i>&#8211;diff</i> option also lists the patch log and the diff for the given files.</p>
<h2>OPTIONS</h2>
<p> -d, &#8211;diff</p>
<dl>
<dt>
<dd> Show the diff for the given files.</dl>
<p> -b BRANCH, &#8211;branch BRANCH</p>
<dl>
<dt>
<dd> Use BRANCH instead of the default branch.</dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
<h2>Index</h2>
