---
title: "git-feature(1)"
name: "git-feature"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-feature/"
description: "git-feature – Create/Merge feature branch"
---

<h2>NAME</h2>
<p> <code>git-feature</code> &#8211; Create/Merge feature branch</p>
<h2>SYNOPSIS</h2>
<p> <code>git-feature</code> [-a|&#8211;alias branch_prefix] [finish] &lt;name&gt;</p>
<h2>DESCRIPTION</h2>
<p> Create/Merge the given feature branch</p>
<h2>OPTIONS</h2>
<p> &lt;-a|&#8211;alias branch_prefix&gt; </p>
<p> use <code>branch_prefix</code> instead of <code>feature</code> </p>
<p> &lt;finish&gt; </p>
<p> Merge and delete the feature branch. </p>
<p> &lt;name&gt; </p>
<p> The name of the feature branch.</p>
<h2>EXAMPLES</h2>
<pre>
$ git feature dependencies
...
$ (feature/dependencies) git commit -m &quot;Some changes&quot;
...
$ (feature/dependencies) git checkout master
$ git feature finish dependencies
$ git alias features &quot;feature -a features&quot;
$ git features dependencies
$ (features/dependencies) ...
$ (features/dependencies) git checkout master
$ git features finish dependencies
</pre>
<h2>AUTHOR</h2>
<p> Written by Jesús Espino &lt;<i>jespinog [at] gmail.com</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
