---
title: "git-undo(1)"
name: "git-undo"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-undo/"
description: "git-undo – Remove latest commits"
---

<h2>NAME</h2>
<p> <code>git-undo</code> &#8211; Remove latest commits</p>
<h2>SYNOPSIS</h2>
<p> <code>git-undo</code> [&lt;commitcount&gt;] [-s, &#8211;soft, -h, &#8211;hard]</p>
<h2>DESCRIPTION</h2>
<p> Removes the latest commits.</p>
<h2>OPTIONS</h2>
<p> &#8211;soft or -s </p>
<p> This is the default, only rolls back the commit but changes remain un-staged. </p>
<p> &#8211;hard or -h </p>
<p> This option wipes your commit(s), so that your changes cannot be recovered. Use with care. </p>
<p> &lt;commitcount&gt; </p>
<p> Number of commits to remove. Defaults to <i>1</i>, thus remove the latest commit.</p>
<h2>EXAMPLES</h2>
<p> Removes the latest commit.</p>
<dl>
<dt>
<dd>
<pre>
$ git undo
</pre>
<dt>
<dd></dl>
<p> Remove the latest 3 commits:</p>
<dl>
<dt>
<dd>
<pre>
$ git undo 3
</pre>
<dt>
<dd></dl>
<h2>AUTHOR</h2>
<p> Written by Kenneth Reitz &lt;<i>me [at] kennethreitz.com</i>&gt; and Nick Lombard &lt;<i>github [at] jigsoft.co.za</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
