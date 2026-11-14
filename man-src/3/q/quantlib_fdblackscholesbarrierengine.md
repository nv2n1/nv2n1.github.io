---
title: "quantlib_fdblackscholesbarrierengine(3)"
name: "quantlib_fdblackscholesbarrierengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_fdblackscholesbarrierengine/"
description: "QuantLib::FdBlackScholesBarrierEngine – Finite-Differences Black Scholes barrier option engine."
---

<p>QuantLib::FdBlackScholesBarrierEngine &#8211; Finite-Differences Black Scholes barrier option engine. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/finitedifferences/fdblackscholesbarrierengine.hpp&gt; </p>
<p> Inherits <code>GenericEngine&lt; DividendBarrierOption::arguments, DividendBarrierOption::results &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>FdBlackScholesBarrierEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;process, Size tGrid=100, Size xGrid=100) </p>
<p> void <code>calculate</code> () const </p>
<h2>Detailed Description</h2>
<p>Finite-Differences Black Scholes barrier option engine. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned value is tested by reproducing results available in web/literature and comparison with Black pricing.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
