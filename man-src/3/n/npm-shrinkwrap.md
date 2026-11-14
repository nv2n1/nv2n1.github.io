---
title: "npm-shrinkwrap(3)"
name: "npm-shrinkwrap"
section: "3"
letter: "n"
url: "/docs/linux/man/3-npm-shrinkwrap/"
description: "npm-shrinkwrap — programmatically generate package shrinkwrap file"
---

<p><code>npm-shrinkwrap</code> &#8212; programmatically generate package shrinkwrap file</p>
<h2>Synopsis</h2>
<pre>npm.commands.shrinkwrap(args, [silent,] callback)</pre>
<h2>Description</h2>
<p>This acts much the same ways as shrinkwrapping on the command-line. This command does not take any arguments, but &#8216;args&#8217; must be defined. Beyond that, if any arguments are passed in, npm will politely warn that it does not take positional arguments. If the &#8216;silent&#8217; parameter is set to true, nothing will be output to the screen, but the shrinkwrap file will still be written. Finally, &#8216;callback&#8217; is a function that will be called when the shrinkwrap has been saved. </p>
