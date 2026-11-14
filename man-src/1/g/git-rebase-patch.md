---
title: "git-rebase-patch(1)"
name: "git-rebase-patch"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-rebase-patch/"
description: "git-rebase-patch – Rebases a patch"
---

<h2>NAME</h2>
<p> <code>git-rebase-patch</code> &#8211; Rebases a patch</p>
<h2>SYNOPSIS</h2>
<p> <code>git-rebase-patch</code> &lt;patch-file&gt;</p>
<h2>DESCRIPTION</h2>
<p> Given you have a patch that doesn&#8217;t apply to the current HEAD, but you know it applied to some commit in the past, <code>git-rebase-patch</code> will help you find that commit and do a rebase.</p>
<h2>OPTIONS</h2>
<dl>
<dt>&lt;patch-file&gt;</p>
<dd> The patch to be applied.</dl>
<h2>EXAMPLES</h2>
<p> Executing</p>
<dl>
<dt>
<dd>
<pre>
$ git rebase-patch test.patch
</pre>
<dt>
<dd></dl>
<p> could give you something like that:</p>
<dl>
<dt>
<dd>
<pre>
Trying to find a commit the patch applies to...
Patch applied to dbcf408dd26 as 7dc8b23ae1a
First, rewinding head to replay your work on top of it...
Applying: test.patch
Using index info to reconstruct a base tree...
Falling back to patching base and 3-way merge...
Auto-merging README.txt
</pre>
<dt>
<dd></dl>
<p> Then your last commit has the changes of the patch and is named <i>test.patch</i>.</p>
<h2>AUTHOR</h2>
<p> Written by Niklas Fiekas &lt;<i>niklas.fiekas [at] tu-clausthal.de</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="http://github.com/tj/git-extras/issues">http://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="http://github.com/tj/git-extras">http://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
