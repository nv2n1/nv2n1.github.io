---
title: "git-count-objects(1)"
name: "git-count-objects"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-count-objects/"
description: "git-count-objects – Count unpacked number of objects and their disk consumption"
---

<h2 class="name">NAME</h2>
<p> git-count-objects &#8211; Count unpacked number of objects and their disk consumption </p>
<h2>SYNOPSIS</h2>
<pre><code>
git count - objects[-v][-H | --human - readable]
</code></pre>
<h2>DESCRIPTION</h2>
<p> This counts the number of unpacked object files and disk space consumed by them, to help you decide when it is a good time to repack.</p>
<h2>OPTIONS</h2>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Report in more detail: </p>
<p> count: the number of loose objects </p>
<p> size: disk space consumed by loose objects, in KiB (unless -H is specified) </p>
<p> in-pack: the number of in-pack objects </p>
<p> size-pack: disk space consumed by the packs, in KiB (unless -H is specified) </p>
<p> prune-packable: the number of loose objects that are also present in the packs. These objects could be pruned using <code>git prune-packed</code>. </p>
<p> garbage: the number of files in object database that are neither valid loose objects nor valid packs </p>
<p> size-garbage: disk space consumed by garbage files, in KiB (unless -H is specified) </p>
<p> alternate: absolute path of alternate object databases; may appear multiple times, one line per path. Note that if the path contains non-printable characters, it may be surrounded by double-quotes and contain C-style backslashed escape sequences.</dl>
<p> -H, &#8211;human-readable</p>
<dl>
<dt>
<dd> Print sizes in human readable format</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
