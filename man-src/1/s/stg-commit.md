---
title: "stg-commit(1)"
name: "stg-commit"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-commit/"
description: "stg-commit – Permanently store the applied patches into the stack base"
---

<h2 class="name">NAME</h2>
<p> stg-commit &#8211; Permanently store the applied patches into the stack base </p>
<h2>SYNOPSIS</h2>
<pre><code>
stg commit
        stg commit[--]&lt;patchnames&gt;
            stg commit - n NUM
                             stg commit-- all
</code></pre>
<h2>DESCRIPTION</h2>
<p> Merge one or more patches into the base of the current stack and remove them from the series while advancing the base. This is the opposite of <i>stg uncommit</i>. Use this command if you no longer want to manage a patch with StGIT. </p>
<p> By default, the bottommost patch is committed. If patch names are given, the stack is rearranged so that those patches are at the bottom, and then they are committed. </p>
<p> The -n/&#8211;number option specifies the number of applied patches to commit (counting from the bottom of the stack). If -a/&#8211;all is given, all applied patches are committed.</p>
<h2>OPTIONS</h2>
<p> -n NUMBER, &#8211;number NUMBER</p>
<dl>
<dt>
<dd> Commit the specified number of patches.</dl>
<p> -a, &#8211;all</p>
<dl>
<dt>
<dd> Commit all applied patches.</dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
<h2>Index</h2>
