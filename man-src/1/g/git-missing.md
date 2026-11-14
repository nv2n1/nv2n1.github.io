---
title: "git-missing(1)"
name: "git-missing"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-missing/"
description: "git-missing – Show commits missing from another branch"
---

<h2>NAME</h2>
<p> <code>git-missing</code> &#8211; Show commits missing from another branch</p>
<h2>SYNOPSIS</h2>
<p> <code>git-missing</code> [&lt;first branch&gt;] &lt;second branch&gt; [&lt;git log options&gt;]</p>
<h2>DESCRIPTION</h2>
<p> Shows commits that are in either of two branches but not both. Useful for seeing what would come across in a merge or push.</p>
<h2>OPTIONS</h2>
<p> [&lt;first branch&gt;] </p>
<p> First branch to compare. If not specified, defaults to currently checked out branch. </p>
<p> &lt;second branch&gt; </p>
<p> Second branch to compare. </p>
<p> [&lt;git log options&gt;] </p>
<p> Any flags that should be passed to &#8216;git log&#8217;, such as &#8211;no-merges.</p>
<h2>EXAMPLES</h2>
<p> Show commits on either my current branch or master but not both:</p>
<dl>
<dt>
<dd>
<pre>
$ git missing master
&lt; d14b8f0 only on current checked out branch
&gt; 97ef387 only on master
</pre>
<dt>
<dd></dl>
<p> Show commits on either branch foo or branch bar but not both:</p>
<dl>
<dt>
<dd>
<pre>
$ git missing foo bar
&lt; b8f0d14 only on foo
&gt; f38797e only on bar
</pre>
<dt>
<dd></dl>
<h2>AUTHOR</h2>
<p> Written by Nate Jones &lt;<i>nate [at] endot.org</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="http://github.com/tj/git-extras/issues">http://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="http://github.com/tj/git-extras">http://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
