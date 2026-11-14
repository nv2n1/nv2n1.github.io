---
title: "npm-run-script(3)"
name: "npm-run-script"
section: "3"
letter: "n"
url: "/docs/linux/man/3-npm-run-script/"
description: "npm-run-script — Run arbitrary package scripts"
---

<p><code>npm-run-script</code> &#8212; Run arbitrary package scripts</p>
<h2>Synopsis</h2>
<pre>npm.commands.run-script(args, callback)</pre>
<h2>Description</h2>
<p>This runs an arbitrary command from a package&#8217;s &quot;scripts&quot; object. </p>
<p> It is used by the test, start, restart, and stop commands, but can be called directly, as well. </p>
<p> The &#8216;args&#8217; parameter is an array of strings. Behavior depends on the number of elements. If there is only one element, npm assumes that the element represents a command to be run on the local repository. If there is more than one element, then the first is assumed to be the package and the second is assumed to be the command to run. All other elements are ignored.</p>
<h2>See Also</h2>
<dl>
<dt>&bull;</p>
<dd>npm help scripts</p>
<dt>&bull;</p>
<dd>npm apihelp test</p>
<dt>&bull;</p>
<dd>npm apihelp start</p>
<dt>&bull;</p>
<dd>npm apihelp restart</p>
<dt>&bull;</p>
<dd>npm apihelp stop</p>
<dd>
