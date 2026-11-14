---
title: "stg-clone(1)"
name: "stg-clone"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-clone/"
description: "stg-clone – Make a local clone of a remote repository"
---

<h2 class="name">NAME</h2>
<p> stg-clone &#8211; Make a local clone of a remote repository </p>
<h2>SYNOPSIS</h2>
<pre>
<i>stg</i> clone &lt;repository&gt; &lt;dir&gt;
</pre>
<h2>DESCRIPTION</h2>
<p> Clone a git repository into the local directory &lt;dir&gt; (using <code><a href="/docs/linux/man/1-stg-clone/">stg-clone</a></code>(1)) and initialise the local branch &quot;master&quot;. </p>
<p> This operation is for example suitable to start working using the &quot;tracking branch&quot; workflow (see m[blue]<code>1</code>m[]<font SIZE="-2">[1]</font>). Other means to setup an StGit stack are <code><a href="/docs/linux/man/1-stg-init/">stg-init</a></code>(1) and the <i>&#8211;create</i> and <i>&#8211;clone</i> commands of <code><a href="/docs/linux/man/1-stg-branch/">stg-branch</a></code>(1). </p>
<p> The target directory &lt;dir&gt; will be created by this command, and must not already exist.</p>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> 1</p>
<dl>
<dt>
<dd> [set $man.base.url.for.relative.links]/stg</dl>
</dl>
<h2>Index</h2>
