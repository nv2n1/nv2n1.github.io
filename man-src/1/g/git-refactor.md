---
title: "git-refactor(1)"
name: "git-refactor"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-refactor/"
description: "git-refactor – Create refactor branch"
---

<h2>NAME</h2>
<p> <code>git-refactor</code> &#8211; Create refactor branch</p>
<h2>SYNOPSIS</h2>
<p> <code>git-refactor</code> [finish] &lt;name&gt;</p>
<h2>DESCRIPTION</h2>
<p> Create the given refactor branch</p>
<h2>OPTIONS</h2>
<p> &lt;finish&gt; </p>
<p> Merge and delete the refactor branch. </p>
<p> &lt;name&gt; </p>
<p> The name of the refactor branch.</p>
<h2>EXAMPLES</h2>
<pre>
$ git refactor mainlib_refactor
...
$ git commit -m &quot;Some changes&quot;
...
$ git checkout master
$ git refactor finish mainlib_refactor
</pre>
<h2>AUTHOR</h2>
<p> Written by Jesús Espino &lt;<i>jespinog [at] gmail.com</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
