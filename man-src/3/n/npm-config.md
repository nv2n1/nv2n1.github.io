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
<dt>&bull;</dt>
<dd><code>set</code></dd>
<dd>Sets a config parameter. The second element in <code>args</code> is interpreted as the key, and the third element is interpreted as the value.</dd>
<dt>&bull;</dt>
<dd><code>get</code></dd>
<dd>Gets the value of a config parameter. The second element in <code>args</code> is the key to get the value of.</dd>
<dt>&bull;</dt>
<dd><code>delete</code> (<code>rm</code> or <code>del</code>)</dd>
<dd>Deletes a parameter from the config. The second element in <code>args</code> is the key to delete.</dd>
<dt>&bull;</dt>
<dd><code>list</code> (<code>ls</code>)</dd>
<dd>Show all configs that aren&#8217;t secret. No parameters necessary.</dd>
<dt>&bull;</dt>
<dd><code>edit</code>:</dd>
<dd>Opens the config file in the default editor. This command isn&#8217;t very useful programmatically, but it is made available.</dd>
<dd></dd></dl>
<p> To programmatically access npm configuration settings, or set them for the duration of a program, use the <code>npm.config.set</code> and <code>npm.config.get</code> functions instead.</p>
<h2>See Also</h2>
<dl>
<dt>&bull;</dt>
<dd>npm apihelp npm</dd>
<dd>
</dd></dl>