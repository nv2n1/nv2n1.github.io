---
title: "node-gyp(1)"
name: "node-gyp"
section: "1"
letter: "n"
url: "/docs/linux/man/1-node-gyp/"
description: "node-gyp — native addon build tool for node"
---

<h2 class="name">NAME</h2>
<p> <code>node-gyp</code> &#8212; native addon build tool for node </p>
<h2>SYNOPSIS</h2>
<pre>
node-gyp &lt;command&gt; [args]
</pre>
<h2>DESCRIPTION</h2>
<p> <code>node-gyp</code> is a cross-platform command-line tool for compiling native addon modules for Node.js, taking away the pain of dealing with the various differences in build platforms. It is the replacement to the <code>node-waf</code> program, which is removed since node 0.8. Native addons still using a <code>wscript</code> file should definitely add a <code>binding.gyp</code> file to support the latest versions of node. </p>
<p> Multiple target versions of node are supported (from node 0.6 to the next released version), regardless of what version of node is actually installed on your system; <code>node-gyp</code> downloads the necessary development files for the target version.</p>
<h2>COMMANDS</h2>
<dl>
<dt>&bull;</p>
<dd> <code>build</code> Invokes <code>make</code>/<code>msbuild.exe</code> and builds the native addon</p>
<dt>&bull;</p>
<dd> <code>clean</code> Removes any the <code>build</code> dir if it exists</p>
<dt>&bull;</p>
<dd> <code>configure</code> Generates project build files for the current platform</p>
<dt>&bull;</p>
<dd> <code>rebuild</code> Runs <code>clean</code>, <code>configure</code> and <code>build</code> all in a row</p>
<dt>&bull;</p>
<dd> <code>install</code> &lt;version&gt; Installs node development header files for the given version</p>
<dt>&bull;</p>
<dd> <code>list</code> Lists the currently installed node development file versions</p>
<dt>&bull;</p>
<dd> <code>remove</code> &lt;version&gt; Removes the node development header files for the given version</p>
<dt>
<dd></dl>
<h2>SEE ALSO</h2>
<p> README.md </p>
<h2>Index</h2>
