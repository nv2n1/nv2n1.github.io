---
title: "git-show-index(1)"
name: "git-show-index"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-show-index/"
description: "git-show-index – Show packed archive index"
---

<h2 class="name">NAME</h2>
<p> git-show-index &#8211; Show packed archive index </p>
<h2>SYNOPSIS</h2>
<pre>
<i>git show-index</i> [--object-format=&lt;hash-algorithm&gt;]
</pre>
<h2>DESCRIPTION</h2>
<p> Read the <code>.idx</code> file for a Git packfile (created with <code><a href="/docs/linux/man/1-git-pack-objects/">git-pack-objects</a></code>(1) or <code><a href="/docs/linux/man/1-git-index-pack/">git-index-pack</a></code>(1)) from the standard input, and dump its contents. The output consists of one object per line, with each line containing two or three space-separated columns: </p>
<dl>
<dt>
<dd> &bull; the first column is the offset in bytes of the object within the corresponding packfile</dl>
<dl>
<dt>
<dd> &bull; the second column is the object id of the object</dl>
<dl>
<dt>
<dd> &bull; if the index version is 2 or higher, the third column contains the CRC32 of the object data</dl>
<p> The objects are output in the order in which they are found in the index file, which should be (in a correctly constructed file) sorted by object id. </p>
<p> Note that you can get more information on a packfile by calling <code><a href="/docs/linux/man/1-git-verify-pack/">git-verify-pack</a></code>(1). However, as this command considers only the index file itself, it&#8217;s both faster and more flexible.</p>
<h2>OPTIONS</h2>
<p> &#8211;object-format=&lt;hash-algorithm&gt;</p>
<dl>
<dt>
<dd> Specify the given object format (hash algorithm) for the index file. The valid values are <i>sha1</i> and (if enabled) <i>sha256</i>. The default is the algorithm for the current repository (set by <code>extensions.objectFormat</code>), or <i>sha1</i> if no value is set or outside a repository.. </p>
<p> THIS OPTION IS EXPERIMENTAL! SHA-256 support is experimental and still in an early stage. A SHA-256 repository will in general not be able to share work with &quot;regular&quot; SHA-1 repositories. It should be assumed that, e.g., Git internal file formats in relation to SHA-256 repositories may change in backwards-incompatible ways. Only use <code>&#8211;object-format=sha256</code> for testing purposes.</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
