---
title: "git-clear(1)"
name: "git-clear"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-clear/"
description: "git-clear – Rigorously clean up a repository"
---

<h2>NAME</h2>
<p> <code>git-clear</code> &#8211; Rigorously clean up a repository</p>
<h2>SYNOPSIS</h2>
<p> <code>git-clear</code></p>
<h2>DESCRIPTION</h2>
<p> Clears the repository to a state that it looks as if it was freshly cloned with the current HEAD. Basically it is a git-reset &#8211;hard together with deletion of all untracked files that reside inside the working directory, including those in .gitignore.</p>
<h2>EXAMPLES</h2>
<p> Clears the repo.</p>
<dl>
<dt>
<dd>
<pre>
$ git clear
</pre>
<dt>
<dd></dl>
<h2>AUTHOR</h2>
<p> Written by Daniel &#8216;grindhold&#8217; Brendle &lt;<i>grindhold [at] gmx.net</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
