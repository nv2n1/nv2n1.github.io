---
title: "git-pack-refs(1)"
name: "git-pack-refs"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-pack-refs/"
description: "git-pack-refs – Pack heads and tags for efficient repository access"
---

<h2 class="name">NAME</h2>
<p> git-pack-refs &#8211; Pack heads and tags for efficient repository access </p>
<h2>SYNOPSIS</h2>
<pre><code>
git pack - refs[--all][--no - prune]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Traditionally, tips of branches and tags (collectively known as <i>refs</i>) were stored one file per ref in a (sub)directory under <code>$GIT_DIR/refs</code> directory. While many branch tips tend to be updated often, most tags and some branch tips are never updated. When a repository has hundreds or thousands of tags, this one-file-per-ref format both wastes storage and hurts performance. </p>
<p> This command is used to solve the storage and performance problem by storing the refs in a single file, <code>$GIT_DIR/packed-refs</code>. When a ref is missing from the traditional <code>$GIT_DIR/refs</code> directory hierarchy, it is looked up in this file and used if found. </p>
<p> Subsequent updates to branches always create new files under <code>$GIT_DIR/refs</code> directory hierarchy. </p>
<p> A recommended practice to deal with a repository with too many refs is to pack its refs with <code>&#8211;all</code> once, and occasionally run <code>git pack-refs</code>. Tags are by definition stationary and are not expected to change. Branch heads will be packed with the initial <code>pack-refs &#8211;all</code>, but only the currently active branch heads will become unpacked, and the next <code>pack-refs</code> (without <code>&#8211;all</code>) will leave them unpacked.</p>
<h2>OPTIONS</h2>
<p> &#8211;all</p>
<dl>
<dt>
<dd> The command by default packs all tags and refs that are already packed, and leaves other refs alone. This is because branches are expected to be actively developed and packing their tips does not help performance. This option causes branch tips to be packed as well. Useful for a repository with many branches of historical interests.</dl>
<p> &#8211;no-prune</p>
<dl>
<dt>
<dd> The command usually removes loose refs under <code>$GIT_DIR/refs</code> hierarchy after packing them. This option tells it not to.</dl>
<h2>BUGS</h2>
<p> Older documentation written before the packed-refs mechanism was introduced may still say things like &quot;.git/refs/heads/&lt;branch&gt; file exists&quot; when it means &quot;branch &lt;branch&gt; exists&quot;.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
