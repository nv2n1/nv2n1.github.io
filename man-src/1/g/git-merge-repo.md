---
title: "git-merge-repo(1)"
name: "git-merge-repo"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-merge-repo/"
description: "git-merge-repo – Merge two repo histories"
---

<h2>NAME</h2>
<p> <code>git-merge-repo</code> &#8211; Merge two repo histories</p>
<h2>SYNOPSIS</h2>
<p> <code>git-merge-repo</code> &lt;repo&gt; &lt;branch&gt; &lt;directory&gt; [&#8211;squash]</p>
<h2>DESCRIPTION</h2>
<p> Merges a repository&#8217;s history with the current repository, inside a specified directory. </p>
<p> Optional <code>&#8211;squash</code> flag skips the full history and generates only one commit for the merge.</p>
<h2>EXAMPLES</h2>
<p> Merges a local repo&#8217;s <code>frontend</code> branch into the current repo&#8217;s <code>web</code> folder:</p>
<dl>
<dt>
<dd>
<pre>
$ git merge-repo ../app/.git frontend web
</pre>
<dt>
<dd></dl>
<p> Merges a remote repo&#8217;s <code>master</code> branch into the current repo&#8217;s folder:</p>
<dl>
<dt>
<dd>
<pre>
$ git merge-repo git [at] github.com:tj/git-extras.git master .
</pre>
<dt>
<dd></dl>
<h2>AUTHOR</h2>
<p> Written by Ivan Malopinsky &lt;<i>hello [at] imsky.co</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
