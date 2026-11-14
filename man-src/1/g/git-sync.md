---
title: "git-sync(1)"
name: "git-sync"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-sync/"
description: "git-sync – Sync local branch with remote branch"
---

<h2>NAME</h2>
<p> <code>git-sync</code> &#8211; Sync local branch with remote branch</p>
<h2>SYNOPSIS</h2>
<p> <code>git sync</code> [ &lt;remote&gt; &lt;branch&gt; ]</p>
<h2>DESCRIPTION</h2>
<p> Sync local branch with &lt;remote&gt;/&lt;branch&gt;. </p>
<p> When &lt;remote&gt; and &lt;branch&gt; are not specified on the command line, upstream of local branch will be used by default. </p>
<p> All changes and untracked files and directories will be removed.</p>
<h2>EXAMPLES</h2>
<p> Sync local branch with its upstream</p>
<dl>
<dt>
<dd>
<pre>
$ git sync
</pre>
<dt>
<dd></dl>
<p> Sync local branch with origin/master</p>
<dl>
<dt>
<dd>
<pre>
$ git sync origin master
</pre>
<dt>
<dd></dl>
<h2>AUTHOR</h2>
<p> Written by Takuma Yamaguchi &lt;<i>kumon0587 [at] gmail.com</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
