---
title: "slice2freezej(1)"
name: "slice2freezej"
section: "1"
letter: "s"
url: "/docs/linux/man/1-slice2freezej/"
description: "slice2freezej – Generates Freeze map and index classes in Java."
---

<h2 class="name">NAME</h2>
<p> slice2freezej &#8211; Generates Freeze map and index classes in Java.</p>
<h2>SYNOPSIS</h2>
<p> slice2freezej [options] [files] </p>
<h2>DESCRIPTION</h2>
<p> slice2java generates Freeze map and index classes in Java. </p>
<p> Full documentation for slice2freezej is available online at:<br />
 &quot;<a rel="nofollow" href="http://doc.zeroc.com/display/Ice/Using+a+Freeze+Map+in+Java">http://doc.zeroc.com/display/Ice/Using+a+Freeze+Map+in+Java</a>&quot;. </p>
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
<dt><code>&#8211;dict</code> <code>NAME,KEY,VALUE</code></p>
<dd>
 Generate a Freeze map class named NAME using KEY as key and VALUE as value. This option may be specified multiple times to generate several Freeze maps. NAME may be a scoped Java name, such as Demo.Struct1ObjectMap. KEY and VALUE represent Slice types and therefore must use Slice syntax, such as bool or Ice::Identity. </p>
<dt><code>&#8211;dict-index</code> <code>MAP[,MEMBER][,case-sensitive|case-insensitive]</code></p>
<dd>
 Add an index to the Freeze map named MAP. If MEMBER is specified, the map value type must be a structure or a class, and MEMBER must be the name of a member of that type. If MEMBER is not specified, the entire value is indexed. When the indexed member (or entire value) is a string, the index can be case-sensitive (default) or case-insensitive. </p>
<dt><code>&#8211;index</code> <code>CLASS,TYPE,MEMBER[,case-sensitive|case-insensitive]</code></p>
<dd>
 Generate an index class for a Freeze evictor. CLASS is the name of the index class to be generated. TYPE denotes the type of class to be indexed (objects of different classes are not included in this index). MEMBER is the name of the data member in TYPE to index. When MEMBER has type string, it is possible to specify whether the index is case-sensitive or not. The default is case-sensitive. </p>
<dt><code>&#8211;meta</code> <code>META</code></p>
<dd>
 Define the global metadata directive META. Using this option is equivalent to defining the global metadata META in each named Slice file, as well as in any file included by a named Slice file. Global metadata specified with &#8211;meta overrides any corresponding global metadata directive in the files being compiled. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-slice2cpp/">slice2cpp</a></code>(1), <code><a href="/docs/linux/man/1-slice2cs/">slice2cs</a></code>(1), <code><a href="/docs/linux/man/1-slice2freeze/">slice2freeze</a></code>(1), <code><a href="/docs/linux/man/1-slice2html/">slice2html</a></code>(1), <code><a href="/docs/linux/man/1-slice2java/">slice2java</a></code>(1), <code><a href="/docs/linux/man/1-slice2php/">slice2php</a></code>(1), <code><a href="/docs/linux/man/1-slice2py/">slice2py</a></code>(1), <code><a href="/docs/linux/man/1-slice2rb/">slice2rb</a></code>(1) </p>
<h2>Index</h2>
