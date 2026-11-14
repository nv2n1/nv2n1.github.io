---
title: "git-symbolic-ref(1)"
name: "git-symbolic-ref"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-symbolic-ref/"
description: "git-symbolic-ref – Read, modify and delete symbolic refs"
---

<h2 class="name">NAME</h2>
<p> git-symbolic-ref &#8211; Read, modify and delete symbolic refs </p>
<h2>SYNOPSIS</h2>
<pre><code>
git symbolic - ref[-m&lt;reason&gt;]&lt;name&gt;&lt;ref&gt; git symbolic - ref[-q][--short]&lt;name&gt; git symbolic - ref-- delete[-q]&lt;name&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> Given one argument, reads which branch head the given symbolic ref refers to and outputs its path, relative to the <code>.git/</code> directory. Typically you would give <code>HEAD</code> as the &lt;name&gt; argument to see which branch your working tree is on. </p>
<p> Given two arguments, creates or updates a symbolic ref &lt;name&gt; to point at the given branch &lt;ref&gt;. </p>
<p> Given <code>&#8211;delete</code> and an additional argument, deletes the given symbolic ref. </p>
<p> A symbolic ref is a regular file that stores a string that begins with <code>ref: refs/</code>. For example, your <code>.git/HEAD</code> is a regular file whose contents is <code>ref: refs/heads/master</code>.</p>
<h2>OPTIONS</h2>
<p> -d, &#8211;delete</p>
<dl>
<dt>
<dd> Delete the symbolic ref &lt;name&gt;.</dl>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> Do not issue an error message if the &lt;name&gt; is not a symbolic ref but a detached HEAD; instead exit with non-zero status silently.</dl>
<p> &#8211;short</p>
<dl>
<dt>
<dd> When showing the value of &lt;name&gt; as a symbolic ref, try to shorten the value, e.g. from <code>refs/heads/master</code> to <code>master</code>.</dl>
<p> -m</p>
<dl>
<dt>
<dd> Update the reflog for &lt;name&gt; with &lt;reason&gt;. This is valid only when creating or updating a symbolic ref.</dl>
<h2>NOTES</h2>
<p> In the past, <code>.git/HEAD</code> was a symbolic link pointing at <code>refs/heads/master</code>. When we wanted to switch to another branch, we did <code>ln -sf refs/heads/newbranch .git/HEAD</code>, and when we wanted to find out which branch we are on, we did <code>readlink .git/HEAD</code>. But symbolic links are not entirely portable, so they are now deprecated and symbolic refs (as described above) are used by default. </p>
<p> <i>git symbolic-ref</i> will exit with status 0 if the contents of the symbolic ref were printed correctly, with status 1 if the requested name is not a symbolic ref, or 128 if another error occurs.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
