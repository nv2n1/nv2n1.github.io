---
title: "vss_strip(8)"
name: "vss_strip"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vss_strip/"
description: "vss_strip – program for extracting file data from a file containing VSS headers"
---

<p>vss_strip &#8211; program for extracting file data from a file containing VSS headers</p>
<h2>Synopsis</h2>
<p><code>vss_strip</code> [<i>options</i>]<br />
 A program for extracting file data from a file containing VSS headers. This program comes with the burp backup and restore package. </p>
<h2>Options</h2>
<dl>
<dt><code>-i</code> <code>path</code></p>
<dd>Input file. If -i is not given, input will be read on stdin.</p>
<dt><code>-o</code> <code>path</code></p>
<dd>Output file. If -o is not given, output will be read on stdout.</p>
<dt><code>-p</code></p>
<dd>Print VSS header info.</p>
<dt><code>-h|-?</code></p>
<dd>Print help text and exit. </p>
</dl>
<h2>Examples</h2>
<dl>
<dt><code>vss_strip -i infile -o outfile</code></p>
<dd>Takes uncompressed infile, and extracts the file data to outfile.</p>
<dt><code>zcat infile.gz | vss_strip</code></p>
<dd>Takes the output of zcat as input, and outputs to stdout. </p>
<h2>Bugs</h2>
<p>If you find bugs, please report them to the email list. See the website &lt;<a rel="nofollow" href="http://burp.grke.net/">http://burp.grke.net/</a>&gt; for details. </p>
<h2>Author</h2>
<p>The main author of Burp is Graham Keeling.</p>
<h2>Copyright</h2>
<p>See the LICENCE file included with the source distribution.</p>
