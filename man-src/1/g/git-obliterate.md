---
title: "git-obliterate(1)"
name: "git-obliterate"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-obliterate/"
description: "git-obliterate – rewrite past commits to remove some files"
---

<h2>NAME</h2>
<p> <code>git-obliterate</code> &#8211; rewrite past commits to remove some files</p>
<h2>SYNOPSIS</h2>
<p> git obliterate &lt;files&#8230;&gt; [&#8211; &lt;rev-list options&#8230;&gt;]</p>
<h2>DESCRIPTION</h2>
<p> Completely remove some files from the repository, including past commits and tags. WARNING! This command will rewirte the history similar to <code>git rebase</code>(though it affects more). The rewritten history will have different object names for all the objects and will not converge with the original branch. So <code>avoid using it on commits that you shared</code>. And it will mess up stash, so <code>don&#8217;t have stash when you run git obliterate</code>.</p>
<h2>OPTIONS</h2>
<p> You can pass rev-list options to indicate the range of commits affected. Those options need to be seperated with &#8216;&#8211;&#8216; before them. Run <code>git help rev-list</code> to see the acceptable options.</p>
<h2>Examples</h2>
<p> Remove .secret from the repository:</p>
<dl>
<dt>
<dd>
<pre>
$ git obliterate .secret
</pre>
<dt>
<dd></dl>
<p> Remove .secret from commits between origin and feature:</p>
<dl>
<dt>
<dd>
<pre>
$ git obliterate .secret -- feature ^origin
</pre>
<dt>
<dd></dl>
<p> Remove .secret from commit abcdefg to commit 1234567</p>
<dl>
<dt>
<dd>
<pre>
$ git obliterate .secret -- abcdefg..1234567
</pre>
<dt>
<dd></dl>
<h2>AUTHOR</h2>
<p> Written by &lt;<i>brianloveswords [at] gmail.com</i>&gt;</p>
<h2>REPORTING BUG</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
