---
title: "targetandvalue(3)"
name: "targetandvalue"
section: "3"
letter: "t"
url: "/docs/linux/man/3-targetandvalue/"
description: "QuantLib::LeastSquareProblem – Base class for least square problem."
---

<p>QuantLib::LeastSquareProblem &#8211; Base class for least square problem. </p>
<h2>Synopsis</h2>
<pre><code>virtual Size size ()=0


size of the problem ie size of target vector


virtual void targetAndValue (const Array &amp;x, Array &amp;target, Array &amp;fct2fit)=0


compute the target vector and the values of the function to fit


virtual void targetValueAndGradient (const Array &amp;x, Matrix &amp;grad_fct2fit, Array &amp;target, Array &amp;fct2fit)=0</code></pre>
<h3>Public Member Functions</h3>
<pre><code>virtual Size size ()=0


size of the problem ie size of target vector


virtual void targetAndValue (const Array &amp;x, Array &amp;target, Array &amp;fct2fit)=0


compute the target vector and the values of the function to fit


virtual void targetValueAndGradient (const Array &amp;x, Matrix &amp;grad_fct2fit, Array &amp;target, Array &amp;fct2fit)=0</code></pre>
<h2>Detailed Description</h2>
<p>Base class for least square problem.</p>
<h2>Member Function Documentation</h2>
<h3>virtual void targetValueAndGradient (const <code>Array</code> &amp; x, <code>Matrix</code> &amp; grad_fct2fit, <code>Array</code> &amp; target, <code>Array</code> &amp; fct2fit) [pure virtual]</h3>
<p>compute the target vector, the values of the function to fit and the matrix of derivatives</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
