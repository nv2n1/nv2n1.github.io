---
title: "git-chore(1)"
name: "git-chore"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-chore/"
description: "git-chore – Create chore branch"
---

<h2>NAME</h2>
<p> <code>git-chore</code> &#8211; Create chore branch</p>
<h2>SYNOPSIS</h2>
<p> <code>git-chore</code> [finish] &lt;name&gt;</p>
<h2>DESCRIPTION</h2>
<p> Create the given chore branch</p>
<h2>OPTIONS</h2>
<p> &lt;finish&gt; </p>
<p> Merge and delete the chore branch. </p>
<p> &lt;name&gt; </p>
<p> The name of the chore branch.</p>
<h2>EXAMPLES</h2>
<pre>
$ git chore chore-123456
...
$ git commit -m &quot;Some changes&quot;
...
$ git checkout master
$ git chore finish chore-123456
</pre>
<h2>AUTHOR</h2>
<p> Written by Chris Hall &lt;<i>christopher.k.hall [at] gmail.com</i>&gt; from bug/feature/refactor comamnds originally written by Jesús Espino &lt;<i>jespinog [at] gmail.com</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
