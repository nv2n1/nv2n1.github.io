---
title: "quantlib_leastsquarefunction(3)"
name: "quantlib_leastsquarefunction"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_leastsquarefunction/"
description: "QuantLib::LeastSquareFunction – Cost function for least-square problems."
---

<p>QuantLib::LeastSquareFunction &#8211; Cost function for least-square problems. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/optimization/leastsquare.hpp&gt; </p>
<p> Inherits <code>QuantLib::CostFunction</code>. </p>
<h3>Public Member Functions</h3>
<p><code>LeastSquareFunction</code> (<code>LeastSquareProblem</code> &amp;lsp)<br />
 <i>Default constructor. </i><br />
 virtual <code>~LeastSquareFunction</code> ()<br />
 <i>Destructor. </i><br />
 virtual <code>Real</code> <code>value</code> (const <code>Array</code> &amp;x) const<br />
 <i>compute value of the least square function </i><br />
 virtual <code>Disposable</code>&lt; <code>Array</code> &gt; <code>values</code> (const <code>Array</code> &amp;) const<br />
 <i>method to overload to compute the cost function values in x </i><br />
 virtual void <code>gradient</code> (<code>Array</code> &amp;grad_f, const <code>Array</code> &amp;x) const<br />
 <i>compute vector of derivatives of the least square function </i><br />
 virtual <code>Real</code> <code>valueAndGradient</code> (<code>Array</code> &amp;grad_f, const <code>Array</code> &amp;x) const<br />
 <i>compute value and gradient of the least square function </i></p>
<h3>Protected Attributes</h3>
<p><code>LeastSquareProblem</code> &amp; <code>lsp_</code><br />
 <i>least square problem </i></p>
<h2>Detailed Description</h2>
<p>Cost function for least-square problems. </p>
<p> Implements a cost function using the interface provided by the <code>LeastSquareProblem</code> class. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
