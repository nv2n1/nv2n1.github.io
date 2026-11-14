---
title: "npm-tag(3)"
name: "npm-tag"
section: "3"
letter: "n"
url: "/docs/linux/man/3-npm-tag/"
description: "npm-tag — Tag a published version"
---

<p><code>npm-tag</code> &#8212; Tag a published version</p>
<h2>Synopsis</h2>
<pre>npm.commands.tag(package [at] version, tag, callback)</pre>
<h2>Description</h2>
<p>Tags the specified version of the package with the specified tag, or the <code>&#8211;tag</code> config if not specified. The &#8216;package [at] version&#8217; is an array of strings, but only the first two elements are currently used. The first element must be in the form package [at] version, where package is the package name and version is the version number (much like installing a specific version). The second element is the name of the tag to tag this version with. If this parameter is missing or falsey (empty), the default froom the config will be used. For more information about how to set this config, check <code>man 3 npm-config</code> for programmatic usage or <code>man npm-config</code> for cli usage. </p>
