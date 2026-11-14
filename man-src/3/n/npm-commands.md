---
title: "npm-commands(3)"
name: "npm-commands"
section: "3"
letter: "n"
url: "/docs/linux/man/3-npm-commands/"
description: "npm-commands — npm commands"
---

<p><code>npm-commands</code> &#8212; npm commands</p>
<h2>Synopsis</h2>
<pre>npm.commands[&lt;command&gt;](args, callback)</pre>
<h2>Description</h2>
<p>npm comes with a full set of commands, and each of the commands takes a similar set of arguments. </p>
<p> In general, all commands on the command object take an <code>array</code> of positional argument <code>strings</code>. The last argument to any function is a callback. Some commands are special and take other optional arguments. </p>
<p> All commands have their own man page. See <code>man npm-&lt;command&gt;</code> for command-line usage, or <code>man 3 npm-&lt;command&gt;</code> for programmatic usage.</p>
<h2>See Also</h2>
<dl>
<dt>&bull;</p>
<dd>npm help index</p>
<dd>
