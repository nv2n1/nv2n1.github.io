---
title: "git-root(1)"
name: "git-root"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-root/"
description: "git-root – show path of root"
---

<h2>NAME</h2>
<p> <code>git-root</code> &#8211; show path of root</p>
<h2>SYNOPSIS</h2>
<p> <code>git root</code> <i>OPTIONS</i></p>
<h2>DESCRIPTION</h2>
<p> print the path for the root directory of git repo</p>
<h2>OPTIONS</h2>
<p> -r, &#8211;relative </p>
<p> show the relative path from root directory to current directory</p>
<h2>EXAMPLES</h2>
<pre>
$ cd .../git-extras/bin
$ git root -r
bin/
$ git root
/home/.../git-extras
$ cd `git root`
$ pwd
/home/.../git-extras
# then we can
$ git add . &amp;&amp; git commit
</pre>
<h2>AUTHOR</h2>
<p> Written by spacewander &lt;<i>spacewanderlzx [at] gmail.com</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
