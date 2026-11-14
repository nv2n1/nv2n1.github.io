---
title: "git-pack-redundant(1)"
name: "git-pack-redundant"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-pack-redundant/"
description: "git-pack-redundant – Find redundant pack files"
---

<h2 class="name">NAME</h2>
<p> git-pack-redundant &#8211; Find redundant pack files </p>
<h2>SYNOPSIS</h2>
<pre><code>
git pack - redundant[--verbose][--alt - odb]&lt;--all |.pack filename...&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> This program computes which packs in your repository are redundant. The output is suitable for piping to <code>xargs rm</code> if you are in the root of the repository. </p>
<p> <i>git pack-redundant</i> accepts a list of objects on standard input. Any objects given will be ignored when checking which packs are required. This makes the following command useful when wanting to remove packs which contain unreachable objects. </p>
<p> git fsck &#8211;full &#8211;unreachable | cut -d &#8216; &#8216; -f3 | \ git pack-redundant &#8211;all | xargs rm</p>
<h2>OPTIONS</h2>
<p> &#8211;all</p>
<dl>
<dt>
<dd> Processes all packs. Any filenames on the command line are ignored.</dl>
<p> &#8211;alt-odb</p>
<dl>
<dt>
<dd> Don&#8217;t require objects present in packs from alternate object directories to be present in local packs.</dl>
<p> &#8211;verbose</p>
<dl>
<dt>
<dd> Outputs some statistics to stderr. Has a small performance penalty.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-pack-objects/">git-pack-objects</a></code>(1) <code><a href="/docs/linux/man/1-git-repack/">git-repack</a></code>(1) <code><a href="/docs/linux/man/1-git-prune-packed/">git-prune-packed</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
