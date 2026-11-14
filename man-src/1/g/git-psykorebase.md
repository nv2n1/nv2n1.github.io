---
title: "git-psykorebase(1)"
name: "git-psykorebase"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-psykorebase/"
description: "git-psykorebase – Rebase a branch with a merge commit"
---

<h2>NAME</h2>
<p> <code>git-psykorebase</code> &#8211; Rebase a branch with a merge commit</p>
<h2>SYNOPSIS</h2>
<p> <code>git-psykorebase</code> &lt;target_branch&gt; [&lt;feature_branch&gt;] [&#8211;no-ff] </p>
<p> <code>git-psykorebase</code> &#8211;continue</p>
<h2>DESCRIPTION</h2>
<p> Rebase the <code>feature_branch</code> on top of the <code>target_branch</code>, the <code>feature_branch</code> defaults to the current one.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;no-ff</code> Force a commit message even if there are no conflicts. </p>
<p> <code>&#8211;continue</code> Continue the rebase after conflicts have been resolved.</p>
<h2>EXAMPLES</h2>
<p> Rebase current branch on top of master:</p>
<dl>
<dt>
<dd>
<pre>
$ git psykorebase master --no-ff
</pre>
<dt>
<dd></dl>
<p> Handle conflicts:</p>
<dl>
<dt>
<dd>
<pre>
$ git add README.md
</pre>
<dt>
<dd></dl>
<p> Continue rebase:</p>
<dl>
<dt>
<dd>
<pre>
$ git psykorebase --continue
</pre>
<dt>
<dd></dl>
<h2>AUTHOR</h2>
<p> Written by Rémy Hubscher &lt;<i>rhubscher [at] mozilla.com</i>&gt; </p>
<p> Based on Benoît Bryon &lt;<i>benoit [at] marmelune.net</i>&gt; implementation in Python.</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<p> &lt;<i><a rel="nofollow" href="https://github.com/benoitbryon/psykorebase">https://github.com/benoitbryon/psykorebase</a></i>&gt; </p>
<h2>Index</h2>
