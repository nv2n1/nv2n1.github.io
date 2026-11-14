---
title: "quantlib_garmankohlagenprocess(3)"
name: "quantlib_garmankohlagenprocess"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_garmankohlagenprocess/"
description: "QuantLib::GarmanKohlagenProcess – Garman-Kohlhagen (1983) stochastic process."
---

<p>QuantLib::GarmanKohlagenProcess &#8211; Garman-Kohlhagen (1983) stochastic process. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/processes/blackscholesprocess.hpp&gt; </p>
<p> Inherits <code>QuantLib::GeneralizedBlackScholesProcess</code>. </p>
<h3>Public Member Functions</h3>
<p><code>GarmanKohlagenProcess</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;x0, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;foreignRiskFreeTS, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;domesticRiskFreeTS, const <code>Handle</code>&lt; <code>BlackVolTermStructure</code> &gt; &amp;blackVolTS, const boost::shared_ptr&lt; <code>discretization</code> &gt; &amp;d=boost::shared_ptr&lt; <code>discretization</code> &gt;(new <code>EulerDiscretization</code>)) </p>
<h2>Detailed Description</h2>
<p>Garman-Kohlhagen (1983) stochastic process. </p>
<p> This class describes the stochastic process for an exchange rate given by [ dS(t, S) = (r(t) &#8211; r_f(t) &#8211; ac{igma(t, S)^2}{2}) dt + igma dW_t. ] </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
