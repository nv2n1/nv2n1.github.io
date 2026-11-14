---
title: "npm-bugs(3)"
name: "npm-bugs"
section: "3"
letter: "n"
url: "/docs/linux/man/3-npm-bugs/"
description: "npm-bugs — Bugs for a package in a web browser maybe"
---

<p><code>npm-bugs</code> &#8212; Bugs for a package in a web browser maybe</p>
<h2>Synopsis</h2>
<pre>npm.commands.bugs(package, callback)</pre>
<h2>Description</h2>
<p>This command tries to guess at the likely location of a package&#8217;s bug tracker URL, and then tries to open it using the <code>&#8211;browser</code> config param. Like other commands, the first parameter is an array. This command only uses the first element, which is expected to be a package name with an optional version number. This command will launch a browser, so this command may not be the most friendly for programmatic use. </p>
