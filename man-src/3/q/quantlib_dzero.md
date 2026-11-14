---
title: "quantlib_dzero(3)"
name: "quantlib_dzero"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_dzero/"
description: "QuantLib::DZero – $ D_{0} $ matricial representation"
---

<p>QuantLib::DZero &#8211; $ D_{0} $ matricial representation </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/methods/finitedifferences/dzero.hpp&gt; </p>
<p> Inherits <code>QuantLib::TridiagonalOperator</code>. </p>
<h3>Public Member Functions</h3>
<p><code>DZero</code> (Size gridPoints, Real h) </p>
<h2>Detailed Description</h2>
<p>$ D_{0} $ matricial representation </p>
<p> The differential operator $ D_{0} $ discretizes the first derivative with the second-order formula [ ac{<br />
 artial u_{i}}{<br />
 artial x} pprox ac{u_{i+1}-u_{i-1}}{2h} = D_{0} u_{i} ] </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned values is tested by checking them against numerical calculations.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
