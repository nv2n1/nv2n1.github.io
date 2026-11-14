---
title: "git-verify-pack(1)"
name: "git-verify-pack"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-verify-pack/"
description: "git-verify-pack – Validate packed Git archive files"
---

<h2 class="name">NAME</h2>
<p> git-verify-pack &#8211; Validate packed Git archive files </p>
<h2>SYNOPSIS</h2>
<pre><code>
git verify - pack[-v | --verbose][-s | --stat - only][--]&lt;pack&gt;.idx...
</code></pre>
<h2>DESCRIPTION</h2>
<p> Reads given idx file for packed Git archive created with the <i>git pack-objects</i> command and verifies idx file and the corresponding pack file.</p>
<h2>OPTIONS</h2>
<p> &lt;pack&gt;.idx &#8230;</p>
<dl>
<dt>
<dd> The idx files to verify.</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> After verifying the pack, show list of objects contained in the pack and a histogram of delta chain length.</dl>
<p> -s, &#8211;stat-only</p>
<dl>
<dt>
<dd> Do not verify the pack contents; only show the histogram of delta chain length. With <code>&#8211;verbose</code>, list of objects is also shown.</dl>
<p> &#8212;</p>
<dl>
<dt>
<dd> Do not interpret any more arguments as options.</dl>
<h2>OUTPUT FORMAT</h2>
<p> When specifying the -v option the format used is: </p>
<dl>
<dt>
<dd>
<pre>
SHA-1 type size size-in-packfile offset-in-packfile
</pre>
</dl>
<p> for objects that are not deltified in the pack, and </p>
<dl>
<dt>
<dd>
<pre>
SHA-1 type size size-in-packfile offset-in-packfile depth base-SHA-1
</pre>
</dl>
<p> for objects that are deltified.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
