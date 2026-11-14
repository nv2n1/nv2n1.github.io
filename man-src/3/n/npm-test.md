---
title: "npm-test(3)"
name: "npm-test"
section: "3"
letter: "n"
url: "/docs/linux/man/3-npm-test/"
description: "npm-test — Test a package"
---

<p><code>npm-test</code> &#8212; Test a package</p>
<h2>Synopsis</h2>
<pre> npm.commands.test(packages, callback)</pre>
<h2>Description</h2>
<p>This runs a package&#8217;s &quot;test&quot; script, if one was provided. To run tests as a condition of installation, set the <code>npat</code> config to true. npm can run tests on multiple packages. Just specify multiple packages in the <code>packages</code> parameter. </p>
