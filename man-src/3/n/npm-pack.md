---
title: "npm-pack(3)"
name: "npm-pack"
section: "3"
letter: "n"
url: "/docs/linux/man/3-npm-pack/"
description: "npm-pack — Create a tarball from a package"
---

<p><code>npm-pack</code> &#8212; Create a tarball from a package</p>
<h2>Synopsis</h2>
<pre>npm.commands.pack([packages,] callback)</pre>
<h2>Description</h2>
<p>For anything that&#8217;s installable (that is, a package folder, tarball, tarball url, name@tag, name [at] version, or name), this command will fetch it to the cache, and then copy the tarball to the current working directory as <code>&lt;name&gt;-&lt;version&gt;.tgz</code>, and then write the filenames out to stdout. If the same package is specified multiple times, then the file will be overwritten the second time. If no arguments are supplied, then npm packs the current package folder. </p>
