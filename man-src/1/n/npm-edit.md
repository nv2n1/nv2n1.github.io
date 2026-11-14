---
title: "npm-edit(1)"
name: "npm-edit"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-edit/"
description: "npm-edit – Edit an installed package"
---

<h2 class="name">NAME</h2>
<p> <code>npm-edit</code> &#8211; Edit an installed package </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre>
npm edit &lt;pkg&gt;[/&lt;subpkg&gt;...]
</pre>
</dl>
<h3>Description</h3>
<p> Selects a (sub)dependency in the current working directory and opens the package folder in the default editor (or whatever you&#8217;ve configured as the npm <code>editor</code> config &#8212; see <code>npm-config</code> <i>npm-config</i>.) </p>
<p> After it has been edited, the package is rebuilt so as to pick up any changes in compiled packages. </p>
<p> For instance, you can do <code>npm install connect</code> to install connect into your package, and then <code>npm edit connect</code> to make a few changes to your locally installed copy.</p>
<h3>Configuration</h3>
<h3>editor</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Default: <code>EDITOR</code> environment variable if set, or <code>&quot;vi&quot;</code> on Posix, or <code>&quot;notepad&quot;</code> on Windows.</p>
<dt>&bull;</p>
<dd> Type: path </p>
</dl>
</dl>
<p> The command to run for <code>npm edit</code> or <code>npm config edit</code>.</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help folders</p>
<dt>&bull;</p>
<dd> npm help explore</p>
<dt>&bull;</p>
<dd> npm help install</p>
<dt>&bull;</p>
<dd> npm help config</p>
<dt>&bull;</p>
<dd> npm help npmrc </p>
</dl>
</dl>
<h2>Index</h2>
