---

title: "euca-unbundle(1)"
name: "euca-unbundle"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-unbundle/"
description: "euca-unbundle – Recreate an image from its bundled parts"
---

<p> euca-unbundle &#8211; Recreate an image from its bundled parts</p>
<h2>SYNOPSIS</h2>
<p> euca-unbundle <code>-m</code> FILE [-s DIR] [-d DIR] [-k FILE]</p>
<dl>
<dt>[&#8211;progress | <code>&#8211;no-progress]</code> [&#8211;region USER [at] REGION]</dt>
<dd> [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</dd></dl>
<h2>DESCRIPTION</h2>
<p> Recreate an image from its bundled parts</p>
<h2>DESCRIPTION</h2>
<p> The key used to unbundle the image must match a certificate that was used to bundle it.</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>-m</code> FILE, <code>&#8211;manifest</code> FILE</dt>
<dd> the bundle&#8217;s manifest file (required)</dd>
<dt><code>-s</code> DIR, <code>&#8211;source</code> DIR</dt>
<dd> directory containing the bundled image parts (default: current directory)</dd>
<dt><code>-d</code> DIR, <code>&#8211;destination</code> DIR</dt>
<dd> where to place the unbundled image (default: current directory)</dd>
<dt><code>-k</code> FILE, <code>&#8211;privatekey</code> FILE</dt>
<dd> file containing the private key to decrypt the bundle with. This must match a certificate used when bundling the image.</dd>
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
