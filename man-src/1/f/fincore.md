---
title: "fincore(1)"
name: "fincore"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fincore/"
description: "fincore – count pages of file contents in core"
---

<h2 class="name">NAME</h2>
<p> fincore &#8211; count pages of file contents in core </p>
<h2>SYNOPSIS</h2>
<p> <code>fincore</code> [options] <i>file</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>fincore</code> counts pages of file contents being resident in memory (in core), and reports the numbers. If an error occurs during counting, then an error message is printed to the stderr and <code>fincore</code> continues processing the rest of files listed in a command line. </p>
<p> The default output is subject to change. So whenever possible, you should avoid using default outputs in your scripts. Always explicitly define expected columns by using <code>&#8211;output</code> <i>columns-list</i> in environments where a stable output is required.</p>
<h2>OPTIONS</h2>
<p> <code>-n</code>, <code>&#8211;noheadings</code></p>
<dl>
<dt>
<dd> Do not print a header line in status output.</dl>
<p> <code>-b</code>, <code>&#8211;bytes</code></p>
<dl>
<dt>
<dd> Print the SIZE column in bytes rather than in a human-readable format.</dl>
<p> <code>-o</code>, <code>&#8211;output</code> <i>list</i></p>
<dl>
<dt>
<dd> Define output columns. See the <code>&#8211;help</code> output to get a list of the currently supported columns. The default list of columns may be extended if <i>list</i> is specified in the format <i>+list</i>.</dl>
<p> <code>-r</code>, <code>&#8211;raw</code></p>
<dl>
<dt>
<dd> Produce output in raw format. All potentially unsafe characters are hex-escaped (
