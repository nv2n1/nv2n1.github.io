---
title: "npm-install(3)"
name: "npm-install"
section: "3"
letter: "n"
url: "/docs/linux/man/3-npm-install/"
description: "npm-install — install a package programmatically"
---

<p><code>npm-install</code> &#8212; install a package programmatically</p>
<h2>Synopsis</h2>
<pre>npm.commands.install([where,] packages, callback)</pre>
<h2>Description</h2>
<p>This acts much the same ways as installing on the command-line. The &#8216;where&#8217; parameter is optional and only used internally, and it specifies where the packages should be installed to. The &#8216;packages&#8217; parameter is an array of strings. Each element in the array is the name of a package to be installed. Finally, &#8216;callback&#8217; is a function that will be called when all packages have been installed or when an error has been encountered. </p>
