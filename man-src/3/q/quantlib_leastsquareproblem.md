---
title: "quantlib_leastsquareproblem(3)"
name: "quantlib_leastsquareproblem"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_leastsquareproblem/"
description: "QuantLib::LeastSquareProblem – Base class for least square problem."
---

<p>QuantLib::LeastSquareProblem &#8211; Base class for least square problem. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/optimization/leastsquare.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p>virtual Size <code>size</code> ()=0<br />
 <i>size of the problem ie size of target vector </i><br />
 virtual void <code>targetAndValue</code> (const <code>Array</code> &amp;x, <code>Array</code> &amp;target, <code>Array</code> &amp;fct2fit)=0<br />
 <i>compute the target vector and the values of the function to fit </i><br />
 virtual void <code>targetValueAndGradient</code> (const <code>Array</code> &amp;x, <code>Matrix</code> &amp;grad_fct2fit, <code>Array</code> &amp;target, <code>Array</code> &amp;fct2fit)=0 </p>
<h2>Detailed Description</h2>
<p>Base class for least square problem.</p>
<h2>Member Function Documentation</h2>
<h3>virtual void targetValueAndGradient (const <code>Array</code> &amp; x, <code>Matrix</code> &amp; grad_fct2fit, <code>Array</code> &amp; target, <code>Array</code> &amp; fct2fit) [pure virtual]</h3>
<p>compute the target vector, the values of the function to fit and the matrix of derivatives </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
