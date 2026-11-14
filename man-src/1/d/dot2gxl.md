---
title: "dot2gxl(1)"
name: "dot2gxl"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dot2gxl/"
description: "gxl2gv,gv2gxl – GXL-GV converters"
---

<h2 class="name">NAME</h2>
<p> gxl2gv,gv2gxl &#8211; GXL-GV converters </p>
<h2>SYNOPSIS</h2>
<p> <code>gxl2gv</code> [ <code>-gd?</code> ] [ <code>-o</code><i>outfile</i> ] [ <i>files</i> ]<br />
 <code>gv2gxl</code> [ <code>-gd?</code> ] [ <code>-o</code><i>outfile</i> ] [ <i>files</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>gxl2gv</code> converts between graphs represented in GXL and in the GV language. Unless a conversion type is specified using a flag, <code>gxl2gv</code> will deduce the type of conversion from the suffix of the input file, a &quot;.gv&quot; suffix causing a conversion from GV to GXL, and a &quot;.gxl&quot; suffix causing a conversion from GXL to GV. If no suffix is available, e.g. when the input is from a pipe, and no flags are used then <code>gxl2gv</code> assumes the type of the input file from its executable name so that <code>gxl2gv</code> converts from GXL to GV, and <code>gv2gxl</code> converts from GV to GXL. </p>
<p> GXL supports a much richer graph model than GV. <code>gxl2gv</code> will attempt to map GXL constructs into the analogous GV construct when this is possible. If not, the GXL information is stored as an attribute. The intention is that applying <code>gxl2gv|gv2gxl</code> is semantically equivalent to the identity operator.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><code>-g</code></p>
<dd> The command name and input file extensions are ignored, the input is taken as a GV file and a GXL file is generated.</p>
<dt><code>-d</code></p>
<dd> The command name and input file extensions are ignored, the input is taken as a GXL file and a GV file is generated.</p>
<dt><code>-?</code></p>
<dd> Prints usage information and exits.</p>
<dt><code>-o</code><i> outfile</i></p>
<dd> If specified, the output will be written into the file <i>outfile</i>. Otherwise, output is written to standard out.</dl>
<h2>OPERANDS</h2>
<p> The following operand is supported:</p>
<dl>
<dt><i>files</i></p>
<dd> Names of files containing 1 or more graphs in GXL or GV. If no <i>files</i> operand is specified, the standard input will be used.</dl>
<h2>RETURN CODES</h2>
<p> Both <code>gxl2gv</code> and <code>gv2gxl</code> return <code>0</code> if there were no problems during conversion; and non-zero if any error occurred.</p>
<h2>BUGS</h2>
<p> <code>gxl2gv</code> will only convert in one direction even if given multiple files with varying suffixes. </p>
<p> The conversion can only handle one graph per GXL file. </p>
<p> There are some GXL constructs which <code>gxl2gv</code> cannot handle.</p>
<h2>AUTHORS</h2>
<p> Krishnam Pericherla &lt;kp [at] research.att.com&gt;<br />
 Emden R. Gansner &lt;erg [at] research.att.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-dot/">dot</a>(1), <a href="/docs/linux/man/3-libgraph/">libgraph</a>(3), <a href="/docs/linux/man/3-libagraph/">libagraph</a>(3), <a href="/docs/linux/man/1-neato/">neato</a>(1), <a href="/docs/linux/man/1-twopi/">twopi</a>(1) </p>
<h2>Index</h2>
