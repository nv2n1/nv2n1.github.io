---
title: "slice2cpp(1)"
name: "slice2cpp"
section: "1"
letter: "s"
url: "/docs/linux/man/1-slice2cpp/"
description: "slice2cpp – The Slice to C++ compiler."
---

<h2 class="name">NAME</h2>
<p> slice2cpp &#8211; The Slice to C++ compiler.</p>
<h2>SYNOPSIS</h2>
<p> slice2cpp [options] [files] </p>
<h2>DESCRIPTION</h2>
<p> slice2cpp compiles Slice files to C++. </p>
<p> Full documentation for slice2cpp is available online at:<br />
 &quot;<a rel="nofollow" href="http://doc.zeroc.com/display/Ice/slice2cpp+Command-Line+Options">http://doc.zeroc.com/display/Ice/slice2cpp+Command-Line+Options</a>&quot;. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>
 Displays help message. </p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Displays the compiler version. </p>
<dt><code>-DNAME</code></p>
<dd>
 Defines the preprocessor symbol NAME. </p>
<dt><code>-DNAME=DEF</code></p>
<dd>
 Defines the preprocessor symbol NAME with the value DEF. </p>
<dt><code>-UNAME</code></p>
<dd>
 Undefines the preprocessor symbol NAME. </p>
<dt><code>-IDIR</code></p>
<dd>
 Add the directory DIR to the search path for #include directives. </p>
<dt><code>-E</code></p>
<dd>
 Print the preprocessor output on stdout. </p>
<dt><code>&#8211;output-dir</code> <code>DIR</code></p>
<dd>
 Place the generated files into directory DIR. </p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd>
 Print debug information showing the operation of the Slice parser. </p>
<dt><code>&#8211;ice</code></p>
<dd>
 Permit use of the normally reserved prefix Ice for identifiers. Use this option only when compiling the source code for the Ice run time. </p>
<dt><code>&#8211;underscore</code></p>
<dd>
 Permit use of underscores in Slice identifiers. </p>
<dt><code>&#8211;header-ext</code> <code>EXT</code></p>
<dd>
 Changes the file extension for the generated header files from the default h to EXT. </p>
<dt><code>&#8211;source-ext</code> <code>EXT</code></p>
<dd>
 Changes the file extension for the generated source files from the default cpp to EXT. </p>
<dt><code>&#8211;add-header</code> <code>HDR[,GUARD]</code></p>
<dd>
 This option adds an include directive for the specified header at the beginning of the generated source file (preceding any other include directives). If GUARD is specified, the include directive is protected by the specified guard. </p>
<dt><code>&#8211;include-dir</code> <code>DIR</code></p>
<dd>
 Modifies #include directives in source files to prepend the path name of each header file with the directory DIR. </p>
<dt><code>&#8211;impl</code></p>
<dd>
 Generate sample implementation files. This option will not overwrite an existing file. </p>
<dt><code>&#8211;depend</code></p>
<dd> Prints makefile dependency information to standard output. </p>
<dt><code>&#8211;dll-export</code> <code>SYMBOL</code></p>
<dd>
 Use SYMBOL to control DLL exports or imports. This option allows you to selectively export or import global symbols in the generated code. </p>
<dt><code>&#8211;checksum</code></p>
<dd>
 Generate checksums for Slice definitions. </p>
<dt><code>&#8211;stream</code></p>
<dd>
 Generate streaming helper functions for Slice types. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-slice2cs/">slice2cs</a></code>(1), <code><a href="/docs/linux/man/1-slice2freeze/">slice2freeze</a></code>(1), <code><a href="/docs/linux/man/1-slice2freezej/">slice2freezej</a></code>(1), <code><a href="/docs/linux/man/1-slice2html/">slice2html</a></code>(1), <code><a href="/docs/linux/man/1-slice2java/">slice2java</a></code>(1), <code><a href="/docs/linux/man/1-slice2php/">slice2php</a></code>(1), <code><a href="/docs/linux/man/1-slice2py/">slice2py</a></code>(1), <code><a href="/docs/linux/man/1-slice2rb/">slice2rb</a></code>(1) </p>
<h2>Index</h2>
