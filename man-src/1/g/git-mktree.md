---
title: "git-mktree(1)"
name: "git-mktree"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-mktree/"
description: "git-mktree – Build a tree-object from ls-tree formatted text"
---

<h2 class="name">NAME</h2>
<p> git-mktree &#8211; Build a tree-object from ls-tree formatted text </p>
<h2>SYNOPSIS</h2>
<pre><code>
git mktree[-z][--missing][--batch]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Reads standard input in non-recursive <code>ls-tree</code> output format, and creates a tree object. The order of the tree entries is normalized by mktree so pre-sorting the input is not required. The object name of the tree object built is written to the standard output.</p>
<h2>OPTIONS</h2>
<p> -z</p>
<dl>
<dt>
<dd> Read the NUL-terminated <code>ls-tree -z</code> output instead.</dl>
<p> &#8211;missing</p>
<dl>
<dt>
<dd> Allow missing objects. The default behaviour (without this option) is to verify that each tree entry&#8217;s sha1 identifies an existing object. This option has no effect on the treatment of gitlink entries (aka &quot;submodules&quot;) which are always allowed to be missing.</dl>
<p> &#8211;batch</p>
<dl>
<dt>
<dd> Allow building of more than one tree object before exiting. Each tree is separated by as single blank line. The final new-line is optional. Note &#8211; if the <code>-z</code> option is used, lines are terminated with NUL.</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
