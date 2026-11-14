---
title: "stg-sink(1)"
name: "stg-sink"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-sink/"
description: "stg-sink – Send patches deeper down the stack"
---

<h2 class="name">NAME</h2>
<p> stg-sink &#8211; Send patches deeper down the stack </p>
<h2>SYNOPSIS</h2>
<pre><code>
stg sink[-t&lt;target patch&gt;][-n][--][&lt;patches&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> This is the opposite operation of <code><a href="/docs/linux/man/1-stg-float/">stg-float</a></code>(1): move the specified patches down the stack. It is for example useful to group stable patches near the bottom of the stack, where they are less likely to be impacted by the push of another patch, and from where they can be more easily committed or pushed. </p>
<p> If no patch is specified on command-line, the current patch gets sunk. By default patches are sunk to the bottom of the stack, but the <i>&#8211;to</i> option allows one to place them under any applied patch. </p>
<p> Sinking internally involves popping all patches (or all patches including &lt;target patch&gt;), then pushing the patches to sink, and then (unless <i>&#8211;nopush</i> is also given) pushing back into place the formerly-applied patches.</p>
<h2>OPTIONS</h2>
<p> -n, &#8211;nopush</p>
<dl>
<dt>
<dd> Do not push back on the stack the formerly-applied patches. Only the patches to sink are pushed.</dl>
<p> -t TARGET, &#8211;to TARGET</p>
<dl>
<dt>
<dd> Specify a target patch to place the patches below, instead of sinking them to the bottom of the stack.</dl>
<p> -k, &#8211;keep</p>
<dl>
<dt>
<dd> Keep the local changes.</dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
<h2>Index</h2>
