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
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>
 Displays a help message. </dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> Displays the compiler version. </dd>
<dt><code>-DNAME</code></dt>
<dd>
 Defines the preprocessor symbol NAME. </dd>
<dt><code>-DNAME=DEF</code></dt>
<dd>
 Defines the preprocessor symbol NAME with the value DEF. </dd>
<dt><code>-UNAME</code></dt>
<dd>
 Undefines the preprocessor symbol NAME. </dd>
<dt><code>-IDIR</code></dt>
<dd>
 Add the directory DIR to the search path for #include directives. </dd>
<dt><code>-E</code></dt>
<dd>
 Print the preprocessor output on stdout. </dd>
<dt><code>&#8211;output-dir</code> <code>DIR</code></dt>
<dd>
 Place the generated files into directory DIR. </dd>
<dt><code>-d</code>, <code>&#8211;debug</code></dt>
<dd>
 Print debug information showing the operation of the Slice parser. </dd>
<dt><code>&#8211;ice</code></dt>
<dd>
 Permit use of the normally reserved prefix Ice for identifiers. Use this option only when compiling the source code for the Ice run time. </dd>
<dt><code>&#8211;underscore</code></dt>
<dd>
 Permit use of underscores in Slice identifiers. </dd>
<dt><code>&#8211;tie</code></dt>
<dd>
 Generate tie classes. </dd>
<dt><code>&#8211;impl</code></dt>
<dd>
 Generate sample implementation files. This option will not overwrite an existing file. </dd>
<dt><code>&#8211;impl-tie</code></dt>
<dd>
 Generate sample implementation files using tie classes. This option will not overwrite an existing file. </dd>
<dt><code>&#8211;checksum</code> <code>CLASS</code></dt>
<dd>
 Generate checksums for Slice definitions into the class CLASS. The given class name may optionally contain a package specifier. The generated class contains checksums for all of the Slice files being translated by this invocation of the compiler. </dd>
<dt><code>&#8211;stream</code></dt>
<dd>
 Generate streaming helper functions for Slice types. </dd>
<dt><code>&#8211;meta</code> <code>META</code></dt>
<dd>
 Define the global metadata directive META. Using this option is equivalent to defining the global metadata META in each named Slice file, as well as in any file included by a named Slice file. Global metadata specified with &#8211;meta overrides any corresponding global metadata directive in the files being compiled. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-slice2cpp/">slice2cpp</a></code>(1), <code><a href="/docs/linux/man/1-slice2cs/">slice2cs</a></code>(1), <code><a href="/docs/linux/man/1-slice2freeze/">slice2freeze</a></code>(1), <code><a href="/docs/linux/man/1-slice2freezej/">slice2freezej</a></code>(1), <code><a href="/docs/linux/man/1-slice2html/">slice2html</a></code>(1), <code><a href="/docs/linux/man/1-slice2php/">slice2php</a></code>(1), <code><a href="/docs/linux/man/1-slice2py/">slice2py</a></code>(1), <code><a href="/docs/linux/man/1-slice2rb/">slice2rb</a></code>(1) </p>
