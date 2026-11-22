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
<p><code>vss_strip</code> [<i>options</i>]<br/>
 A program for extracting file data from a file containing VSS headers. This program comes with the burp backup and restore package. </p>
<h2>Options</h2>
<dl>
<dt><code>-i</code> <code>path</code></dt>
<dd>Input file. If -i is not given, input will be read on stdin.</dd>
<dt><code>-o</code> <code>path</code></dt>
<dd>Output file. If -o is not given, output will be read on stdout.</dd>
<dt><code>-p</code></dt>
<dd>Print VSS header info.</dd>
<dt><code>-h|-?</code></dt>
<dd>Print help text and exit. </dd>
</dl>
<h2>Examples</h2>
<dl>
<dt><code>vss_strip -i infile -o outfile</code></dt>
<dd>Takes uncompressed infile, and extracts the file data to outfile.</dd>
<dt><code>zcat infile.gz | vss_strip</code></dt>
<dd>Takes the output of zcat as input, and outputs to stdout. </dd>
<h2>Bugs</h2>
<p>If you find bugs, please report them to the email list. See the website &lt;<a rel="nofollow" href="http://burp.grke.net/">http://burp.grke.net/</a>&gt; for details. </p>
<h2>Author</h2>
<p>The main author of Burp is Graham Keeling.</p>
<h2>Copyright</h2>
<p>See the LICENCE file included with the source distribution.</p>
</dl>