---
title: "stg-rebase(1)"
name: "stg-rebase"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-rebase/"
description: "stg-rebase – Move the stack base to another point in history"
---

<h2 class="name">NAME</h2>
<p> stg-rebase &#8211; Move the stack base to another point in history </p>
<h2>SYNOPSIS</h2>
<pre><code>
stg rebase[options][--]&lt;new - base - id&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> Pop all patches from current stack, move the stack base to the given &lt;new-base-id&gt; and push the patches back. </p>
<p> If you experience merge conflicts, resolve the problem and continue the rebase by executing the following sequence: </p>
<dl>
<dt>
<dd>
<pre>
$ git add --update
$ stg refresh
$ stg goto top-patch
</pre>
</dl>
<p> Or if you want to skip that patch: </p>
<dl>
<dt>
<dd>
<pre>
$ stg undo --hard
$ stg push next-patch..top-patch
</pre>
</dl>
<h2>OPTIONS</h2>
<p> -n, &#8211;nopush</p>
<dl>
<dt>
<dd> Do not push the patches back after rebasing.</dl>
<p> -m, &#8211;merged</p>
<dl>
<dt>
<dd> Check for patches merged upstream.</dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
<h2>Index</h2>
