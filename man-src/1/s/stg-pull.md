---
title: "stg-pull(1)"
name: "stg-pull"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-pull/"
description: "stg-pull – Pull changes from a remote repository"
---

<h2 class="name">NAME</h2>
<p> stg-pull &#8211; Pull changes from a remote repository </p>
<h2>SYNOPSIS</h2>
<pre><code>
stg pull[options][--][&lt;repository&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Pull the latest changes from the given remote repository (defaulting to branch.&lt;name&gt;.remote, or <i>origin</i> if not set). This command works by popping all the patches from the stack, pulling the changes in the parent repository, setting the base of the stack to the latest parent HEAD and pushing the patches back (unless <i>&#8211;nopush</i> is specified). The <i>push</i> operation can fail if there are conflicts. They need to be resolved and the patch pushed again. </p>
<p> Check the <i>git fetch</i> documentation for the &lt;repository&gt; format.</p>
<h2>OPTIONS</h2>
<p> -n, &#8211;nopush</p>
<dl>
<dt>
<dd> Do not push the patches back after pulling.</dl>
<p> -m, &#8211;merged</p>
<dl>
<dt>
<dd> Check for patches merged upstream.</dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
<h2>Index</h2>
