---
title: "npm-config(3)"
name: "npm-config"
section: "3"
letter: "n"
url: "/docs/linux/man/3-npm-config/"
description: "npm-config — Manage the npm configuration files"
---

<p><code>npm-config</code> &#8212; Manage the npm configuration files</p>
<h2>Synopsis</h2>
<pre>npm.commands.config(args, callback)
var val = npm.config.get(key)
npm.config.set(key, val)</pre>
<h2>Description</h2>
<p>This function acts much the same way as the command-line version. The first element in the array tells config what to do. Possible values are:</p>
<dl>
<dt>&bull;</p>
<dd><code>set</code></p>
<dd>Sets a config parameter. The second element in <code>args</code> is interpreted as the key, and the third element is interpreted as the value.</p>
<dt>&bull;</p>
<dd><code>get</code></p>
<dd>Gets the value of a config parameter. The second element in <code>args</code> is the key to get the value of.</p>
<dt>&bull;</p>
<dd><code>delete</code> (<code>rm</code> or <code>del</code>)</p>
<dd>Deletes a parameter from the config. The second element in <code>args</code> is the key to delete.</p>
<dt>&bull;</p>
<dd><code>list</code> (<code>ls</code>)</p>
<dd>Show all configs that aren&#8217;t secret. No parameters necessary.</p>
<dt>&bull;</p>
<dd><code>edit</code>:</p>
<dd>Opens the config file in the default editor. This command isn&#8217;t very useful programmatically, but it is made available.</p>
<dd></dl>
<p> To programmatically access npm configuration settings, or set them for the duration of a program, use the <code>npm.config.set</code> and <code>npm.config.get</code> functions instead.</p>
<h2>See Also</h2>
<dl>
<dt>&bull;</p>
<dd>npm apihelp npm</p>
<dd>
