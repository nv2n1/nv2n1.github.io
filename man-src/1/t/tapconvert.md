---
title: "tapconvert(1)"
name: "tapconvert"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tapconvert/"
description: "tapconvert – convert Twisted configurations from one format to another"
---

<h2>NAME</h2>
<p> tapconvert &#8211; convert Twisted configurations from one format to another</p>
<h2>SYNOPSIS</h2>
<p> <code>tapconvert -i </code><i>input</i> -o <i>output</i> [-f <i>input-type</i>] [-t <i>output-type</i>] [-d] [-e] </p>
<p> <code>tapconvert &#8211;help</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>&#8211;help</code> prints out a usage message to standard output.</p>
<dl>
<dt><code>&#8211;in</code>, <code>-i</code> <i>&lt;input file&gt;</i></p>
<dd> The name of the input configuration.</p>
<dt><code>&#8211;out</code>, <code>-o</code> <i>&lt;output file&gt;</i></p>
<dd> The name of the output configuration.</p>
<dt><code>&#8211;typein</code>, <code>-f</code> <i>&lt;input type&gt;</i></p>
<dd> The type of the input file. Can be either &#8216;guess&#8217;, &#8216;python&#8217;, &#8216;pickle&#8217;, &#8216;xml&#8217;, or &#8216;source&#8217;. Default is &#8216;guess&#8217;.</p>
<dt><code>&#8211;typeout</code>, <code>-t</code> <i>&lt;output type&gt;</i></p>
<dd> The type of the output file. Can be either &#8216;pickle&#8217;, &#8216;xml&#8217;, or &#8216;source&#8217;. Default is &#8216;source&#8217;.</p>
<dt><code>&#8211;decrypt</code>, <code>-d</code></p>
<dd> Decrypt the specified tap/aos/xml input file.</p>
<dt><code>&#8211;encrypt</code>, <code>-e</code></p>
<dd> Encrypt output file before writing.</p>
<dt><code>&#8211;version</code></p>
<dd> Output version information and exit.</dl>
<h2>AUTHOR</h2>
<p> Written by Moshe Zadka, based on tapconvert&#8217;s help messages</p>
<h2>REPORTING BUGS</h2>
<p> To report a bug, visit <i><a rel="nofollow" href="http://twistedmatrix.com/bugs/">http://twistedmatrix.com/bugs/</a></i></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2000-2012 Twisted Matrix Laboratories.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
