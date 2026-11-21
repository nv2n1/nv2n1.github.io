---
title: "stg-log(1)"
name: "stg-log"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-log/"
description: "stg-log – Display the patch changelog"
---

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
</dt><dd> Use BRANCH instead of the default one.</dd></dl>
<p> -d, &#8211;diff</p>
<dl>
<dt>
</dt><dd> Show the refresh diffs.</dd></dl>
<p> -n NUMBER, &#8211;number NUMBER</p>
<dl>
<dt>
</dt><dd> Limit the output to NUMBER commits.</dd></dl>
<p> -f, &#8211;full</p>
<dl>
<dt>
</dt><dd> Show the full commit ids.</dd></dl>
<p> -g, &#8211;graphical</p>
<dl>
<dt>
</dt><dd> Run gitk instead of printing.</dd></dl>
<p> &#8211;clear</p>
<dl>
<dt>
</dt><dd> Clear the log history.</dd></dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
