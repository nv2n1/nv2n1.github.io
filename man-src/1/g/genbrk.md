---
title: "genbrk(1)"
name: "genbrk"
section: "1"
letter: "g"
url: "/docs/linux/man/1-genbrk/"
description: "genbrk – Compiles ICU break iteration rules source files into binary data files"
---

<h2 class="name">NAME</h2>
<p> <code>genbrk</code> &#8211; Compiles ICU break iteration rules source files into binary data files </p>
<h2>SYNOPSIS</h2>
<p> <code>genbrk</code> [ <code>-h</code>, <code>-?</code>, <code>&#8211;help</code> ] [ <code>-V</code>, <code>&#8211;version</code> ] [ <code>-c</code>, <code>&#8211;copyright</code> ] [ <code>-v</code>, <code>&#8211;verbose</code> ] [ <code>-d</code>, <code>&#8211;destdir</code><i> destination</i> ] [ <code>-i</code>, <code>&#8211;icudatadir</code><i> directory</i> ] <code>-r</code>, <code>&#8211;rules</code><i> rule-file</i> <code>-o</code>, <code>&#8211;out</code><i> output-file</i></p>
<h2>DESCRIPTION</h2>
<p> <code>genbrk</code> reads the break (boundary) rule source code from <i>rule-file</i> and creates a break iteration data file. Normally this data file has the <code>.brk</code> extension. </p>
<p> The details of the rule syntax can be found in ICU&#8217;s User Guide.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>-?</code>, <code>&#8211;help</code></p>
<dd> Print help about usage and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print the version of <code>genbrk</code> and exit.</p>
<dt><code>-c</code>, <code>&#8211;copyright</code></p>
<dd> Embeds the standard ICU copyright into the <i>output-file</i>.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Display extra informative messages during execution.</p>
<dt><code>-d</code>, <code>&#8211;destdir</code><i> destination</i></p>
<dd> Set the destination directory of the <i>output-file</i> to <i>destination</i>.</p>
<dt><code>-i</code>, <code>&#8211;icudatadir</code><i> directory</i></p>
<dd> Look for any necessary ICU data files in <i>directory</i>. For example, the file <code>pnames.icu</code> must be located when ICU&#8217;s data is not built as a shared library. The default ICU data directory is specified by the environment variable <code>ICU_DATA</code>. Most configurations of ICU do not require this argument.</p>
<dt><code>-r</code>, <code>&#8211;rules</code><i> rule-file</i></p>
<dd> The source file to read.</p>
<dt><code>-o</code>, <code>&#8211;out</code><i> output-file</i></p>
<dd> The output data file to write.</dl>
<h2>CAVEATS</h2>
<p> When the <i>rule-file</i> contains a byte order mark (BOM) at the beginning of the file, which is the Unicode character <code>U+FEFF,</code> then the <i>rule-file</i> is interpreted as Unicode. Without the BOM, the file is interpreted in the current operating system default codepage. In order to eliminate any ambiguity of the encoding for how the <i>rule-file</i> was written, it is recommended that you write this file in UTF-8 with the BOM.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>ICU_DATA</code></p>
<dd> Specifies the directory containing ICU data. Defaults to <code>${prefix}/share/icu/70.1/</code>. Some tools in ICU depend on the presence of the trailing slash. It is thus important to make sure that it is present if <code>ICU_DATA</code> is set.</dl>
<h2>AUTHORS</h2>
<p> George Rhoten<br />
 Andy Heninger</p>
<h2>VERSION</h2>
<p> 1.0</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2005 International Business Machines Corporation and others</p>
<h2>SEE ALSO</h2>
<p> <code><a rel="nofollow" href="http://www.icu-project.org/userguide/boundaryAnalysis.html">http://www.icu-project.org/userguide/boundaryAnalysis.html</a></code> </p>
<h2>Index</h2>
