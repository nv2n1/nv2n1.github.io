---
title: "stg-redo(1)"
name: "stg-redo"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-redo/"
description: "stg-redo – Undo the last undo operation"
---

<h2 class="name">NAME</h2>
<p> stg-redo &#8211; Undo the last undo operation </p>
<h2>SYNOPSIS</h2>
<pre>
<i>stg</i> redo
</pre>
<h2>DESCRIPTION</h2>
<p> If the last command was an undo, reset the patch stack to the state it had before the undo. Consecutive invocations of &quot;stg redo&quot; will undo the effects of consecutive invocations of &quot;stg undo&quot;. </p>
<p> It is an error to run &quot;stg redo&quot; if the last command was not an undo.</p>
<h2>OPTIONS</h2>
<p> -n N, &#8211;number N</p>
<dl>
<dt>
<dd> Undo the last N undos.</dl>
<p> &#8211;hard</p>
<dl>
<dt>
<dd> Discard changes in your index/worktree.</dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
<h2>Index</h2>
