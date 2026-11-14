---
title: "xrmqgetresource(3)"
name: "xrmqgetresource"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xrmqgetresource/"
description: "XrmGetResource, XrmQGetResource, XrmQGetSearchList, XrmQGetSearchResource – retrieve database resources and search lists"
---

<p>XrmGetResource, XrmQGetResource, XrmQGetSearchList, XrmQGetSearchResource &#8211; retrieve database resources and search lists </p>
<h2>Syntax</h2>
<dl COMPACT>
<dt> #include &lt;X11/Xresource.h&gt;</p>
<dd>Bool XrmGetResource(XrmDatabase <i>database</i>, char *<i>str_name</i>, char *<i>str_class</i>, char **<i>str_type_return</i>, XrmValue *<i>value_return</i>);</p>
<dd>Bool XrmQGetResource(XrmDatabase <i>database</i>, XrmNameList <i>quark_name</i>, XrmClassList <i>quark_class</i>, XrmRepresentation *<i>quark_type_return</i>, XrmValue *<i>value_return</i>);</p>
<dd>typedef XrmHashTable *XrmSearchList; </p>
<p> Bool XrmQGetSearchList(XrmDatabase <i>database</i>, XrmNameList <i>names</i>, XrmClassList <i>classes</i>, XrmSearchList <i>list_return</i>, int <i>list_length</i>);</p>
<dd>Bool XrmQGetSearchResource(XrmSearchList <i>list</i>, XrmName <i>name</i>, XrmClass <i>class</i>, XrmRepresentation *<i>type_return</i>, XrmValue *<i>value_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>class</i></p>
<dd>Specifies the resource class.</p>
<dt><i>classes</i></p>
<dd>Specifies a list of resource classes.</p>
<dt><i>database</i></p>
<dd>Specifies the database that is to be used.</p>
<dt><i>list</i></p>
<dd>Specifies the search list returned by <code>XrmQGetSearchList</code>.</p>
<dt><i>list_length</i></p>
<dd>Specifies the number of entries (not the byte size) allocated for list_return.</p>
<dt><i>list_return</i></p>
<dd>Returns a search list for further use.</p>
<dt><i>name</i></p>
<dd>Specifies the resource name.</p>
<dt><i>names</i></p>
<dd>Specifies a list of resource names.</p>
<dt><i>quark_class</i></p>
<dd>Specifies the fully qualified class of the value being retrieved (as a quark).</p>
<dt><i>quark_name</i></p>
<dd>Specifies the fully qualified name of the value being retrieved (as a quark).</p>
<dt><i>quark_type_return</i></p>
<dd>Returns the representation type of the destination (as a quark).</p>
<dt><i>str_class</i></p>
<dd>Specifies the fully qualified class of the value being retrieved (as a string).</p>
<dt><i>str_name</i></p>
<dd>Specifies the fully qualified name of the value being retrieved (as a string).</p>
<dt><i>str_type_return</i></p>
<dd>Returns the representation type of the destination (as a string).</p>
<dt><i>type_return</i></p>
<dd>Returns data representation type.</p>
<dt><i>value_return</i></p>
<dd>Returns the value in the database.</dl>
<h2>Description</h2>
<p>The <code>XrmGetResource</code> and <code>XrmQGetResource</code> functions retrieve a resource from the specified database. Both take a fully qualified name/class pair, a destination resource representation, and the address of a value (size/address pair). The value and returned type point into database memory; therefore, you must not modify the data. </p>
<p> The database only frees or overwrites entries on <code>XrmPutResource</code>, <code>XrmQPutResource</code>, or <code>XrmMergeDatabases</code>. A client that is not storing new values into the database or is not merging the database should be safe using the address passed back at any time until it exits. If a resource was found, both <code>XrmGetResource</code> and <code>XrmQGetResource</code> return <code>True</code>; otherwise, they return <code>False</code>. </p>
<p> The <code>XrmQGetSearchList</code> function takes a list of names and classes and returns a list of database levels where a match might occur. The returned list is in best-to-worst order and uses the same algorithm as <code>XrmGetResource</code> for determining precedence. If list_return was large enough for the search list, <code>XrmQGetSearchList</code> returns <code>True</code>; otherwise, it returns <code>False</code>. </p>
<p> The size of the search list that the caller must allocate is dependent upon the number of levels and wildcards in the resource specifiers that are stored in the database. The worst case length is %3 sup n%, where <i>n</i> is the number of name or class components in names or classes. </p>
<p> When using <code>XrmQGetSearchList</code> followed by multiple probes for resources with a common name and class prefix, only the common prefix should be specified in the name and class list to <code>XrmQGetSearchList</code>. </p>
<p> The <code>XrmQGetSearchResource</code> function searches the specified database levels for the resource that is fully identified by the specified name and class. The search stops with the first match. <code>XrmQGetSearchResource</code> returns <code>True</code> if the resource was found; otherwise, it returns <code>False</code>. </p>
<p> A call to <code>XrmQGetSearchList</code> with a name and class list containing all but the last component of a resource name followed by a call to <code>XrmQGetSearchResource</code> with the last component name and class returns the same database entry as <code>XrmGetResource</code> and <code>XrmQGetResource</code> with the fully qualified name and class.</p>
<h2>Matching Rules</h2>
<p>The algorithm for determining which resource database entry matches a given query is the heart of the resource manager. All queries must fully specify the name and class of the desired resource (use of the characters &#8220;*&#8221; and &#8220;?&#8221; are not permitted). The library supports up to 100 components in a full name or class. Resources are stored in the database with only partially specified names and classes, using pattern matching constructs. An asterisk (*) is a loose binding and is used to represent any number of intervening components, including none. A period (.) is a tight binding and is used to separate immediately adjacent components. A question mark (?) is used to match any single component name or class. A database entry cannot end in a loose binding; the final component (which cannot be the character &#8220;?&#8221;) must be specified. The lookup algorithm searches the database for the entry that most closely matches (is most specific for) the full name and class being queried. When more than one database entry matches the full name and class, precedence rules are used to select just one. </p>
<p> The full name and class are scanned from left to right (from highest level in the hierarchy to lowest), one component at a time. At each level, the corresponding component and/or binding of each matching entry is determined, and these matching components and bindings are compared according to precedence rules. Each of the rules is applied at each level before moving to the next level, until a rule selects a single entry over all others. The rules, in order of precedence, are:</p>
<dl COMPACT>
<dt>1.</p>
<dd>An entry that contains a matching component (whether name, class, or the character &#8220;?&#8221;) takes precedence over entries that elide the level (that is, entries that match the level in a loose binding).</p>
<dt>2.</p>
<dd>An entry with a matching name takes precedence over both entries with a matching class and entries that match using the character &#8220;?&#8221;. An entry with a matching class takes precedence over entries that match using the character &#8220;?&#8221;.</p>
<dt>3.</p>
<dd>An entry preceded by a tight binding takes precedence over entries preceded by a loose binding.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xrminitialize/">XrmInitialize</a>(3), <a href="/docs/linux/man/3-xrmmergedatabases/">XrmMergeDatabases</a>(3), <a href="/docs/linux/man/3-xrmputresource/">XrmPutResource</a>(3), <a href="/docs/linux/man/3-xrmuniquequark/">XrmUniqueQuark</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
