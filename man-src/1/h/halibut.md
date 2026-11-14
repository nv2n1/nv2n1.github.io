---
title: "halibut(1)"
name: "halibut"
section: "1"
letter: "h"
url: "/docs/linux/man/1-halibut/"
description: "halibut – multi-format documentation formatting tool"
---

<h2>NAME</h2>
<p> <code>halibut</code> &#8211; multi-format documentation formatting tool</p>
<h2>SYNOPSIS</h2>
<pre><code>
halibut &amp;nbsp;
[options] &amp; nbsp;
file1.but &amp;nbsp;
[file2.but &amp; nbsp;...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>halibut</code> reads the given set of input files, assembles them into a document, and outputs that document in one or more formats. </p>
<p> The available command-line options can configure what formats Halibut should output in, and can also configure other things about the way Halibut works.</p>
<h2>OPTIONS</h2>
<p> The command-line options supported by <code>halibut</code> are:</p>
<dl>
<dt><code>&#8211;text</code>[<code>=</code><i>filename</i>]</p>
<dd> Makes Halibut generate an output file in plain text format. If the optional <i>filename</i> parameter is supplied, the output text file will be given that name. Otherwise, the name of the output text file will be as specified in the input files, or <code>output.txt</code> if none is specified at all.</p>
<dt><code>&#8211;html</code>[<code>=</code><i>filename</i>]</p>
<dd> Makes Halibut generate one or more output files in HTML format. If the optional <i>filename</i> parameter is supplied, there will be precisely one HTML output file with that name, containing the whole document. Otherwise, there may be one or more than one HTML file produced as output; this, and the file names, will be as specified in the input files, or given a set of default names starting with <code>Contents.html</code> if none is specified at all.</p>
<dt><code>&#8211;winhelp</code>[<code>=</code><i>filename</i>]</p>
<dd> Makes Halibut generate an output file in Windows Help format. If the optional <i>filename</i> parameter is supplied, the output help file will be given that name. Otherwise, the name of the output help file will be as specified in the input files, or <code>output.hlp</code> if none is specified at all.</p>
<dl>
<dt>
<dd>
<p> The output help file must have a name ending in <code>.hlp</code>; if it does not, <code>.hlp</code> will be added. A secondary contents file will be created alongside the main help file, with the same name except that it will end in <code>.cnt</code> (for example <code>output.cnt</code>, if the main file is <code>output.hlp</code>).</dl>
<dt><code>&#8211;man</code>[<code>=</code><i>filename</i>]</p>
<dd> Makes Halibut generate an output file in Unix <code>man</code> page format. If the optional <i>filename</i> parameter is supplied, the output <code>man</code> page will be given that name. Otherwise, the name of the output <code>man</code> page will be as specified in the input files, or <code>output.1</code> if none is specified at all.</p>
<dt><code>&#8211;info</code>[<code>=</code><i>filename</i>]</p>
<dd> Makes Halibut generate an <code>info</code> file. If the optional <i>filename</i> parameter is supplied, the output <code>info</code> file will be given that name. Otherwise, the name of the output <code>info</code> file will be as specified in the input files, or <code>output.info</code> if none is specified at all.</p>
<dl>
<dt>
<dd>
<p> By default, unless configured otherwise using the <code>
