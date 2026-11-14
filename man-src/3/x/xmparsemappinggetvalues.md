---
title: "xmparsemappinggetvalues(3)"
name: "xmparsemappinggetvalues"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmparsemappinggetvalues/"
description: "XmParseMappingGetValues — A compound string function to retrieve attributes of a parse mapping"
---

<p><code>XmParseMappingGetValues</code> &#8212; A compound string function to retrieve attributes of a parse mapping</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>void XmParseMappingGetValues</code>(
<code>XmParseMapping parse_mapping</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmParseMappingGetValues</code> retrieves attributes of an <code>XmParseMapping</code> object, using a resource-style argument list. If the <code>XmNsubstitute</code> resource is in the <i>arglist</i>, the function will allocate space to hold the returned <code>XmString</code> value. The application is responsible for managing this allocated space. The application can recover the allocated space by calling <code>XmStringFree</code>.</p>
<dl COMPACT>
<dt><i>arglist</i></p>
<dd>Specifies the argument list</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dl>
<p> For a complete definition of <code>XmParseMapping</code> and its associated resources, see <code><a href="/docs/linux/man/3-xmparsemapping/">XmParseMapping</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmparsemapping/">XmParseMapping</a></code>(3), <code><a href="/docs/linux/man/3-xmparsemappingcreate/">XmParseMappingCreate</a></code>(3), <code><a href="/docs/linux/man/3-xmparsemappingfree/">XmParseMappingFree</a></code>(3), <code><a href="/docs/linux/man/3-xmparsemappingsetvalues/">XmParseMappingSetValues</a></code>(3), <code><a href="/docs/linux/man/3-xmparsetable/">XmParseTable</a></code>(3), and <code><a href="/docs/linux/man/3-xmstring/">XmString</a></code>(3).</p>
