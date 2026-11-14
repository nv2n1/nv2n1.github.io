---
title: "npm-publish(3)"
name: "npm-publish"
section: "3"
letter: "n"
url: "/docs/linux/man/3-npm-publish/"
description: "npm-publish — Publish a package"
---

<p><code>npm-publish</code> &#8212; Publish a package</p>
<h2>Synopsis</h2>
<pre>npm.commands.publish([packages,] callback)</pre>
<h2>Description</h2>
<p>Publishes a package to the registry so that it can be installed by name. Possible values in the &#8216;packages&#8217; array are:</p>
<dl>
<dt>&bull;</p>
<dd><code>&lt;folder&gt;</code>: A folder containing a package.json file</p>
<dt>&bull;</p>
<dd><code>&lt;tarball&gt;</code>: A url or file path to a gzipped tar archive containing a single folder with a package.json file inside.</p>
<dd></dl>
<p> If the package array is empty, npm will try to publish something in the current working directory. </p>
<p> This command could fails if one of the packages specified already exists in the registry. Overwrites when the &quot;force&quot; environment variable is set.</p>
<h2>See Also</h2>
<dl>
<dt>&bull;</p>
<dd>npm help registry</p>
<dt>&bull;</p>
<dd>npm help adduser</p>
<dt>&bull;</p>
<dd>npm apihelp owner</p>
<dd>
