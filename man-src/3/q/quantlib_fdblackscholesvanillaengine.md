---
title: "quantlib_fdblackscholesvanillaengine(3)"
name: "quantlib_fdblackscholesvanillaengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_fdblackscholesvanillaengine/"
description: "QuantLib::FdBlackScholesVanillaEngine – Finite-Differences Black Scholes vanilla option engine."
---

<p>QuantLib::FdBlackScholesVanillaEngine &#8211; Finite-Differences Black Scholes vanilla option engine. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/finitedifferences/fdblackscholesvanillaengine.hpp&gt; </p>
<p> Inherits <code>GenericEngine&lt; DividendVanillaOption::arguments, DividendVanillaOption::results &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>FdBlackScholesVanillaEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;, Size tGrid=100, Size xGrid=100) </p>
<p> void <code>calculate</code> () const </p>
<h2>Detailed Description</h2>
<p>Finite-Differences Black Scholes vanilla option engine. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned value is tested by reproducing results available in web/literature and comparison with Black pricing.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
