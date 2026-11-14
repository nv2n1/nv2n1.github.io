---
title: "ksflatten(1)"
name: "ksflatten"
section: "1"
letter: "k"
url: "/docs/linux/man/1-ksflatten/"
description: "ksflatten — flatten a kickstart file"
---

<h2>NAME</h2>
<p> ksflatten &#8212; flatten a kickstart file</p>
<h2>SYNOPSIS</h2>
<p> <code>ksflatten</code> [<code>-c</code> | <code>&#8211;config INFILE</code>] [<code>-o</code> | <code>&#8211;output OUTFILE</code>] [<code>-v</code> | <code>&#8211;version VERSION</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>ksflatten</code> is a program that takes an input kickstart file potentially containing includes and generates an output file with all the includes inlined.</p>
<h2>EXIT STATUS</h2>
<p> <code>ksflatten</code> returns 0 on success, and 1 if INFILE does not exist or there is an error parsing the kickstart file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;config INFILE</code></p>
<dd> The name of the input kickstart file.</p>
<dt><code>-o</code>, <code>&#8211;output OUTFILE</code></p>
<dd> Write the flattened kickstart file to OUTFILE, or stdout if no filename is given.</p>
<dt><code>-v</code>, <code>&#8211;version VERSION</code></p>
<dd> Use this version of kickstart syntax when processing the file, or the latest if no version is given.</dl>
<h2>SEE ALSO</h2>
<p> ksvalidator (1), ksverdiff (1) </p>
<h2>Index</h2>
