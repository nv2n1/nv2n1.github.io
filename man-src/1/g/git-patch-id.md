---
title: "git-patch-id(1)"
name: "git-patch-id"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-patch-id/"
description: "git-patch-id – Compute unique ID for a patch"
---

<h2 class="name">NAME</h2>
<p> git-patch-id &#8211; Compute unique ID for a patch </p>
<h2>SYNOPSIS</h2>
<pre><code>
git patch - id[--stable | --unstable]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Read a patch from the standard input and compute the patch ID for it. </p>
<p> A &quot;patch ID&quot; is nothing but a sum of SHA-1 of the file diffs associated with a patch, with whitespace and line numbers ignored. As such, it&#8217;s &quot;reasonably stable&quot;, but at the same time also reasonably unique, i.e., two patches that have the same &quot;patch ID&quot; are almost guaranteed to be the same thing. </p>
<p> IOW, you can use this thing to look for likely duplicate commits. </p>
<p> When dealing with <i>git diff-tree</i> output, it takes advantage of the fact that the patch is prefixed with the object name of the commit, and outputs two 40-byte hexadecimal strings. The first string is the patch ID, and the second string is the commit ID. This can be used to make a mapping from patch ID to commit ID.</p>
<h2>OPTIONS</h2>
<p> &#8211;stable</p>
<dl>
<dt>
<dd> Use a &quot;stable&quot; sum of hashes as the patch ID. With this option: </p>
<dl>
<dt>
<dd> &bull; Reordering file diffs that make up a patch does not affect the ID. In particular, two patches produced by comparing the same two trees with two different settings for &quot;-O&lt;orderfile&gt;&quot; result in the same patch ID signature, thereby allowing the computed result to be used as a key to index some meta-information about the change between the two trees;</dl>
<dl>
<dt>
<dd> &bull; Result is different from the value produced by git 1.9 and older or produced when an &quot;unstable&quot; hash (see &#8211;unstable below) is configured &#8211; even when used on a diff output taken without any use of &quot;-O&lt;orderfile&gt;&quot;, thereby making existing databases storing such &quot;unstable&quot; or historical patch-ids unusable. </p>
<dl>
<dt>
<dd>
<pre>
This is the default if patchid.stable is set to true.
</pre>
</dl>
</dl>
</dl>
<p> &#8211;unstable</p>
<dl>
<dt>
<dd> Use an &quot;unstable&quot; hash as the patch ID. With this option, the result produced is compatible with the patch-id value produced by git 1.9 and older. Users with pre-existing databases storing patch-ids produced by git 1.9 and older (who do not deal with reordered patches) may want to use this option. </p>
<dl>
<dt>
<dd>
<pre>
This is the default.
</pre>
</dl>
</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
