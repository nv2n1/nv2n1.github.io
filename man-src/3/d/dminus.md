---
title: "dminus(3)"
name: "dminus"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dminus/"
description: "QuantLib::DMinus – $ D_{-} $ matricial representation"
---

<p>QuantLib::DMinus &#8211; $ D_{-} $ matricial representation </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/methods/finitedifferences/dminus.hpp&gt; </p>
<p> Inherits <code>QuantLib::TridiagonalOperator</code>. </p>
<h3>Public Member Functions</h3>
<p><code>DMinus</code> (Size gridPoints, Real h) </p>
<h2>Detailed Description</h2>
<p>$ D_{-} $ matricial representation </p>
<p> The differential operator $ D_{-} $ discretizes the first derivative with the first-order formula [ ac{<br />
 artial u_{i}}{<br />
 artial x} pprox ac{u_{i}-u_{i-1}}{h} = D_{-} u_{i} ] </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
