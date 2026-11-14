---
title: "git-write-tree(1)"
name: "git-write-tree"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-write-tree/"
description: "git-write-tree – Create a tree object from the current index"
---

<h2 class="name">NAME</h2>
<p> git-write-tree &#8211; Create a tree object from the current index </p>
<h2>SYNOPSIS</h2>
<pre><code>
git write - tree[--missing - ok][--prefix = &lt;prefix&gt; / ]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Creates a tree object using the current index. The name of the new tree object is printed to standard output. </p>
<p> The index must be in a fully merged state. </p>
<p> Conceptually, <i>git write-tree</i> sync()s the current index contents into a set of tree files. In order to have that match what is actually in your directory right now, you need to have done a <i>git update-index</i> phase before you did the <i>git write-tree</i>.</p>
<h2>OPTIONS</h2>
<p> &#8211;missing-ok</p>
<dl>
<dt>
<dd> Normally <i>git write-tree</i> ensures that the objects referenced by the directory exist in the object database. This option disables this check.</dl>
<p> &#8211;prefix=&lt;prefix&gt;/</p>
<dl>
<dt>
<dd> Writes a tree object that represents a subdirectory <code>&lt;prefix&gt;</code>. This can be used to write the tree object for a subproject that is in the named subdirectory.</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
