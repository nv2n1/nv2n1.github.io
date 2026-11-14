---
title: "lmvolatilitymodel(3)"
name: "lmvolatilitymodel"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lmvolatilitymodel/"
description: "QuantLib::LmVolatilityModel – caplet volatility model"
---

<p>QuantLib::LmVolatilityModel &#8211; caplet volatility model </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/legacy/libormarketmodels/lmvolmodel.hpp&gt; </p>
<p> Inherited by <code>LmConstWrapperVolatilityModel</code>, LmFixedVolatilityModel, and <code>LmLinearExponentialVolatilityModel</code>. </p>
<h3>Public Member Functions</h3>
<p><code>LmVolatilityModel</code> (Size size, Size nArguments) </p>
<p> Size <code>size</code> () const </p>
<p> std::vector&lt; <code>Parameter</code> &gt; &amp; <code>params</code> () </p>
<p> void <code>setParams</code> (const std::vector&lt; <code>Parameter</code> &gt; &amp;arguments) </p>
<p> virtual <code>Disposable</code>&lt; <code>Array</code> &gt; <code>volatility</code> (Time t, const <code>Array</code> &amp;x=<code>Null</code>&lt; <code>Array</code> &gt;()) const =0 </p>
<p> virtual <code>Volatility</code> <code>volatility</code> (Size i, Time t, const <code>Array</code> &amp;x=<code>Null</code>&lt; <code>Array</code> &gt;()) const </p>
<p> virtual <code>Real</code> <code>integratedVariance</code> (Size i, Size j, Time u, const <code>Array</code> &amp;x=<code>Null</code>&lt; <code>Array</code> &gt;()) const </p>
<h3>Protected Attributes</h3>
<p>const Size <code>size_</code> </p>
<p> std::vector&lt; <code>Parameter</code> &gt; <code>arguments_</code> </p>
<h2>Detailed Description</h2>
<p>caplet volatility model </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
