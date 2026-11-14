---
title: "npm-rebuild(3)"
name: "npm-rebuild"
section: "3"
letter: "n"
url: "/docs/linux/man/3-npm-rebuild/"
description: "npm-rebuild — Rebuild a package"
---

<p><code>npm-rebuild</code> &#8212; Rebuild a package</p>
<h2>Synopsis</h2>
<pre>npm.commands.rebuild([packages,] callback)</pre>
<h2>Description</h2>
<p>This command runs the <code>npm build</code> command on each of the matched packages. This is useful when you install a new version of node, and must recompile all your C++ addons with the new binary. If no &#8216;packages&#8217; parameter is specify, every package will be rebuilt.</p>
<h2>Configuration</h2>
<p>See <code>npm help build</code></p>
