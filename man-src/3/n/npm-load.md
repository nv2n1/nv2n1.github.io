---
title: "npm-load(3)"
name: "npm-load"
section: "3"
letter: "n"
url: "/docs/linux/man/3-npm-load/"
description: "npm-load — Load config settings"
---

<p><code>npm-load</code> &#8212; Load config settings</p>
<h2>Synopsis</h2>
<pre>npm.load(conf, cb)</pre>
<h2>Description</h2>
<p>npm.load() must be called before any other function call. Both parameters are optional, but the second is recommended. The first parameter is an object hash of command-line config params, and the second parameter is a callback that will be called when npm is loaded and ready to serve. The first parameter should follow a similar structure as the package.json config object. For example, to emulate the &#8211;dev flag, pass an object that looks like this:</p>
<dl>
<dd>
<pre>{
 &quot;dev&quot;: true
}</pre>
<dd></dl>
<p> For a list of all the available command-line configs, see <code>npm help config</code> </p>
