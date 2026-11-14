---
title: "bin2obj(1)"
name: "bin2obj"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bin2obj/"
description: "bin2obj – The Free Pascal binary to pascal include file converter."
---

<h2>NAME</h2>
<p> bin2obj &#8211; The Free Pascal binary to pascal include file converter. </p>
<h2>SYNOPSIS</h2>
<p> <code>bin2obj [-aeouUz] -c constname infile</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>bin2obj</code> reads a binary file and converts it to a pascal typed constant declaration. The constant is an array of bytes (zero based), in which each byte has the value of the byte at the offset <i>index</i> in the file. (index is the index in the array). </p>
<h2>USAGE</h2>
<p> <code>bin2obj</code> accepts a filename of a binary file, and needs the name of a constant (use the <code>-c</code> option). The output goes to standard output by default. If no unitname is given, the output will be in the form of code which can be written to an include file. </p>
<h2>OPTIONS</h2>
<p> bin2obj has a small number of options to control its behaviour: </p>
<dl>
<dt><code>-a</code></p>
<dd> Write ASCII data instead of bytes. The constant array will be an array of char instead of an array of bytes. The bytes will be written as ASCII constants.</p>
<dt><code>-e key</code></p>
<dd> If this option is given, the data will be encrypted with <i>key</i> which is a string of 8 characters long.</p>
<dt><code>-h</code></p>
<dd> emit a small helptext.</p>
<dt><code>-o filename</code></p>
<dd> By default, the output goes to standard output (the screen). If this option is given, <code>bin2obj</code> will write the output to a file with name <i>filename</i> instead. This option is mandatory if the <code>-U</code> option is specified.</p>
<dt><code>-u [unitname]</code></p>
<dd> This option tells <code>bin2obj</code> to generate a unit. By default the output is just the declaration of the constant. If the unitname is not specified, <code>bin2obj</code> tries to determine it from the input filename.</p>
<dt><code>-U [unitname]</code></p>
<dd> The same as the <code>-u</code> option, only bin2obj will also call the compiler and compile the unit.</p>
<dt><code>-z</code></p>
<dd> Compress the data before creating the unit. zlib compression is used. </p>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>
<dd> <code><a href="/docs/linux/man/1-ppc386/">ppc386</a></code>(1) <code><a href="/docs/linux/man/1-data2inc/">data2inc</a></code>(1) </p>
</dl>
<h2>Index</h2>
