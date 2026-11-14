---
title: "quantlib_dplus(3)"
name: "quantlib_dplus"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_dplus/"
description: "QuantLib::DPlus – $ D_{+} $ matricial representation"
---

<p>QuantLib::DPlus &#8211; $ D_{+} $ matricial representation </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/methods/finitedifferences/dplus.hpp&gt; </p>
<p> Inherits <code>QuantLib::TridiagonalOperator</code>. </p>
<h3>Public Member Functions</h3>
<p><code>DPlus</code> (Size gridPoints, Real h) </p>
<h2>Detailed Description</h2>
<p>$ D_{+} $ matricial representation </p>
<p> The differential operator $ D_{+} $ discretizes the first derivative with the first-order formula [ ac{<br />
 artial u_{i}}{<br />
 artial x} pprox ac{u_{i+1}-u_{i}}{h} = D_{+} u_{i} ] </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
