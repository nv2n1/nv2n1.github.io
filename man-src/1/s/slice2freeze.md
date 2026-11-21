---

title: "slice2freeze(1)"
name: "slice2freeze"
section: "1"
letter: "s"
url: "/docs/linux/man/1-slice2freeze/"
description: "slice2freeze – Generates Freeze map and index classes in C++."
---

<p> slice2freeze [options] [files] </p>
<p> slice2freeze generates Freeze map and index classes in C++. </p>
<p> Full documentation for slice2freeze is available online at:<br />
 &quot;<a rel="nofollow" href="http://doc.zeroc.com/pages/viewpage.action?pageId=5048540">http://doc.zeroc.com/pages/viewpage.action?pageId=5048540</a>&quot;. </p>
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
<dt><code>&#8211;header-ext</code> <code>EXT</code></dt>
<dd>
 Changes the file extension for the generated header files from the default h to EXT. </dd>
<dt><code>&#8211;source-ext</code> <code>EXT</code></dt>
<dd>
 Changes the file extension for the generated source files from the default cpp to EXT. </dd>
<dt><code>&#8211;add-header</code> <code>HDR[,GUARD]</code></dt>
<dd>
 This option adds an include directive for the specified header at the beginning of the generated source file (preceding any other include directives). If GUARD is specified, the include directive is protected by the specified guard. </dd>
<dt><code>&#8211;include-dir</code> <code>DIR</code></dt>
<dd>
 Modifies #include directives in source files to prepend the path name of each header file with the directory DIR. </dd>
<dt><code>&#8211;dll-export</code> <code>SYMBOL</code></dt>
<dd>
 Use SYMBOL to control DLL exports or imports. This option allows you to selectively export or import global symbols in the generated code. </dd>
<dt><code>&#8211;dict</code> <code>NAME,KEY,VALUE[,sort[,COMPARE]]</code></dt>
<dd>
 Generate a Freeze map class named NAME using KEY as key and VALUE as value. This option may be specified multiple times to generate several Freeze maps. NAME may be a scoped C++ name, such as Demo::Struct1ObjectMap. KEY and VALUE represent Slice types and therefore must use Slice syntax, such as bool or Ice::Identity. By default, keys are sorted using their binary Ice-encoded representation. Include sort to sort with the COMPARE functor class. If COMPARE is not specified, the default value is std::less&lt;KEY&gt;. </dd>
<dt><code>&#8211;dict-index</code> <code>MAP[,MEMBER]</code> <code>[,case-sensitive|case-insensitive][,sort[,COMPARE]]</code></dt>
<dd>
 Add an index to the Freeze map named MAP. If MEMBER is specified, the map value type must be a structure or a class, and MEMBER must be a member of this structure or class. </dd>
<dt><code>&#8211;index</code> <code>CLASS,TYPE,MEMBER</code> <code>[,case-sensitive|case-insensitive]</code></dt>
<dd>
 Generate an index class for a Freeze evictor. CLASS is the name of the class to be generated. TYPE denotes the type of class to be indexed (objects of different classes are not included in this index). MEMBER is the name of the data member in TYPE to index. When MEMBER has type string, it is possible to specify whether the index is case-sensitive or not. The default is case-sensitive. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-slice2cpp/">slice2cpp</a></code>(1), <code><a href="/docs/linux/man/1-slice2cs/">slice2cs</a></code>(1), <code><a href="/docs/linux/man/1-slice2freezej/">slice2freezej</a></code>(1), <code><a href="/docs/linux/man/1-slice2html/">slice2html</a></code>(1), <code><a href="/docs/linux/man/1-slice2java/">slice2java</a></code>(1), <code><a href="/docs/linux/man/1-slice2php/">slice2php</a></code>(1), <code><a href="/docs/linux/man/1-slice2py/">slice2py</a></code>(1), <code><a href="/docs/linux/man/1-slice2rb/">slice2rb</a></code>(1) </p>
