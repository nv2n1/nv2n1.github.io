---
title: "git-rename-branch(1)"
name: "git-rename-branch"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-rename-branch/"
description: "git-rename-branch – rename local branch and push to remote"
---

<h2>NAME</h2>
<p> <code>git-rename-branch</code> &#8211; rename local branch and push to remote</p>
<h2>SYNOPSIS</h2>
<p> <code>git-rename-branch</code> &lt;new-branch&gt; &lt;old-branch&gt;</p>
<h2>DESCRIPTION</h2>
<pre>
Rename local branch and push the new branch to remote
</pre>
<h2>OPTIONS</h2>
<pre>
&amp;lt;new-branch&amp;gt;
New branch name
&amp;lt;old-branch&amp;gt;
Old branch whose has to be renamed. This is an optional parameter. If no value is supplied then the current branch will be renamed.
</pre>
<h2>EXAMPLES</h2>
<pre>
$ git rename-branch new-name old-name
$ git rename-branch new-name
</pre>
<h2>AUTHOR</h2>
<p> Written by Hozefa Jodiawalla &lt;<i>hozefarules [at] gmail.com</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
