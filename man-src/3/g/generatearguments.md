---
title: "generatearguments(3)"
name: "generatearguments"
section: "3"
letter: "g"
url: "/docs/linux/man/3-generatearguments/"
description: "QuantLib::LmCorrelationModel – libor forward correlation model"
---

<p>QuantLib::LmCorrelationModel &#8211; libor forward correlation model </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/legacy/libormarketmodels/lmcorrmodel.hpp&gt; </p>
<p> Inherited by LmConstWrapperCorrelationModel, <code>LmExponentialCorrelationModel</code>, and <code>LmLinearExponentialCorrelationModel</code>. </p>
<h3>Public Member Functions</h3>
<p><code>LmCorrelationModel</code> (Size size, Size nArguments) </p>
<p> virtual Size <code>size</code> () const </p>
<p> virtual Size <code>factors</code> () const </p>
<p> std::vector&lt; <code>Parameter</code> &gt; &amp; <code>params</code> () </p>
<p> void <code>setParams</code> (const std::vector&lt; <code>Parameter</code> &gt; &amp;arguments) </p>
<p> virtual <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>correlation</code> (Time t, const <code>Array</code> &amp;x=<code>Null</code>&lt; <code>Array</code> &gt;()) const =0 </p>
<p> virtual <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>pseudoSqrt</code> (Time t, const <code>Array</code> &amp;x=<code>Null</code>&lt; <code>Array</code> &gt;()) const </p>
<p> virtual <code>Real</code> <code>correlation</code> (Size i, Size j, Time t, const <code>Array</code> &amp;x=<code>Null</code>&lt; <code>Array</code> &gt;()) const </p>
<p> virtual bool <code>isTimeIndependent</code> () const </p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>generateArguments</code> ()=0 </p>
<h3>Protected Attributes</h3>
<p>const Size <code>size_</code> </p>
<p> std::vector&lt; <code>Parameter</code> &gt; <code>arguments_</code> </p>
<h2>Detailed Description</h2>
<p>libor forward correlation model </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
