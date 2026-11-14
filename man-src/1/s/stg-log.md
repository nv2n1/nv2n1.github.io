---
title: "stg-log(1)"
name: "stg-log"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-log/"
description: "stg-log – Display the patch changelog"
---

<h2 class="name">NAME</h2>
<p> stg-log &#8211; Display the patch changelog </p>
<h2>SYNOPSIS</h2>
<pre><code>
stg log[options][--][&lt;patches&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> List the history of the patch stack: the stack log. If one or more patch names are given, limit the list to the log entries that touch the named patches. </p>
<p> &quot;stg undo&quot; and &quot;stg redo&quot; let you step back and forth in the patch stack. &quot;stg reset&quot; lets you go directly to any state.</p>
<h2>OPTIONS</h2>
<p> -b BRANCH, &#8211;branch BRANCH</p>
<dl>
<dt>
<dd> Use BRANCH instead of the default one.</dl>
<p> -d, &#8211;diff</p>
<dl>
<dt>
<dd> Show the refresh diffs.</dl>
<p> -n NUMBER, &#8211;number NUMBER</p>
<dl>
<dt>
<dd> Limit the output to NUMBER commits.</dl>
<p> -f, &#8211;full</p>
<dl>
<dt>
<dd> Show the full commit ids.</dl>
<p> -g, &#8211;graphical</p>
<dl>
<dt>
<dd> Run gitk instead of printing.</dl>
<p> &#8211;clear</p>
<dl>
<dt>
<dd> Clear the log history.</dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
<h2>Index</h2>
