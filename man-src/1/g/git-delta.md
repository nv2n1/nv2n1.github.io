---
title: "git-delta(1)"
name: "git-delta"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-delta/"
description: "git-delta – Lists changed files"
---

<h2>NAME</h2>
<p> <code>git-delta</code> &#8211; Lists changed files</p>
<h2>SYNOPSIS</h2>
<p> <code>git-delta</code> [&lt;branch&gt;] [&lt;filter&gt;]</p>
<h2>DESCRIPTION</h2>
<p> Lists all files that differ from a branch. By default, lists files that have been added, copied, or modified as compared to the <code>master</code> branch.</p>
<h2>EXAMPLES</h2>
<p> Lists all modified and renamed files vs. <code>master</code>:</p>
<dl>
<dt>
<dd>
<pre>
$ git delta master MR
</pre>
<dt>
<dd></dl>
<p> Lists all deleted files vs. <code>example</code>:</p>
<dl>
<dt>
<dd>
<pre>
$ git delta example D
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
