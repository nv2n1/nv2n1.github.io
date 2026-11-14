---
title: "gst-convert(1)"
name: "gst-convert"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gst-convert/"
description: "gst-convert – Smalltalk syntax converter and beautifier"
---

<h2>NAME</h2>
<p> gst-convert &#8211; Smalltalk syntax converter and beautifier</p>
<h2>DESCRIPTION</h2>
<h3>Usage:</h3>
<dl>
<dt>
<dd> gst-convert [OPTION]&#8230; [INFILE [OUTFILE]] gst-convert [OPTION]&#8230; <code>-o</code>|&#8211;output OUTFILE INFILES</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> don&#8217;t show any message</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> print extra information while processing</p>
<dt><code>-f</code>, <code>&#8211;format</code>=<i>FORMAT</i></p>
<dd> convert from given input format (supported formats are gst, gst2, sif, squeak)</p>
<dt><code>-F</code>, <code>&#8211;output-format</code>=<i>FORMAT</i> convert to given output format (supported</p>
<dd> formats are gst, gst2, squeak)</p>
<dt><code>-C</code>, <code>&#8211;class</code>=<i>REGEX</i></p>
<dd> convert only classes matching REGEX</p>
<dt><code>-C</code>, <code>&#8211;class=</code>+REGEX</p>
<dd> in addition, convert classes matching REGEX</p>
<dt><code>-C</code>, <code>&#8211;class</code>=<i>-REGEX</i></p>
<dd> do not convert classes matching REGEX</p>
<dt><code>-c</code>, <code>&#8211;category</code>=<i>REGEX</i></p>
<dd> convert only classes whose category matches REGEX</p>
<dt><code>-c</code>, <code>&#8211;category=</code>+REGEX</p>
<dd> in addition, convert those whose category matches REGEX</p>
<dt><code>-c</code>, <code>&#8211;category</code>=<i>-REGEX</i></p>
<dd> do not convert classes whose category matches REGEX</p>
<dt><code>-r</code>, <code>&#8211;rule=</code>&#8216;CODE-&gt;REPL&#8217;</p>
<dd> look for CODE and replace it with REPL</p>
<dt><code>-o</code>, <code>&#8211;output</code> OUTFILE</p>
<dd> concatenate multiple input files into a single converted output file</p>
<dt><code>&#8211;help</code></p>
<dd> display this message and exit</p>
<dt><code>&#8211;version</code></p>
<dd> print version information and exit</dl>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gst-convert</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>gst-convert</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info gst</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
