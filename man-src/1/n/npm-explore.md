---

title: "npm-explore(1)"
name: "npm-explore"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-explore/"
description: "npm-explore – Browse an installed package"
---

<p> <code>npm-explore</code> &#8211; Browse an installed package </p>
<h3>Synopsis</h3>
<dl>
<dt>
</dt><dd>
<pre>
npm explore &lt;pkg&gt; [ -- &lt;command&gt;]
</pre>
</dd></dl>
<h3>Description</h3>
<p> Spawn a subshell in the directory of the installed package specified. </p>
<p> If a command is specified, then it is run in the subshell, which then immediately terminates. </p>
<p> This is particularly handy in the case of git submodules in the <code>node_modules</code> folder: </p>
<dl>
<dt>
</dt><dd>
<pre>
npm explore some-dependency -- git pull origin master
</pre>
</dd></dl>
<p> Note that the package is <i>not</i> automatically rebuilt afterwards, so be sure to use <code>npm rebuild &lt;pkg&gt;</code> if you make any changes.</p>
<h3>Configuration</h3>
<h3>shell</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> Default: SHELL environment variable, or &quot;bash&quot; on Posix, or &quot;cmd&quot; on Windows</dd>
<dt>&bull;</dt>
<dd> Type: path </dd>
</dl>
</dl>
<p> The shell to run for the <code>npm explore</code> command.</p>
<h3>See Also</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> npm help folders</dd>
<dt>&bull;</dt>
<dd> npm help edit</dd>
<dt>&bull;</dt>
<dd> npm help rebuild</dd>
<dt>&bull;</dt>
<dd> npm help build</dd>
<dt>&bull;</dt>
<dd> npm help install </dd>
</dl>
</dl>
