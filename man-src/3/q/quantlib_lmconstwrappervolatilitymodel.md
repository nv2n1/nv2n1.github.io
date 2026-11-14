---
title: "quantlib_lmconstwrappervolatilitymodel(3)"
name: "quantlib_lmconstwrappervolatilitymodel"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_lmconstwrappervolatilitymodel/"
description: "QuantLib::LmConstWrapperVolatilityModel – caplet const volatility model"
---

<p>QuantLib::LmConstWrapperVolatilityModel &#8211; caplet const volatility model </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/legacy/libormarketmodels/lmconstwrappervolmodel.hpp&gt; </p>
<p> Inherits <code>QuantLib::LmVolatilityModel</code>. </p>
<h3>Public Member Functions</h3>
<p><code>LmConstWrapperVolatilityModel</code> (const boost::shared_ptr&lt; <code>LmVolatilityModel</code> &gt; &amp;volaModel) </p>
<p> <code>Disposable</code>&lt; <code>Array</code> &gt; <code>volatility</code> (Time t, const <code>Array</code> &amp;x=<code>Null</code>&lt; <code>Array</code> &gt;()) const </p>
<p> <code>Volatility</code> <code>volatility</code> (Size i, Time t, const <code>Array</code> &amp;x=<code>Null</code>&lt; <code>Array</code> &gt;()) </p>
<p> <code>Real</code> <code>integratedVariance</code> (Size i, Size j, Time u, const <code>Array</code> &amp;x=<code>Null</code>&lt; <code>Array</code> &gt;()) const </p>
<h3>Protected Attributes</h3>
<p>const boost::shared_ptr&lt; <code>LmVolatilityModel</code> &gt; <code>volaModel_</code> </p>
<h2>Detailed Description</h2>
<p>caplet const volatility model </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
