---
title: "npm-explore(3)"
name: "npm-explore"
section: "3"
letter: "n"
url: "/docs/linux/man/3-npm-explore/"
description: "npm-explore — Browse an installed package"
---

<p><code>npm-explore</code> &#8212; Browse an installed package</p>
<h2>Synopsis</h2>
<pre>npm.commands.explore(args, callback)</pre>
<h2>Description</h2>
<p>Spawn a subshell in the directory of the installed package specified. If a command is specified, then it is run in the subshell, which then immediately terminates. Note that the package is <i>not</i> automatically rebuilt afterwards, so be sure to use <code>npm rebuild &lt;pkg&gt;</code> if you make any changes. The first element in the &#8216;args&#8217; parameter must be a package name. After that is the optional command, which can be any number of strings. All of the strings will be combined into one, space-delimited command. </p>
