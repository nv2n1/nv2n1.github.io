---
title: "xgridfit(1)"
name: "xgridfit"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xgridfit/"
description: "xgridfit – a program for gridfitting, or \"hinting,\" TrueType fonts"
---

<h2>NAME</h2>
<p> <code>xgridfit </code> &#8211; a program for gridfitting, or &quot;hinting,&quot; TrueType fonts</p>
<h2>SYNOPSIS</h2>
<p> <code>xgridfit [options]</code> <i>file.</i>{<i>xgf</i> or <i>xml</i>}&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>Xgridfit</code> is a simple program that implements an XML-based language for gridfitting, or &quot;hinting,&quot; TrueType fonts. It compiles an XML source file into tables and instructions that relate to the gridfitting of glyphs. <code>Xgridfit</code> does not insert these elements into a font itself, but rather relies on FontForge, the Open Source font editor, to do this. </p>
<p> For each input file specified on the command line, the <code>xgridfit</code> command generates a script named <i>file.pe.</i> You may run this script in <i>FontForge</i> thus: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>fontforge -script file.pe </p>
<p> Alternatively, you can skip generation of a script file and pipe Xgridfit&#8217;s output directly to FontForge: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>xgridfit -f file.xgf </p>
<p> For more information about <code>Xgridfit,</code> point your browser to <i>file:///usr/share/doc/xgridfit/html/index.html</i> or <i><a rel="nofollow" href="http://xgridfit.sourceforge.net">http://xgridfit.sourceforge.net</a></i></p>
<h2>OPTIONS</h2>
<p> Note that options that set TrueType values can also be specified by &quot;default&quot; elements in the program file. However, command-line options always override these defaults.</p>
<dl>
<dt>-a value</p>
<dd> Size of TrueType stack (default is 128)</p>
<dt>-b value</p>
<dd> Delta Break value: formerly the maximum number of delta pairs that could be placed on the stack with a single push instruction. As of version 1.11 it approximates that behavior by setting -p option to twice the specified value. This option has no effect in Python mode (option -l py).</p>
<dt>-c yes|no</p>
<dd> Compile functions, control values, pre-program and maxp entries (default is &quot;yes&quot;)</p>
<dt>-C gray|black|white</p>
<dd> Use this color for rounded distances except where specified otherwise (default is &quot;gray&quot;).</p>
<dt>-d</p>
<dd> Run in debug mode. Output is <i>file.debug</i> rather than <i>file.pe</i></p>
<dt>-f</p>
<dd> Pipe generated script to FontForge. Do not save it in a file. This option overrides -O, and it is incompatible with -d, -S and -z.</p>
<dt>-g glyph</p>
<dd> Compile only the specified glyphs, ignoring all others. The argument is a list of one or more glyph names, delimited by plus signs (&quot;+&quot;). The list must contain no spaces.</p>
<dt>-G yes|no</p>
<dd> Include or omit at the beginning of each glyph program a function call that initializes variables used to track the graphics state. The default is &quot;yes.&quot; This option can be overridden with the init-graphics attribute on any glyph element.</p>
<dt>-h</p>
<dd> Display a help message and exit.</p>
<dt>-i file</p>
<dd> File to be input by generated script. Must have extension <i>.sfd</i> or <i>.ttf</i></p>
<dt>-l py|ff</p>
<dd> Whether the output of Xgridfit should be a Python script or one in the native FontForge scripting language. The default is <i>ff</i></p>
<dt>-o file</p>
<dd> File to be output by generated script. Must have extension <i>.sfd</i> or <i>.ttf</i></p>
<dt>-O file</p>
<dd> Name of script file to be output by Xgridfit, rather than the default, which replaces <i>.xgf</i> in the input file with <i>.pe</i></p>
<dt>-p value</p>
<dd> The number of values that can be pushed with a single PUSHB or PUSHW instruction. The default is 20, except in Python mode, where the default is 255.</p>
<dt>-q</p>
<dd> Run in quiet mode. Routine messages are suppressed</p>
<dt>-s value</p>
<dd> Maximum places in TrueType storage area. This area is used to store variables, and also Xgridfit&#8217;s own run-time data. The number must always be 24 or greater</p>
<dt>-S name</p>
<dd> Save script for each glyph in a separate file named <i>name_glyph-name.pe</i> or <i>name_glyph-name.debug</i></p>
<dt>-t value</p>
<dd> Maximum number of points in Twilight zone. The default is 25, but few fonts require so many</p>
<dt>-T file</p>
<dd> Name of a temporary file in which to store result of XInclude processing: the compiler and/or validator is run against this file. If this option is used, the file is not deleted after processing; if it is not used, the file (named by Xgridfit) is deleted. This option is ignored when the selected processor or validator has XInclude capabilities or when XInclude is not used. If a file by this name already exists, it is renamed as <i>file.bak</i> before processing.</p>
<dt>-v</p>
<dd> Print version number and exit</p>
<dt>-V</p>
<dd> Validate the Xgridfit program against a schema before compiling. Compilation is performed only if validation suceeds. By default xmllint is used for validation; run xgfconfig to choose another validator.</p>
<dt>-x</p>
<dd> Do not compile. Validation is performed if requested via the -V option.</p>
<dt>-z file</p>
<dd> When the -S option is present and the -o option or the &lt;outfile&gt; element has been used to make the output script save a font or FontForge source file, the output of the &lt;outfile&gt; script is saved in a separate script file. Xgridfit will supply a default name for this file, but this option lets you supply your own name.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/usr/share/xgridfit/lib/*.xsl</i></p>
<dd> All XSLT scripts of the <code>Xgridfit</code> program.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fontforge/">fontforge</a></code>(1), <code><a href="/docs/linux/man/1-xgfconfig/">xgfconfig</a></code>(1), <code><a href="/docs/linux/man/1-ttx2xgf/">ttx2xgf</a></code>(1), <code><a href="/docs/linux/man/1-xgfupdate/">xgfupdate</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> <code>xgridfit</code> was written by Peter Baker &lt;psb6m [at] virginia.edu&gt;. </p>
<p> This manual page was written by Kestutis Biliunas &lt;kebil [at] kaunas.init.lt&gt;, for the Debian project (but may be used by others). Revised and OPTIONS section added by P. Baker. </p>
<h2>Index</h2>
