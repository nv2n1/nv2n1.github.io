---
title: "ql_min_integer(3)"
name: "ql_min_integer"
section: "3"
letter: "q"
url: "/docs/linux/man/3-ql_min_integer/"
description: "Numeric limits –"
---

<p>Numeric limits &#8211; </p>
<h3>Defines</h3>
<p>#define <code>QL_MIN_INTEGER</code> ((std::numeric_limits&lt;QL_INTEGER&gt;::min)()) </p>
<p> #define <code>QL_MAX_INTEGER</code> ((std::numeric_limits&lt;QL_INTEGER&gt;::max)()) </p>
<p> #define <code>QL_MIN_REAL</code> -((std::numeric_limits&lt;QL_REAL&gt;::max)()) </p>
<p> #define <code>QL_MIN_POSITIVE_REAL</code> ((std::numeric_limits&lt;QL_REAL&gt;::min)()) </p>
<p> #define <code>QL_MAX_REAL</code> ((std::numeric_limits&lt;QL_REAL&gt;::max)()) </p>
<p> #define <code>QL_EPSILON</code> ((std::numeric_limits&lt;QL_REAL&gt;::epsilon)()) </p>
<p> #define <code>QL_NULL_INTEGER</code> ((std::numeric_limits&lt;int&gt;::max)()) </p>
<p> #define <code>QL_NULL_REAL</code> ((std::numeric_limits&lt;float&gt;::max)()) </p>
<h2>Detailed Description</h2>
<p>Some compilers do not give an implementation of &lt;limits&gt; yet. For the code to be portable these macros should be used instead of the corresponding method of std::numeric_limits or the corresponding macro defined in &lt;<a href="file:/usr/include/limits.h">limits.h</a>&gt;.</p>
<h2>Define Documentation</h2>
<h3>#define QL_MIN_INTEGER ((std::numeric_limits&lt;QL_INTEGER&gt;::min)())</h3>
<p>Defines the value of the largest representable negative integer value</p>
<h3>#define QL_MAX_INTEGER ((std::numeric_limits&lt;QL_INTEGER&gt;::max)())</h3>
<p>Defines the value of the largest representable integer value</p>
<h3>#define QL_MIN_REAL -((std::numeric_limits&lt;QL_REAL&gt;::max)())</h3>
<p>Defines the value of the largest representable negative floating-point value</p>
<h3>#define QL_MIN_POSITIVE_REAL ((std::numeric_limits&lt;QL_REAL&gt;::min)())</h3>
<p>Defines the value of the smallest representable positive double value</p>
<h3>#define QL_MAX_REAL ((std::numeric_limits&lt;QL_REAL&gt;::max)())</h3>
<p>Defines the value of the largest representable floating-point value</p>
<h3>#define QL_EPSILON ((std::numeric_limits&lt;QL_REAL&gt;::epsilon)())</h3>
<p>Defines the machine precision for operations over doubles </p>
<p> <code>Examples: </code> <code>CallableBonds.cpp</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
