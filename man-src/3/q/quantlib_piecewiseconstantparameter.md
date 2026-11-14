---
title: "quantlib_piecewiseconstantparameter(3)"
name: "quantlib_piecewiseconstantparameter"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_piecewiseconstantparameter/"
description: "QuantLib::PiecewiseConstantParameter – Piecewise-constant parameter."
---

<p>QuantLib::PiecewiseConstantParameter &#8211; Piecewise-constant parameter. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/parameter.hpp&gt; </p>
<p> Inherits <code>QuantLib::Parameter</code>. </p>
<h3>Public Member Functions</h3>
<p><code>PiecewiseConstantParameter</code> (const std::vector&lt; <code>Time</code> &gt; &amp;times) </p>
<h2>Detailed Description</h2>
<p>Piecewise-constant parameter. </p>
<p> $ a(t) = a_i if t_{i-1} geq t &lt; t_i $. This kind of parameter is usually used to enhance the fitting of a model </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
