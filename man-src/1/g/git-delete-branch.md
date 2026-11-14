---
title: "git-delete-branch(1)"
name: "git-delete-branch"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-delete-branch/"
description: "git-delete-branch – Delete branches"
---

<h2>NAME</h2>
<p> <code>git-delete-branch</code> &#8211; Delete branches</p>
<h2>SYNOPSIS</h2>
<p> <code>git-delete-branch</code> &lt;branchname&gt;</p>
<h2>DESCRIPTION</h2>
<p> Deletes local and remote branch named &lt;branchname&gt;. Note that local deletion fails if the branch is checked out.</p>
<h2>OPTIONS</h2>
<p> &lt;branchname&gt; </p>
<p> The name of the branch to delete. If multiple branches are provided, then they will all be deleted.</p>
<h2>EXAMPLES</h2>
<pre>
$ git delete-branch integration
$ git delete-branch integration bug/1234
</pre>
<h2>AUTHOR</h2>
<p> Written by Tj Holowaychuk &lt;<i>tj [at] vision-media.ca</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
