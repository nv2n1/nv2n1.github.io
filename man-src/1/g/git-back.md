---
title: "git-back(1)"
name: "git-back"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-back/"
description: "git-back – Undo and Stage latest commits"
---

<h2>NAME</h2>
<p> <code>git-back</code> &#8211; Undo and Stage latest commits</p>
<h2>SYNOPSIS</h2>
<p> <code>git-back</code> [&lt;commitcount&gt;]</p>
<h2>DESCRIPTION</h2>
<p> Removes the latest commits, and add their changes to your staging area.</p>
<h2>OPTIONS</h2>
<p> &lt;commitcount&gt; </p>
<p> Number of commits to remove. Defaults to <i>1</i>, thus remove the latest commit.</p>
<h2>EXAMPLES</h2>
<p> Removes the latest commit.</p>
<dl>
<dt>
<dd>
<pre>
$ git back
</pre>
<dt>
<dd></dl>
<p> Remove the latest 3 commits:</p>
<dl>
<dt>
<dd>
<pre>
$ git back 3
</pre>
<dt>
<dd></dl>
<h2>AUTHOR</h2>
<p> Written by Kenneth Reitz &lt;<i>me [at] kennethreitz.com</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
