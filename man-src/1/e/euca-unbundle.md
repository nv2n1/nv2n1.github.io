---
title: "euca-unbundle(1)"
name: "euca-unbundle"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-unbundle/"
description: "euca-unbundle – Recreate an image from its bundled parts"
---

<h2>NAME</h2>
<p> euca-unbundle &#8211; Recreate an image from its bundled parts</p>
<h2>SYNOPSIS</h2>
<p> euca-unbundle <code>-m</code> FILE [-s DIR] [-d DIR] [-k FILE]</p>
<dl>
<dt>[&#8211;progress | <code>&#8211;no-progress]</code> [&#8211;region USER [at] REGION]</p>
<dd> [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</dl>
<h2>DESCRIPTION</h2>
<p> Recreate an image from its bundled parts</p>
<h2>DESCRIPTION</h2>
<p> The key used to unbundle the image must match a certificate that was used to bundle it.</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>-m</code> FILE, <code>&#8211;manifest</code> FILE</p>
<dd> the bundle&#8217;s manifest file (required)</p>
<dt><code>-s</code> DIR, <code>&#8211;source</code> DIR</p>
<dd> directory containing the bundled image parts (default: current directory)</p>
<dt><code>-d</code> DIR, <code>&#8211;destination</code> DIR</p>
<dd> where to place the unbundled image (default: current directory)</p>
<dt><code>-k</code> FILE, <code>&#8211;privatekey</code> FILE</p>
<dd> file containing the private key to decrypt the bundle with. This must match a certificate used when bundling the image.</p>
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
