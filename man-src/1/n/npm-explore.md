---
title: "npm-explore(1)"
name: "npm-explore"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-explore/"
description: "npm-explore – Browse an installed package"
---

<h2 class="name">NAME</h2>
<p> <code>npm-explore</code> &#8211; Browse an installed package </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre>
npm explore &lt;pkg&gt; [ -- &lt;command&gt;]
</pre>
</dl>
<h3>Description</h3>
<p> Spawn a subshell in the directory of the installed package specified. </p>
<p> If a command is specified, then it is run in the subshell, which then immediately terminates. </p>
<p> This is particularly handy in the case of git submodules in the <code>node_modules</code> folder: </p>
<dl>
<dt>
<dd>
<pre>
npm explore some-dependency -- git pull origin master
</pre>
</dl>
<p> Note that the package is <i>not</i> automatically rebuilt afterwards, so be sure to use <code>npm rebuild &lt;pkg&gt;</code> if you make any changes.</p>
<h3>Configuration</h3>
<h3>shell</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Default: SHELL environment variable, or &quot;bash&quot; on Posix, or &quot;cmd&quot; on Windows</p>
<dt>&bull;</p>
<dd> Type: path </p>
</dl>
</dl>
<p> The shell to run for the <code>npm explore</code> command.</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help folders</p>
<dt>&bull;</p>
<dd> npm help edit</p>
<dt>&bull;</p>
<dd> npm help rebuild</p>
<dt>&bull;</p>
<dd> npm help build</p>
<dt>&bull;</p>
<dd> npm help install </p>
</dl>
</dl>
<h2>Index</h2>
