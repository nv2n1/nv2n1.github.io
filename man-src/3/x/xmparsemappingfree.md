---
title: "xmparsemappingfree(3)"
name: "xmparsemappingfree"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmparsemappingfree/"
description: "XmParseMappingFree — A compound string function to free a parse mapping"
---

<p><code>XmParseMappingFree</code> &#8212; A compound string function to free a parse mapping</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>void XmParseMappingFree</code>(
<code>XmParseMapping parse_mapping</code>);</pre>
<h2>Description</h2>
<p><code>XmParseMappingFree</code> recovers memory used by an <code>XmParseMapping</code>.</p>
<dl COMPACT>
<dt><i>parse_mapping</i></p>
<dd>Specifies the parse mapping to be freed</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmparsemapping/">XmParseMapping</a></code>(3), <code><a href="/docs/linux/man/3-xmparsemappingcreate/">XmParseMappingCreate</a></code>(3), <code><a href="/docs/linux/man/3-xmparsemappinggetvalues/">XmParseMappingGetValues</a></code>(3), <code><a href="/docs/linux/man/3-xmparsemappingsetvalues/">XmParseMappingSetValues</a></code>(3), <code><a href="/docs/linux/man/3-xmparsetable/">XmParseTable</a></code>(3), and <code><a href="/docs/linux/man/3-xmstring/">XmString</a></code>(3).</p>
