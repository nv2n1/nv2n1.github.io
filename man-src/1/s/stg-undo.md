---
title: "stg-undo(1)"
name: "stg-undo"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-undo/"
description: "stg-undo – Undo the last operation"
---

<h2 class="name">NAME</h2>
<p> stg-undo &#8211; Undo the last operation </p>
<h2>SYNOPSIS</h2>
<pre>
<i>stg</i> undo
</pre>
<h2>DESCRIPTION</h2>
<p> Reset the patch stack to the previous state. Consecutive invocations of &quot;stg undo&quot; will take you ever further into the past.</p>
<h2>OPTIONS</h2>
<p> -n N, &#8211;number N</p>
<dl>
<dt>
<dd> Undo the last N commands.</dl>
<p> &#8211;hard</p>
<dl>
<dt>
<dd> Discard changes in your index/worktree.</dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
<h2>Index</h2>
