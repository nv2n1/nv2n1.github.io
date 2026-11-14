---
title: "git-clear-soft(1)"
name: "git-clear-soft"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-clear-soft/"
description: "git-clear-soft – Soft clean up a repository"
---

<h2>NAME</h2>
<p> <code>git-clear-soft</code> &#8211; Soft clean up a repository</p>
<h2>SYNOPSIS</h2>
<p> <code>git-clear-soft</code></p>
<h2>DESCRIPTION</h2>
<p> Clears the repository to a state that it looks as if it was freshly cloned with the current HEAD, however, preserving all changes that are located in files and directories listed in .gitignore. It is a git-reset &#8211;hard together with deletion of all untracked files that reside inside the working directory, excluding those in .gitignore.</p>
<h2>EXAMPLES</h2>
<p> Clears the repo.</p>
<dl>
<dt>
<dd>
<pre>
$ git clear-soft
</pre>
<dt>
<dd></dl>
<h2>AUTHOR</h2>
<p> Modified version of script written by Daniel &#8216;grindhold&#8217; Brendle &lt;<i>grindhold [at] gmx.net</i>&gt; by Matiss Treinis &lt;<i>mrtreinis [at] gmail.com</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
