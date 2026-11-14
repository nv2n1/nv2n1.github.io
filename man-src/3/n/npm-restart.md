---
title: "npm-restart(3)"
name: "npm-restart"
section: "3"
letter: "n"
url: "/docs/linux/man/3-npm-restart/"
description: "npm-restart — Start a package"
---

<p><code>npm-restart</code> &#8212; Start a package</p>
<h2>Synopsis</h2>
<pre>npm.commands.restart(packages, callback)</pre>
<h2>Description</h2>
<p>This runs a package&#8217;s &quot;restart&quot; script, if one was provided. Otherwise it runs package&#8217;s &quot;stop&quot; script, if one was provided, and then the &quot;start&quot; script. </p>
<p> If no version is specified, then it restarts the &quot;active&quot; version. </p>
<p> npm can run tests on multiple packages. Just specify multiple packages in the <code>packages</code> parameter.</p>
<h2>See Also</h2>
<dl>
<dt>&bull;</p>
<dd>npm apihelp start</p>
<dt>&bull;</p>
<dd>npm apihelp stop</p>
<dd>
