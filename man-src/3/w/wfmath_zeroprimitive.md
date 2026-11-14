---
title: "wfmath_zeroprimitive(3)"
name: "wfmath_zeroprimitive"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wfmath_zeroprimitive/"
description: "WFMath::ZeroPrimitive – Utility class for providing zero primitives. This class will only work with simple structures such as Vector or Point which provide a m_elem structure. In order for it to ac..."
---

<p>WFMath::ZeroPrimitive &#8211; Utility class for providing zero primitives. This class will only work with simple structures such as <code>Vector</code> or <code>Point</code> which provide a m_elem structure. In order for it to access the m_elem structure it must be declared as a friend class of the class it will provide an instance of. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/zero.h">zero.h</a>&gt; </p>
<h3>Public Member Functions</h3>
<p><code>ZeroPrimitive</code> (int dim)<br />
 <i>Ctor. An instance of </i><code>Shape</code> with zero values will be created at construction time.<br />
 const <code>Shape</code> &amp; <code>getShape</code> () const<br />
 <i>Gets the zeroed shape. </i></p>
<h2>Detailed Description</h2>
<h3>template&lt;typename Shape&gt; class WFMath::ZeroPrimitive&lt; Shape &gt;</h3>
<p>Utility class for providing zero primitives. This class will only work with simple structures such as <code>Vector</code> or <code>Point</code> which provide a m_elem structure. In order for it to access the m_elem structure it must be declared as a friend class of the class it will provide an instance of. </p>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Erik Hjortsberg &lt;erik [at] worldforge.org&gt;</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>template&lt;typename Shape&gt; <code>WFMath::ZeroPrimitive</code>&lt; <code>Shape</code> &gt;::<code>ZeroPrimitive</code> (int dim) [inline]</h3>
<p>Ctor. An instance of <code>Shape</code> with zero values will be created at construction time. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dim</i> The dimensions of the shape.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for WFMath from the source code.</p>
