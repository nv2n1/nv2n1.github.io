---
title: "data2inc(1)"
name: "data2inc"
section: "1"
letter: "d"
url: "/docs/linux/man/1-data2inc/"
description: "data2inc – Free Pascal binary to pascal include file converter."
---

<h2>NAME</h2>
<p> data2inc &#8211; Free Pascal binary to pascal include file converter. </p>
<h2>SYNOPSIS</h2>
<p> <code>data2inc [-ABSVH] msgfile [incfile] [constname]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>data2inc</code> reads a binary or text file and converts it to a pascal typed constant declaration. The constant is an array of characters (zero based), in which each character&#8217;s ascii value is the value of the byte at the offset <i>index</i> in the binary file. (index is the index in the array). If the input file is a text file, options will be read from the file and an output file will be generated according to the options encountered. </p>
<h2>USAGE</h2>
<p> <code>data2inc</code> with the <code>-B</code> option accepts a filename of a binary file, and needs the name of an include file and constant name. The output is written to <code>incfile</code> The name of the constant <code>constname</code> is mandatory for a binary file. </p>
<p> <code>data2inc</code> without <code>-B </code> option takes the name of a message description file as input. It will process the message file and write the output as described in the message file to <i>incfile</i> </p>
<h2>OPTIONS</h2>
<p> data2inc has a small number of options to control its behaviour: </p>
<dl>
<dt><code>-A</code></p>
<dd> Write bytes instead of characters. The constant array will be an array of byte instead of an array of char.</p>
<dt><code>-B</code></p>
<dd> If this option is given, the <i>msgfile</i> will be treated as a binary file.</p>
<dt><code>-H</code></p>
<dd> emit a small helptext.</p>
<dt><code>-S </code></p>
<dd> <code>data2inc</code> will write the output as an array of strings, or a 2 dimensional array of characters.</p>
<dt><code>-V</code></p>
<dd> Show the version number and exit. </p>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>
<dd> <code><a href="/docs/linux/man/1-ppc386/">ppc386</a></code>(1) <code><a href="/docs/linux/man/1-bin2obj/">bin2obj</a></code>(1) </p>
</dl>
<h2>Index</h2>
