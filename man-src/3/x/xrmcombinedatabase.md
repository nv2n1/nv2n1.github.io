---
title: "xrmcombinedatabase(3)"
name: "xrmcombinedatabase"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xrmcombinedatabase/"
description: "XrmMergeDatabases, XrmCombineDatabase, XrmCombineFileDatabase – merge resource databases"
---

<p>XrmMergeDatabases, XrmCombineDatabase, XrmCombineFileDatabase &#8211; merge resource databases </p>
<h2>Syntax</h2>
<dl COMPACT>
<dt> #include &lt;X11/Xresource.h&gt;</p>
<dd>void XrmMergeDatabases(XrmDatabase <i>source_db</i>, XrmDatabase *<i>target_db</i>);</p>
<dd>void XrmCombineDatabase(XrmDatabase <i>source_db</i>, XrmDatabase *<i>target_db</i>, Bool <i>override</i>);</p>
<dd>Status XrmCombineFileDatabase(char *<i>filename</i>, XrmDatabase *<i>target_db</i>, Bool <i>override</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>source_db</i></p>
<dd>Specifies the resource database that is to be merged into the target database.</p>
<dt><i>target_db</i></p>
<dd>Specifies the resource database into which the source database is to be merged.</p>
<dt><i>filename</i></p>
<dd>Specifies the resource database file name.</p>
<dt><i>override</i></p>
<dd>Specifies whether source entries override target ones.</dl>
<h2>Description</h2>
<p>Calling the <code>XrmMergeDatabases</code> function is equivalent to calling the <code>XrmCombineDatabase</code> function with an override argument of <code>True</code>. </p>
<p> The <code>XrmCombineDatabase</code> function merges the contents of one database into another. If the same specifier is used for an entry in both databases, the entry in the source_db will replace the entry in the target_db if override is <code>True</code>; otherwise, the entry in source_db is discarded. If target_db contains NULL, <code>XrmCombineDatabase</code> simply stores source_db in it. Otherwise, source_db is destroyed by the merge, but the database pointed to by target_db is not destroyed. The database entries are merged without changing values or types, regardless of the locales of the databases. The locale of the target database is not modified. </p>
<p> The <code>XrmCombineFileDatabase</code> function merges the contents of a resource file into a database. If the same specifier is used for an entry in both the file and the database, the entry in the file will replace the entry in the database if override is <code>True</code>; otherwise, the entry in the file is discarded. The file is parsed in the current locale. If the file cannot be read, a zero status is returned; otherwise, a nonzero status is returned. If target_db contains NULL, <code>XrmCombineFileDatabase</code> creates and returns a new database to it. Otherwise, the database pointed to by target_db is not destroyed by the merge. The database entries are merged without changing values or types, regardless of the locale of the database. The locale of the target database is not modified.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xrmgetresource/">XrmGetResource</a>(3), <a href="/docs/linux/man/3-xrminitialize/">XrmInitialize</a>(3), <a href="/docs/linux/man/3-xrmputresource/">XrmPutResource</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
