---
title: "git-commits-since(1)"
name: "git-commits-since"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-commits-since/"
description: "git-commits-since – Show commit logs since some date"
---

<h2>NAME</h2>
<p> <code>git-commits-since</code> &#8211; Show commit logs since some date</p>
<h2>SYNOPSIS</h2>
<p> <code>git-commits-since</code> [&lt;date&gt;]</p>
<h2>DESCRIPTION</h2>
<p> List of commits since the given <i>date</i>.</p>
<h2>OPTIONS</h2>
<p> &lt;date&gt; </p>
<p> Show commits more recent than <i>date</i>. By default, the command shows the commit logs since &quot;last week&quot;.</p>
<h2>EXAMPLES</h2>
<p> It is really flexible and these are only 3 of the options, go ahead give it a try:</p>
<dl>
<dt>
<dd>
<pre>
$ git commits-since yesterday
... commits since yesterday
nickl- - Merge branch upstream master.
nickl- - Rebase bolshakov with master
TJ Holowaychuk - Merge pull request #128 from nickl-/git-extras-html-hyperlinks
TJ Holowaychuk - Merge pull request #129 from nickl-/develop
nickl- - Fix #127 git-ignore won't add duplicates.
$ git commits-since 3 o clock pm
... commits since 3 o clock pm
nickl- - Merge branch upstream master.
$ git commits-since 2 hour ago
... commits since 2 hour ago
nickl- - Merge branch upstream master.
TJ Holowaychuk - Merge pull request #128 from nickl-/git-extras-html-hyperlinks
TJ Holowaychuk - Merge pull request #129 from nickl-/develop
</pre>
<dt>
<dd></dl>
<h2>AUTHOR</h2>
<p> Written by Tj Holowaychuk &lt;<i>tj [at] vision-media.ca</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
