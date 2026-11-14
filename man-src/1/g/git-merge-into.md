---
title: "git-merge-into(1)"
name: "git-merge-into"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-merge-into/"
description: "git-merge-into – Merge one branch into another"
---

<h2>NAME</h2>
<p> <code>git-merge-into</code> &#8211; Merge one branch into another</p>
<h2>SYNOPSIS</h2>
<p> <code>git merge-into</code> [src] &lt;dest&gt; [&#8211;ff-only]</p>
<h2>DESCRIPTION</h2>
<p> Merge one branch into another, and keep yourself on current branch. If src branch not given, it will merge current one to dest.</p>
<h2>OPTIONS</h2>
<p> &lt;src&gt; </p>
<p> The name of the branch will be merged into. If this not given, use current branch as default. </p>
<p> &lt;dest&gt; </p>
<p> The name of the branch to merge into. </p>
<p> &#8211;ff-only </p>
<p> Refuse to merge and exit with a non-zero status unless the current HEAD is already up-to-date or the merge can be resolved as a fast-forward.</p>
<h2>EXAMPLES</h2>
<p> Assume the following history exists and the current branch is src:</p>
<dl>
<dt>
<dd>
<pre><code>
A-- - B-- - C src(current) / D-- - E-- - F-- - G dest
</code></pre>
<dt>
<dd></dl>
<p> After running <code>git merge-into dest</code>, it will look like this:</p>
<dl>
<dt>
<dd>
<pre><code>
A-- - B-- - C src(current) / D-- - E-- - F-- - G-- - H dest
</code></pre>
<dt>
<dd></dl>
<p> The <code>H</code> commit will record the merge result, just like what <code>git merge</code> does. And <code>src</code> is still the current branch. </p>
<p> The default implementation of <code>merge-into</code> use <code>git checkout</code> and <code>git merge</code>, which may cause temporary change in the working tree. If you make sure your branch can be merged fast-forward, add <code>&#8211;ff-only</code> to avoid files change.</p>
<h2>AUTHOR</h2>
<p> Written by spacewander &lt;<i>spacewanderlzx [at] gmail.com</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
