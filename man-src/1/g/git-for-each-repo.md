---
title: "git-for-each-repo(1)"
name: "git-for-each-repo"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-for-each-repo/"
description: "git-for-each-repo – Run a Git command on a list of repositories"
---

<h2 class="name">NAME</h2>
<p> git-for-each-repo &#8211; Run a Git command on a list of repositories </p>
<h2>SYNOPSIS</h2>
<pre><code>
git for-each-repo --config=&lt;config&gt; [--] &lt;arguments&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> Run a Git command on a list of repositories. The arguments after the known options or <code>&#8212;</code> indicator are used as the arguments for the Git subprocess. </p>
<p> THIS COMMAND IS EXPERIMENTAL. THE BEHAVIOR MAY CHANGE. </p>
<p> For example, we could run maintenance on each of a list of repositories stored in a <code>maintenance.repo</code> config variable using </p>
<dl>
<dt>
<dd>
<pre>
git for-each-repo --config=maintenance.repo maintenance run
</pre>
</dl>
<p> This will run <code>git -C &lt;repo&gt; maintenance run</code> for each value <code>&lt;repo&gt;</code> in the multi-valued config variable <code>maintenance.repo</code>.</p>
<h2>OPTIONS</h2>
<p> &#8211;config=&lt;config&gt;</p>
<dl>
<dt>
<dd> Use the given config variable as a multi-valued list storing absolute path names. Iterate on that list of paths to run the given arguments. </p>
<p> These config values are loaded from system, global, and local Git config, as available. If <code>git for-each-repo</code> is run in a directory that is not a Git repository, then only the system and global config is used.</dl>
<h2>SUBPROCESS BEHAVIOR</h2>
<p> If any <code>git -C &lt;repo&gt; &lt;arguments&gt;</code> subprocess returns a non-zero exit code, then the <code>git for-each-repo</code> process returns that exit code without running more subprocesses. </p>
<p> Each <code>git -C &lt;repo&gt; &lt;arguments&gt;</code> subprocess inherits the standard file descriptors <code>stdin</code>, <code>stdout</code>, and <code>stderr</code>.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
