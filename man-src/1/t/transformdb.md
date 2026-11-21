---
title: "transformdb(1)"
name: "transformdb"
section: "1"
letter: "t"
url: "/docs/linux/man/1-transformdb/"
description: "transformdb – The Freeze database migration tool."
---

<h2 class="name">NAME</h2>
<p> transformdb &#8211; The Freeze database migration tool.</p>
<h2>SYNOPSIS</h2>
<p> transformdb -o FILE [-i] [slice-options] [type-options]</p>
<dl>
<dt>
</dt><dd> Generates descriptors in FILE for a database. </dd>
</dl>
<p> transformdb -o FILE [-i] [slice-options] DBENV</p>
<dl>
<dt>
</dt><dd> Generates descriptors in FILE for all databases in the environment DBENV. </dd>
</dl>
<p> transformdb [options] [slice-options] [type-options] DBENV DB NEWDBENV</p>
<dl>
<dt>
</dt><dd> Transform the database DB in the environment DBENV. A database of the same name is created in the environment NEWDBENV. </dd>
</dl>
<p> transformdb [options] [slice-options] DBENV NEWDBENV</p>
<dl>
<dt>
</dt><dd> Transform all databases from the environment DBENV into the environment NEWDBENV. </dd>
</dl>
<h2>DESCRIPTION</h2>
<p> The FreezeScript tool transformdb migrates a database created by a Freeze map or evictor. It accomplishes this by comparing the &quot;old&quot; Slice definitions (i.e., the ones that describe the current contents of the database) with the &quot;new&quot; Slice definitions, and making whatever modifications are necessary to ensure that the transformed database is compatible with the new definitions. Full documentation for transformdb is available online at:<br />
 &quot;<a rel="nofollow" href="http://doc.zeroc.com/display/Ice/Using+transformdb">http://doc.zeroc.com/display/Ice/Using+transformdb</a>&quot;. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>
 Displays a help message. </dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> Displays the Ice version. </dd>
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
<dt><code>&#8211;old</code> <code>SLICE</code></dt>
<dd>
</dd><dt><code>&#8211;new</code> <code>SLICE</code></dt>
<dd>
 Loads the old or new Slice definitions contained in the file SLICE. These options may be specified multiple times if several files must be loaded. However, it is the user&#8217;s responsibility to ensure that duplicate definitions do not occur (which is possible when two files are loaded that share a common include file). One strategy for avoiding duplicate definitions is to load a single Slice file that contains only #include statements for each of the Slice files to be loaded. No duplication is possible in this case if the included files use include guards correctly. </dd>
<dt><code>&#8211;include-old</code> <code>DIR</code></dt>
<dd>
</dd><dt><code>&#8211;include-new</code> <code>DIR</code></dt>
<dd>
 Adds the directory DIR to the set of include paths for the old or new Slice definitions. </dd>
<dt><code>&#8211;key</code> <code>TYPE[,TYPE]</code></dt>
<dd>
</dd><dt><code>&#8211;value</code> <code>TYPE[,TYPE]</code></dt>
<dd>
 Specifies the Slice type(s) of the database key and value. If the type does not change, then the type only needs to be specified once. Otherwise, the old type is specified first, followed by a comma and the new type. For example, the option &#8211;key int,string indicates that the database key is migrating from int to string. On the other hand, the option &#8211;key int,int indicates that the key type does not change, and could be given simply as &#8211;key int. Type changes are restricted to those allowed by the compatibility rules, but custom migration provides additional flexibility. </dd>
<dt><code>-e</code></dt>
<dd>
 Indicates that a Freeze evictor database is being migrated. As a convenience, this option automatically sets the database key and value types to those appropriate for the Freeze evictor, and therefore the &#8211;key and &#8211;value options are not necessary. Specifically, the key type of a Freeze evictor database is Ice::Identity, and the value type is Freeze::ObjectRecord. The latter is defined in the Slice file Freeze/EvictorStorage.ice; however, this file does not need to be loaded into your old and new Slice definitions. </dd>
<dt><code>-i</code></dt>
<dd>
 Requests that transformdb ignore type changes that violate the compatibility rules. If this option is not specified, transformdb fails immediately if such a violation occurs. With this option, a warning is displayed but transformdb continues the requested action. The -i option can be specified in analysis or automatic migration modes. </dd>
<dt><code>-p</code></dt>
<dd> During migration, this option requests that transformdb purge object instances whose type is no longer found in the new Slice definitions. </dd>
<dt><code>-c</code></dt>
<dd>
 Use catastrophic recovery on the old Berkeley DB database environment prior to migration. </dd>
<dt><code>-w</code></dt>
<dd>
 Suppress duplicate warnings during migration. This option is especially useful to minimize diagnostic messages when transformdb would otherwise emit the same warning many times, such as when it detects the same issue in every record of a database. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dumpdb/">dumpdb</a></code>(1) </p>
