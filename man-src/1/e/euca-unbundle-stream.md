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
<dt>[&#8211;image-size BYTES] [&#8211;sha1-digest HEX]</dt>
<dd> [&#8211;progress | <code>&#8211;no-progress]</code> [&#8211;region USER [at] REGION] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</dd></dl>
<h2>DESCRIPTION</h2>
<p> Recreate an image solely from its combined bundled parts without using a manifest</p>
<h2>DESCRIPTION</h2>
<p> Usually one would want to use euca-unbundle instead.</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>-i</code> FILE</dt>
<dd> file to read the bundle from (default: stdin)</dd>
<dt><code>-o</code> FILE</dt>
<dd> file to write the unbundled image to (default: stdout)</dd>
<dt><code>&#8211;enc-key</code> HEX</dt>
<dd> the symmetric key used to encrypt the bundle (required)</dd>
<dt><code>&#8211;enc-iv</code> HEX</dt>
<dd> the initialization vector used to encrypt the bundle (required)</dd>
<dt><code>&#8211;image-size</code> BYTES</dt>
<dd> verify the unbundled image is a certain size</dd>
<dt><code>&#8211;sha1-digest</code> HEX</dt>
<dd> verify the image&#8217;s contents against a SHA1 digest from its manifest file</dd>
<dt><code>&#8211;progress</code></dt>
<dd> show progress (the default when run interactively)</dd>
<dt><code>&#8211;no-progress</code></dt>
<dd> do not show progress (the default when run noninteractively)</dd>
<dt><code>&#8211;region</code> USER [at] REGION</dt>
<dd> region and/or user names to search when looking up config file data</dd>
<dt><code>&#8211;debug</code></dt>
<dd> show debugging output</dd>
<dt><code>&#8211;debugger</code></dt>
<dd> launch interactive debugger on error</dd>
<dt><code>&#8211;version</code></dt>
<dd> show the program&#8217;s version and exit</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit </dd>
</dl>
