---
title: "euca-unbundle-stream(1)"
name: "euca-unbundle-stream"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-unbundle-stream/"
description: "euca-unbundle-stream – Recreate an image solely from its combined bundled parts without using a manifest"
---

<h2>NAME</h2>
<p> euca-unbundle-stream &#8211; Recreate an image solely from its combined bundled parts without using a manifest</p>
<h2>SYNOPSIS</h2>
<p> euca-unbundle-stream [-i FILE] [-o FILE] <code>&#8211;enc-key</code> HEX <code>&#8211;enc-iv</code> HEX</p>
<dl>
<dt>[&#8211;image-size BYTES] [&#8211;sha1-digest HEX]</p>
<dd> [&#8211;progress | <code>&#8211;no-progress]</code> [&#8211;region USER [at] REGION] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</dl>
<h2>DESCRIPTION</h2>
<p> Recreate an image solely from its combined bundled parts without using a manifest</p>
<h2>DESCRIPTION</h2>
<p> Usually one would want to use euca-unbundle instead.</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>-i</code> FILE</p>
<dd> file to read the bundle from (default: stdin)</p>
<dt><code>-o</code> FILE</p>
<dd> file to write the unbundled image to (default: stdout)</p>
<dt><code>&#8211;enc-key</code> HEX</p>
<dd> the symmetric key used to encrypt the bundle (required)</p>
<dt><code>&#8211;enc-iv</code> HEX</p>
<dd> the initialization vector used to encrypt the bundle (required)</p>
<dt><code>&#8211;image-size</code> BYTES</p>
<dd> verify the unbundled image is a certain size</p>
<dt><code>&#8211;sha1-digest</code> HEX</p>
<dd> verify the image&#8217;s contents against a SHA1 digest from its manifest file</p>
<dt><code>&#8211;progress</code></p>
<dd> show progress (the default when run interactively)</p>
<dt><code>&#8211;no-progress</code></p>
<dd> do not show progress (the default when run noninteractively)</p>
<dt><code>&#8211;region</code> USER [at] REGION</p>
<dd> region and/or user names to search when looking up config file data</p>
<dt><code>&#8211;debug</code></p>
<dd> show debugging output</p>
<dt><code>&#8211;debugger</code></p>
<dd> launch interactive debugger on error</p>
<dt><code>&#8211;version</code></p>
<dd> show the program&#8217;s version and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit </p>
</dl>
<h2>Index</h2>
