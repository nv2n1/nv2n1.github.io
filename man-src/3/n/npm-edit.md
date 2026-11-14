---
title: "npm-edit(3)"
name: "npm-edit"
section: "3"
letter: "n"
url: "/docs/linux/man/3-npm-edit/"
description: "npm-edit — Edit an installed package"
---

<p><code>npm-edit</code> &#8212; Edit an installed package</p>
<h2>Synopsis</h2>
<pre>npm.commands.edit(package, callback)</pre>
<h2>Description</h2>
<p>Opens the package folder in the default editor (or whatever you&#8217;ve configured as the npm <code>editor</code> config &#8212; see <code>npm help config</code>.) After it has been edited, the package is rebuilt so as to pick up any changes in compiled packages. For instance, you can do <code>npm install connect</code> to install connect into your package, and then <code>npm.commands.edit([&quot;connect&quot;], callback)</code> to make a few changes to your locally installed copy. The first parameter is a string array with a single element, the package to open. The package can optionally have a version number attached. Since this command opens an editor in a new process, be careful about where and how this is used. </p>
