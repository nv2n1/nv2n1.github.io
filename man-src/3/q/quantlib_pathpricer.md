---
title: "quantlib_pathpricer(3)"
name: "quantlib_pathpricer"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_pathpricer/"
description: "QuantLib::PathPricer – base class for path pricers"
---

<p>QuantLib::PathPricer &#8211; base class for path pricers </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/methods/montecarlo/pathpricer.hpp&gt; </p>
<p> Inherits std::unary_function&lt;PathType, ValueType&gt;. </p>
<h3>Public Member Functions</h3>
<p>virtual ValueType <code>operator()</code> (const PathType &amp;path) const =0 </p>
<h2>Detailed Description</h2>
<h3>template&lt;class PathType, class ValueType = Real&gt; class QuantLib::PathPricer&lt; PathType, ValueType &gt;</h3>
<p>base class for path pricers </p>
<p> Returns the value of an option on a given path. </p>
<p> <code>Examples: </code> </p>
<p> <code>DiscreteHedging.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
