---
title: "stg-diff(1)"
name: "stg-diff"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-diff/"
description: "stg-diff – Show the tree diff"
---

<h2 class="name">NAME</h2>
<p> stg-diff &#8211; Show the tree diff </p>
<h2>SYNOPSIS</h2>
<pre><code>
stg diff[options][--][ &lt; files or dirs &gt; ]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Show the diff (default) or diffstat between the current working copy or a tree-ish object and another tree-ish object (defaulting to HEAD). File names can also be given to restrict the diff output. The tree-ish object has the format accepted by the <code><a href="/docs/linux/man/1-stg-id/">stg-id</a></code>(1) command.</p>
<h2>OPTIONS</h2>
<p> -r rev1[..[rev2]], &#8211;range rev1[..[rev2]]</p>
<dl>
<dt>
<dd> Show the diff between revisions.</dl>
<p> -s, &#8211;stat</p>
<dl>
<dt>
<dd> Show the stat instead of the diff.</dl>
<p> -O OPTIONS, &#8211;diff-opts OPTIONS</p>
<dl>
<dt>
<dd> Extra options to pass to &quot;git diff&quot;.</dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
<h2>Index</h2>
