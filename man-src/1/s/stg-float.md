---
title: "stg-float(1)"
name: "stg-float"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-float/"
description: "stg-float – Push patches to the top, even if applied"
---

<h2 class="name">NAME</h2>
<p> stg-float &#8211; Push patches to the top, even if applied </p>
<h2>SYNOPSIS</h2>
<pre><code>
stg float[--]&lt;patches&gt;
        stg float - s&lt;series&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> Push a patch or a range of patches to the top even if applied. The necessary pop and push operations will be performed to accomplish this. The <i>&#8211;series</i> option can be used to rearrange the (top) patches as specified by the given series file (or the standard input).</p>
<h2>OPTIONS</h2>
<p> -s FILE, &#8211;series FILE</p>
<dl>
<dt>
<dd> Rearrange according to the series FILE.</dl>
<p> -k, &#8211;keep</p>
<dl>
<dt>
<dd> Keep the local changes.</dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
<h2>Index</h2>
