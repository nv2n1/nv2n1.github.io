---
title: "sun2amd(8)"
name: "sun2amd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sun2amd/"
description: "sun2amd – converts Sun automount maps to Amd maps"
---

<p>sun2amd &#8211; converts Sun automount maps to Amd maps</p>
<h2>Synopsis</h2>
<p><code>sun2amd</code> [-hH] [-i infile] [-o outfile] </p>
<h2>Description</h2>
<p><code>sun2amd</code> is used to convert Sun style automount maps to Amd style automount maps. By default <code>sun2amd</code> reads from stdin and writes to stdout. </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Help</p>
<dt><code>-i</code></p>
<dd>Read Sun map information from specified file.</p>
<dt><code>-o</code></p>
<dd>Write Amd map information to specified file. </p>
</dl>
<h2>Example</h2>
<p>To convert a Sun automount file called auto_foo to an Amd file called auto.amd type: <code>sun2amd</code> -i auto_foo -o auto.amd </p>
<h2>Bugs</h2>
<p>* Can not convert master maps yet. * NFS is the only automount type currently supported. </p>
<pre><code>total_bug_count = number_found + 1;
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-automount/">automount</a>(8),</code> <code><a href="/docs/linux/man/8-amd/">amd</a>(8)</code> <i>Linux NFS and Automounter Administration</i> by Erez Zadok, ISBN 0-7821-2739-8, (Sybex, 2001). <i><a rel="nofollow" href="http://www.am-utils.org">http://www.am-utils.org</a></i> </p>
<h2>Author</h2>
<p>Daniel P. Ottavio <i>&lt;dottavio [at] ic.sunysb.edu&gt;</i></p>
