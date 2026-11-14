---
title: "ql_version(3)"
name: "ql_version"
section: "3"
letter: "q"
url: "/docs/linux/man/3-ql_version/"
description: "ql/qldefines.hpp – Global definitions and compiler switches."
---

<p>ql/qldefines.hpp &#8211; Global definitions and compiler switches. </p>
<h2>Synopsis</h2>
<p>#include &lt;boost/config.hpp&gt;<br />
 #include &lt;boost/version.hpp&gt;<br />
 #include &lt;ql/config.ansi.hpp&gt;<br />
 #include &lt;cmath&gt;<br />
 #include &lt;boost/limits.hpp&gt; </p>
<h3>Defines</h3>
<p>#define <code>BOOST_ENABLE_ASSERT_HANDLER</code> </p>
<p> #define <code>QL_INTEGER</code> int </p>
<p> #define <code>QL_BIG_INTEGER</code> long </p>
<p> #define <code>QL_REAL</code> double </p>
<p> #define <code>QL_VERSION</code> &#8216;0.9.7&#8217;<br />
 <i>version string </i><br />
 #define <code>QL_HEX_VERSION</code> 0x000907f0<br />
 <i>version hexadecimal number </i><br />
 #define <code>QL_LIB_VERSION</code> &#8216;0_9_7&#8217;<br />
 <i>version string for output lib name </i><br />
 #define <code>QL_MIN_INTEGER</code> ((std::numeric_limits&lt;QL_INTEGER&gt;::min)()) </p>
<p> #define <code>QL_MAX_INTEGER</code> ((std::numeric_limits&lt;QL_INTEGER&gt;::max)()) </p>
<p> #define <code>QL_MIN_REAL</code> -((std::numeric_limits&lt;QL_REAL&gt;::max)()) </p>
<p> #define <code>QL_MAX_REAL</code> ((std::numeric_limits&lt;QL_REAL&gt;::max)()) </p>
<p> #define <code>QL_MIN_POSITIVE_REAL</code> ((std::numeric_limits&lt;QL_REAL&gt;::min)()) </p>
<p> #define <code>QL_EPSILON</code> ((std::numeric_limits&lt;QL_REAL&gt;::epsilon)()) </p>
<p> #define <code>QL_NULL_INTEGER</code> ((std::numeric_limits&lt;int&gt;::max)()) </p>
<p> #define <code>QL_NULL_REAL</code> ((std::numeric_limits&lt;float&gt;::max)()) </p>
<h2>Detailed Description</h2>
<p>Global definitions and compiler switches. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
