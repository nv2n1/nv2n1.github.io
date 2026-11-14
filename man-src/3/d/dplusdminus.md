---
title: "dplusdminus(3)"
name: "dplusdminus"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dplusdminus/"
description: "QuantLib::DPlusDMinus – $ D_{+}D_{-} $ matricial representation"
---

<p>QuantLib::DPlusDMinus &#8211; $ D_{+}D_{-} $ matricial representation </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/methods/finitedifferences/dplusdminus.hpp&gt; </p>
<p> Inherits <code>QuantLib::TridiagonalOperator</code>. </p>
<h3>Public Member Functions</h3>
<p><code>DPlusDMinus</code> (Size gridPoints, Real h) </p>
<h2>Detailed Description</h2>
<p>$ D_{+}D_{-} $ matricial representation </p>
<p> The differential operator $ D_{+}D_{-} $ discretizes the second derivative with the second-order formula [ ac{<br />
 artial^2 u_{i}}{<br />
 artial x^2} pprox ac{u_{i+1}-2u_{i}+u_{i-1}}{h^2} = D_{+}D_{-} u_{i} ] </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned values is tested by checking them against numerical calculations.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
