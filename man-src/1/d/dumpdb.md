---
title: "dumpdb(1)"
name: "dumpdb"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dumpdb/"
description: "dumpdb – The Freeze database inspector."
---

<h2 class="name">NAME</h2>
<p> dumpdb &#8211; The Freeze database inspector.</p>
<h2>SYNOPSIS</h2>
<p> dumpdb [options] dbenv db </p>
<h2>DESCRIPTION</h2>
<p> The FreezeScript tool dumpdb is used to examine a Freeze database. Its simplest invocation displays every record of the database, but the tool also supports more selective activities. In fact, dumpdb supports a scripted mode that shares many of the same XML descriptors as transformdb, enabling sophisticated filtering and reporting. Full documentation for dumpdb is available online at:<br />
 &quot;<a rel="nofollow" href="http://doc.zeroc.com/display/Ice/Using+dumpdb">http://doc.zeroc.com/display/Ice/Using+dumpdb</a>&quot;. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>
 Displays help message. </p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Displays the Ice version. </p>
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
<dt><code>&#8211;load</code> <code>SLICE</code></p>
<dd>
 Loads the Slice definitions contained in the file SLICE. This option may be specified multiple times if several files must be loaded. However, it is the user&#8217;s responsibility to ensure that duplicate definitions do not occur (which is possible when two files are loaded that share a common include file). One strategy for avoiding duplicate definitions is to load a single Slice file that contains only #include statements for each of the Slice files to be loaded. No duplication is possible in this case if the included files use include guards correctly. </p>
<dt><code>&#8211;key</code> <code>TYPE</code></p>
<dd>
<dt><code>&#8211;value</code> <code>TYPE</code></p>
<dd>
 Specifies the Slice type of the database key and value. If these options are not specified, and the -e option is not used, dumpdb obtains type information from the Freeze catalog. </p>
<dt><code>-e</code></p>
<dd>
 Indicates that a Freeze evictor database is being examined. As a convenience, this option automatically sets the database key and value types to those appropriate for the Freeze evictor, and therefore the &#8211;key and &#8211;value options are not necessary. Specifically, the key type of a Freeze evictor database is Ice::Identity, and the value type is Freeze::ObjectRecord. The latter is defined in the Slice file Freeze/EvictorStorage.ice, however this file does not need to be explicitly loaded. If this option is not specified, and the &#8211;key and &#8211;value options are not used, dumpdb obtains type information from the Freeze catalog. </p>
<dt><code>-o</code> <code>FILE</code></p>
<dd>
 Create a file named FILE containing sample descriptors for the loaded Slice definitions. If type information is not specified, dumpdb obtains it from the Freeze catalog. If the &#8211;select option is used, its expression is included in the sample descriptors. Database traversal does not occur when the -o option is used. </p>
<dt><code>-f</code> <code>FILE</code></p>
<dd>
 Execute the descriptors in the file named FILE. The file&#8217;s &lt;database&gt; descriptor specifies the key and value types, therefore it is not necessary to supply type information. </p>
<dt><code>&#8211;select</code> <code>EXPR</code></p>
<dd>
 Only display those records for which the expression EXPR is true. The expression can refer to the symbols key and value. </p>
<dt><code>-c</code>, <code>&#8211;catalog</code></p>
<dd>
 Display information about the databases in an environment, or about a particular database. This option presents the type information contained in the Freeze catalog. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-transformdb/">transformdb</a></code>(1) </p>
<h2>Index</h2>
