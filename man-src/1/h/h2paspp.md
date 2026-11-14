---
title: "h2paspp(1)"
name: "h2paspp"
section: "1"
letter: "h"
url: "/docs/linux/man/1-h2paspp/"
description: "h2paspp – Free Pascal h2pas preprocessor program."
---

<h2>NAME</h2>
<p> h2paspp &#8211; Free Pascal h2pas preprocessor program. </p>
<h2>SYNOPSIS</h2>
<p> <code>h2paspp [-doih] file1 &#8230; filen</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>h2paspp</code> reads one or more C header files and preprocesses them, writing the result to files with the same name as the originals as it goes along. It does not accept all preprocesser tokens of C, but takes care of the following preprocessor directives:</p>
<dl>
<dt><i>#define symbol</i></p>
<dd> Defines the new symbol <i>symbol</i> <code>te that macros are not supported.</code></p>
<dt><i>#if symbol</i></p>
<dd> The text following this directive is included if <i>symbol </i> is defined.</p>
<dt><i>#ifdef symbol</i></p>
<dd> The text following this directive is included if <i>symbol </i> is defined.</p>
<dt><i>#ifndef symbol</i></p>
<dd> The text following this directive is included if <i>symbol </i> is not defined.</p>
<dt><i>#include filename</i></p>
<dd> Include directives are removed, unless the <code>-I</code> option was given, in which case the include file is included and written to the output file.</p>
<dt><i>#undef symbol</i></p>
<dd> The symbol <i>symbol</i> is undefined. </p>
</dl>
<h2>USAGE</h2>
<p> <code>h2paspp</code> accepts one or more filenames and preprocesses them. It will read the input, and write output to a file with the same name unless the <code>-o</code> option is given, in which case the file is written to the specified file. Note that only one output filename can be given. </p>
<h2>OPTIONS</h2>
<p> h2paspp has a small number of options to control its behaviour: </p>
<dl>
<dt><code>-dsymbol</code></p>
<dd> Define the symbol <i>symbol</i> before processing is started.</p>
<dt><code>-h</code></p>
<dd> emit a small helptext.</p>
<dt><code>-ooutfile</code></p>
<dd> If this option is given, the output will be written to a file named <i>outfile</i> <code>te that only one output file can be given.</code> </p>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>
<dd> <code><a href="/docs/linux/man/1-ppc386/">ppc386</a></code>(1) <code><a href="/docs/linux/man/1-h2pas/">h2pas</a></code>(1) <code><a href="/docs/linux/man/1-cpp/">cpp</a></code>(1) </p>
</dl>
<h2>Index</h2>
