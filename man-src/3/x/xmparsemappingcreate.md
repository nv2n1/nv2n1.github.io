---
title: "xmparsemappingcreate(3)"
name: "xmparsemappingcreate"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmparsemappingcreate/"
description: "XmParseMappingCreate — A compound string function to create a parse mapping"
---

<p><code>XmParseMappingCreate</code> &#8212; A compound string function to create a parse mapping</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmParseMapping XmParseMappingCreate</code>(
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmParseMappingCreate</code> creates a parse mapping for use in a parse table. This function allows the application to specify values for components of the parse mapping using a resource-style argument list.</p>
<dl COMPACT>
<dt><i>arglist</i></p>
<dd>Specifies the argument list</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dl>
<p> For a complete definition of <code>XmParseMapping</code> and its associated resources, see <code><a href="/docs/linux/man/3-xmparsemapping/">XmParseMapping</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the <code>XmParseMapping</code> object. The function allocates space to hold the returned <code>XmParseMapping</code> object. The application is responsible for managing the allocated space. The application can recover the allocated space by calling <code>XmParseMappingFree</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmparsemapping/">XmParseMapping</a></code>(3), <code><a href="/docs/linux/man/3-xmparsemappingfree/">XmParseMappingFree</a></code>(3), <code><a href="/docs/linux/man/3-xmparsemappinggetvalues/">XmParseMappingGetValues</a></code>(3), <code><a href="/docs/linux/man/3-xmparsemappingsetvalues/">XmParseMappingSetValues</a></code>(3), <code><a href="/docs/linux/man/3-xmparsetable/">XmParseTable</a></code>(3), and <code><a href="/docs/linux/man/3-xmstring/">XmString</a></code>(3).</p>
