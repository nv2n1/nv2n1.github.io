---
title: "git-squash(1)"
name: "git-squash"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-squash/"
description: "git-squash – Import changes from a branch"
---

<h2>NAME</h2>
<p> <code>git-squash</code> &#8211; Import changes from a branch</p>
<h2>SYNOPSIS</h2>
<p> <code>git-squash</code> &lt;source-branch|commit ref&gt; [&lt;commit-message&gt;]</p>
<h2>DESCRIPTION</h2>
<p> Produce the working tree and index state as if a real merge happened without the commit or merge marks.</p>
<h2>OPTIONS</h2>
<p> &lt;source-branch&gt; </p>
<p> Branch to squash on the actual branch. </p>
<p> &lt;commit reference&gt; A commit reference (has to be from the current branch) can also be used as the first argument. A range of commits <i>sha</i>..HEAD will be squashed. </p>
<p> &lt;commit-message&gt; </p>
<p> If commit-message is given, commit the squash result.</p>
<h2>EXAMPLES</h2>
<pre>
$ git squash my-other-branch
Updating a2740f5..533b19c
Fast-forward
Squash commit -- not updating HEAD
 my-changed-file | 1 +
 1 file changed, 1 insertion(+)
$ git commit -m &quot;New commit without a real merge&quot;
$ git squash HEAD~3 &quot;Commit message&quot;
</pre>
<h2>AUTHOR</h2>
<p> Written by Jesús Espino &lt;<i>jespinog [at] gmail.com</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
