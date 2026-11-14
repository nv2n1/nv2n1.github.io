---
title: "git-standup(1)"
name: "git-standup"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-standup/"
description: "git-standup – Recall the commit history"
---

<h2>NAME</h2>
<p> <code>git-standup</code> &#8211; Recall the commit history</p>
<h2>SYNOPSIS</h2>
<p> <code>git-standup</code> [&lt;full name&gt;] [&lt;since&gt;] [&lt;until&gt;]</p>
<h2>DESCRIPTION</h2>
<p> Recall what you did on the last working day ..or be nosy and find what someone else did.</p>
<h2>OPTIONS</h2>
<p> &lt;full name&gt; </p>
<p> The author of commits. Defaults to <code>$(git config user.name)</code>. </p>
<p> &lt;since&gt; </p>
<p> The start of commit history. Defaults to <code>yesterday</code>. </p>
<p> &lt;until&gt; </p>
<p> The end of commit history. Defaults to <code>today</code>.</p>
<h2>EXAMPLES</h2>
<p> This shows your commits since yesterday:</p>
<dl>
<dt>
<dd>
<pre>
$ git standup
a26d1f9 - add profile hook (69 minutes ago) &lt;spacewander&gt;
</pre>
<dt>
<dd></dl>
<p> This shows the author&#8217;s commits since last week:</p>
<dl>
<dt>
<dd>
<pre>
$ git standup spacewander &quot;last week&quot;
a26d1f9 - add profile hook (70 minutes ago) &lt;spacewander&gt;
4e19859 - fix getTotalSize return value error (6 days ago) &lt;spacewander&gt;
36da84e - fix rename over bound (7 days ago) &lt;spacewander&gt;
8e4182a - add watermark.png (7 days ago) &lt;spacewander&gt;
46fef1d - use tinyXML to configure (7 days ago) &lt;spacewander&gt;
</pre>
<dt>
<dd></dl>
<p> If current directory is not a git repo, git-standup will fetch data from all top-level git repos under it:</p>
<dl>
<dt>
<dd>
<pre>
$ cd ..
$ git standup spacewander &quot;last week&quot; yesterday
someProject/
4e19859 - fix getTotalSize return value error (6 days ago) &lt;spacewander&gt;
36da84e - fix rename over bound (7 days ago) &lt;spacewander&gt;
8e4182a - add watermark.png (7 days ago) &lt;spacewander&gt;
46fef1d - use tinyXML to configure (7 days ago) &lt;spacewander&gt;
</pre>
<dt>
<dd></dl>
<h2>AUTHOR</h2>
<p> Originally from <a rel="nofollow" href="https://github.com/kamranahmedse/git-standup">https://github.com/kamranahmedse/git-standup</a></p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
