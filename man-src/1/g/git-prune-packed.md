---
title: "git-prune-packed(1)"
name: "git-prune-packed"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-prune-packed/"
description: "git-prune-packed – Remove extra objects that are already in pack files"
---

<h2 class="name">NAME</h2>
<p> git-prune-packed &#8211; Remove extra objects that are already in pack files </p>
<h2>SYNOPSIS</h2>
<pre><code>
git prune - packed[-n | --dry - run][-q | --quiet]
</code></pre>
<h2>DESCRIPTION</h2>
<p> This program searches the <code>$GIT_OBJECT_DIRECTORY</code> for all objects that currently exist in a pack file as well as the independent object directories. </p>
<p> All such extra objects are removed. </p>
<p> A pack is a collection of objects, individually compressed, with delta compression applied, stored in a single file, with an associated index file. </p>
<p> Packs are used to reduce the load on mirror systems, backup engines, disk storage, etc.</p>
<h2>OPTIONS</h2>
<p> -n, &#8211;dry-run</p>
<dl>
<dt>
<dd> Don&#8217;t actually remove any objects, only show those that would have been removed.</dl>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> Squelch the progress indicator.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-pack-objects/">git-pack-objects</a></code>(1) <code><a href="/docs/linux/man/1-git-repack/">git-repack</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
