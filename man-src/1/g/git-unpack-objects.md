---
title: "git-unpack-objects(1)"
name: "git-unpack-objects"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-unpack-objects/"
description: "git-unpack-objects – Unpack objects from a packed archive"
---

<h2 class="name">NAME</h2>
<p> git-unpack-objects &#8211; Unpack objects from a packed archive </p>
<h2>SYNOPSIS</h2>
<pre><code>
git unpack - objects[-n][-q][-r][--strict]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Read a packed archive (.pack) from the standard input, expanding the objects contained within and writing them into the repository in &quot;loose&quot; (one object per file) format. </p>
<p> Objects that already exist in the repository will <code>not</code> be unpacked from the packfile. Therefore, nothing will be unpacked if you use this command on a packfile that exists within the target repository. </p>
<p> See <code><a href="/docs/linux/man/1-git-repack/">git-repack</a></code>(1) for options to generate new packs and replace existing ones.</p>
<h2>OPTIONS</h2>
<p> -n</p>
<dl>
<dt>
<dd> Dry run. Check the pack file without actually unpacking the objects.</dl>
<p> -q</p>
<dl>
<dt>
<dd> The command usually shows percentage progress. This flag suppresses it.</dl>
<p> -r</p>
<dl>
<dt>
<dd> When unpacking a corrupt packfile, the command dies at the first corruption. This flag tells it to keep going and make the best effort to recover as many objects as possible.</dl>
<p> &#8211;strict</p>
<dl>
<dt>
<dd> Don&#8217;t write objects with broken content or links.</dl>
<p> &#8211;max-input-size=&lt;size&gt;</p>
<dl>
<dt>
<dd> Die, if the pack is larger than &lt;size&gt;.</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
