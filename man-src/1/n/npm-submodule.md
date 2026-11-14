---
title: "npm-submodule(1)"
name: "npm-submodule"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-submodule/"
description: "npm-submodule — Add a package as a git submodule"
---

<h2>NAME</h2>
<p> <code>npm-submodule</code> &#8212; Add a package as a git submodule</p>
<h2>SYNOPSIS</h2>
<pre>
npm submodule &lt;pkg&gt;
</pre>
<h2>DESCRIPTION</h2>
<p> If the specified package has a git repository url in its package.json description, then this command will add it as a git submodule at <code>node_modules/&lt;pkg name&gt;</code>. </p>
<p> This is a convenience only. From then on, it&#8217;s up to you to manage updates by using the appropriate git commands. npm will stubbornly refuse to update, modify, or remove anything with a <code>.git</code> subfolder in it. </p>
<p> This command also does not install missing dependencies, if the package does not include them in its git repository. If <code>npm ls</code> reports that things are missing, you can either install, link, or submodule them yourself, or you can do <code>npm explore &lt;pkgname&gt; &#8212; npm install</code> to install the dependencies into the submodule folder.</p>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd> npm help package.json</p>
<dt>&bull;</p>
<dd> git help submodule</p>
<dt>
<dd>
</dl>
<h2>Index</h2>
