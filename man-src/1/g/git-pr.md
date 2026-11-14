---
title: "git-pr(1)"
name: "git-pr"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-pr/"
description: "git-pr – Checks out a pull request locally"
---

<h2>NAME</h2>
<p> <code>git-pr</code> &#8211; Checks out a pull request locally</p>
<h2>SYNOPSIS</h2>
<p> <code>git-pr</code> &lt;number&gt; [&lt;remote&gt;]<br />
 <code>git-pr</code> &lt;url&gt;<br />
 <code>git-pr clean</code></p>
<h2>DESCRIPTION</h2>
<p> Creates a local branch based on a GitHub pull request number or URL, and switch to that branch afterwards.</p>
<h2>OPTIONS</h2>
<p> &lt;remote&gt; </p>
<p> The name of the remote to fetch from. Defaults to <code>origin</code>. </p>
<p> &lt;url&gt; </p>
<p> GitHub pull request URL in the format <code><a rel="nofollow" href="https://github.com/tj/git-extras/pull/453">https://github.com/tj/git-extras/pull/453</a></code>.</p>
<h2>EXAMPLES</h2>
<p> This checks out the pull request <code>226</code> from <code>origin</code>:</p>
<dl>
<dt>
<dd>
<pre>
$ git pr 226
remote: Counting objects: 12, done.
remote: Compressing objects: 100% (9/9), done.
remote: Total 12 (delta 3), reused 9 (delta 3)
Unpacking objects: 100% (12/12), done.
From <a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a>
 * [new ref]         refs/pull/226/head -&gt; pr/226
Switched to branch 'pr/226'
</pre>
<dt>
<dd></dl>
<p> This pulls from a different remote:</p>
<dl>
<dt>
<dd>
<pre>
$ git pr 226 upstream
</pre>
<dt>
<dd></dl>
<p> You can also checkout a pull request based on a GitHub URL:</p>
<dl>
<dt>
<dd>
<pre>
$ git pr <a rel="nofollow" href="https://github.com/tj/git-extras/pull/453">https://github.com/tj/git-extras/pull/453</a>
From <a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a>
 * [new ref]         refs/pull/453/head -&gt; pr/453
Switched to branch 'pr/453'
</pre>
<dt>
<dd></dl>
<p> To clean up old branches:</p>
<dl>
<dt>
<dd>
<pre>
$ git pr clean
Deleted branch pr/226 (was b96a8c2).
Deleted branch pr/220 (was d34dc0f).
</pre>
<dt>
<dd></dl>
<h2>AUTHOR</h2>
<p> Originally from <a rel="nofollow" href="https://gist.github.com/gnarf/5406589">https://gist.github.com/gnarf/5406589</a></p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
