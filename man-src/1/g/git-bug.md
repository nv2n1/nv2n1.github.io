---
title: "git-bug(1)"
name: "git-bug"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-bug/"
description: "git-bug – Create bug branch"
---

<h2>NAME</h2>
<p> <code>git-bug</code> &#8211; Create bug branch</p>
<h2>SYNOPSIS</h2>
<p> <code>git-bug</code> [finish] &lt;name&gt;</p>
<h2>DESCRIPTION</h2>
<p> Create the given bug branch</p>
<h2>OPTIONS</h2>
<p> &lt;finish&gt; </p>
<p> Merge and delete the bug branch. </p>
<p> &lt;name&gt; </p>
<p> The name of the bug branch.</p>
<h2>EXAMPLES</h2>
<pre>
$ git bug bug-123456
...
$ git commit -m &quot;Some changes&quot;
...
$ git checkout master
$ git bug finish bug-123456
</pre>
<h2>AUTHOR</h2>
<p> Written by Jesús Espino &lt;<i>jespinog [at] gmail.com</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
