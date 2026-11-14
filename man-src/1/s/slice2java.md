---
title: "slice2java(1)"
name: "slice2java"
section: "1"
letter: "s"
url: "/docs/linux/man/1-slice2java/"
description: "slice2java – The Slice to Java compiler."
---

<h2 class="name">NAME</h2>
<p> slice2java &#8211; The Slice to Java compiler.</p>
<h2>SYNOPSIS</h2>
<p> slice2java [options] [files] </p>
<h2>DESCRIPTION</h2>
<p> slice2java compiles Slice files to Java. Full documentation for slice2java is available online at:<br />
 &quot;<a rel="nofollow" href="http://doc.zeroc.com/display/Ice/Using+the+Slice+Compiler+for+Java">http://doc.zeroc.com/display/Ice/Using+the+Slice+Compiler+for+Java</a>&quot;. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>
 Displays a help message. </p>
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
<dt><code>&#8211;tie</code></p>
<dd>
 Generate tie classes. </p>
<dt><code>&#8211;impl</code></p>
<dd>
 Generate sample implementation files. This option will not overwrite an existing file. </p>
<dt><code>&#8211;impl-tie</code></p>
<dd>
 Generate sample implementation files using tie classes. This option will not overwrite an existing file. </p>
<dt><code>&#8211;checksum</code> <code>CLASS</code></p>
<dd>
 Generate checksums for Slice definitions into the class CLASS. The given class name may optionally contain a package specifier. The generated class contains checksums for all of the Slice files being translated by this invocation of the compiler. </p>
<dt><code>&#8211;stream</code></p>
<dd>
 Generate streaming helper functions for Slice types. </p>
<dt><code>&#8211;meta</code> <code>META</code></p>
<dd>
 Define the global metadata directive META. Using this option is equivalent to defining the global metadata META in each named Slice file, as well as in any file included by a named Slice file. Global metadata specified with &#8211;meta overrides any corresponding global metadata directive in the files being compiled. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-slice2cpp/">slice2cpp</a></code>(1), <code><a href="/docs/linux/man/1-slice2cs/">slice2cs</a></code>(1), <code><a href="/docs/linux/man/1-slice2freeze/">slice2freeze</a></code>(1), <code><a href="/docs/linux/man/1-slice2freezej/">slice2freezej</a></code>(1), <code><a href="/docs/linux/man/1-slice2html/">slice2html</a></code>(1), <code><a href="/docs/linux/man/1-slice2php/">slice2php</a></code>(1), <code><a href="/docs/linux/man/1-slice2py/">slice2py</a></code>(1), <code><a href="/docs/linux/man/1-slice2rb/">slice2rb</a></code>(1) </p>
<h2>Index</h2>
