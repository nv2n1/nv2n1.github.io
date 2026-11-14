---
title: "stg-goto(1)"
name: "stg-goto"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-goto/"
description: "stg-goto – Push or pop patches to the given one"
---

<h2 class="name">NAME</h2>
<p> stg-goto &#8211; Push or pop patches to the given one </p>
<h2>SYNOPSIS</h2>
<pre><code>
stg goto[options][--]&lt;patch - name&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> Push/pop patches to/from the stack until the one given on the command line becomes current.</p>
<h2>OPTIONS</h2>
<p> -k, &#8211;keep</p>
<dl>
<dt>
<dd> Keep the local changes.</dl>
<p> -m, &#8211;merged</p>
<dl>
<dt>
<dd> Check for patches merged upstream.</dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
<h2>Index</h2>
