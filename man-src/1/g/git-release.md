---
title: "git-release(1)"
name: "git-release"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-release/"
description: "git-release – Commit, tag and push changes to the repository"
---

<h2>NAME</h2>
<p> <code>git-release</code> &#8211; Commit, tag and push changes to the repository</p>
<h2>SYNOPSIS</h2>
<p> <code>git-release</code> &lt;tagname&gt; [-r &lt;remote&gt;] [-m &lt;commit info%gt;] [-c]</p>
<h2>DESCRIPTION</h2>
<p> Commits changes with message &quot;Release &lt;tagname&gt;&quot; or custom commit information, tags with the given &lt;tagname&gt; and pushes the branch / tags. Optionally it generates a changelog (see git-changelog) and a remote can be defined. The order of first -c or -r does not matter.</p>
<h2>OPTIONS</h2>
<p> &lt;tagname&gt; </p>
<p> The name of the newly created tag. Also used in tag comment. </p>
<p> -r &lt;remote&gt; </p>
<p> The &quot;remote&quot; repository that is destination of a push operation: it is passed to git push. </p>
<p> -m &lt;commit info&gt; </p>
<p> use the custom commit information instead of the default message &quot;Release &lt;tagname&gt;&quot; . </p>
<p> -c </p>
<p> Generates or populates the changelog with all commit message since the last tag. For more info see git-changelog..</p>
<h2>EXAMPLES</h2>
<dl>
<dt>&bull;</p>
<dd> Release commit with the given &lt;tagname&gt;.</p>
<dt>
<dd> $ git release 0.1.0</p>
<dt>&bull;</p>
<dd> Release commit with the given &lt;tagname&gt; and custom commit message.</p>
<dt>
<dd> $ git release 0.1.0 -m &quot;+ powerful feature added.&quot;</p>
<dt>&bull;</p>
<dd> Release commit with the given &lt;tagname&gt; and push to specific remote.</p>
<dt>
<dd> $ git release 0.1.0 -r github</p>
<dt>&bull;</p>
<dd> Release commit with the given &lt;tagname&gt; and populate changelog.</p>
<dt>
<dd> $ git release 0.1.0 -c</p>
<dt>&bull;</p>
<dd> Release commit with the given &lt;tagname&gt;, populate changelog, and push to specific remote.</p>
<dt>
<dd> $ git release 0.1.0 -r github -c</p>
<dt>
<dd></dl>
<h2>AUTHOR</h2>
<p> Written by Tj Holowaychuk &lt;<i>tj [at] vision-media.ca</i>&gt; Extended by David Hartmann &lt;<i>dh [at] tsl.io</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
