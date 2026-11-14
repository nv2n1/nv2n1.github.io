---
title: "git-merge-tree(1)"
name: "git-merge-tree"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-merge-tree/"
description: "git-merge-tree – Show three-way merge without touching index"
---

<h2 class="name">NAME</h2>
<p> git-merge-tree &#8211; Show three-way merge without touching index </p>
<h2>SYNOPSIS</h2>
<pre>
<i>git merge-tree</i> &lt;base-tree&gt; &lt;branch1&gt; &lt;branch2&gt;
</pre>
<h2>DESCRIPTION</h2>
<p> Reads three tree-ish, and output trivial merge results and conflicting stages to the standard output. This is similar to what three-way <i>git read-tree -m</i> does, but instead of storing the results in the index, the command outputs the entries to the standard output. </p>
<p> This is meant to be used by higher level scripts to compute merge results outside of the index, and stuff the results back into the index. For this reason, the output from the command omits entries that match the &lt;branch1&gt; tree.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
