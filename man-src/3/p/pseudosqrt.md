---
title: "pseudosqrt(3)"
name: "pseudosqrt"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pseudosqrt/"
description: "QuantLib::LmCorrelationModel – libor forward correlation model"
---

<p>QuantLib::LmCorrelationModel &#8211; libor forward correlation model </p>
<h2>Synopsis</h2>
<pre><code>LmCorrelationModel (Size size, Size nArguments)



virtual Size size () const



virtual Size factors () const



std::vector&lt; Parameter &gt; &amp; params ()



void setParams (const std::vector&lt; Parameter &gt; &amp;arguments)



virtual Disposable&lt; Matrix &gt; correlation (Time t, const Array &amp;x=Null&lt; Array &gt;()) const =0



virtual Disposable&lt; Matrix &gt; pseudoSqrt (Time t, const Array &amp;x=Null&lt; Array &gt;()) const



virtual Real correlation (Size i, Size j, Time t, const Array &amp;x=Null&lt; Array &gt;()) const



virtual bool isTimeIndependent () const



Protected Member Functions
virtual void generateArguments ()=0



Protected Attributes
const Size size_



std::vector&lt; Parameter &gt; arguments_</code></pre>
<p> Inherited by LmConstWrapperCorrelationModel, <code>LmExponentialCorrelationModel</code>, and <code>LmLinearExponentialCorrelationModel</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>LmCorrelationModel (Size size, Size nArguments)



virtual Size size () const



virtual Size factors () const



std::vector&lt; Parameter &gt; &amp; params ()



void setParams (const std::vector&lt; Parameter &gt; &amp;arguments)



virtual Disposable&lt; Matrix &gt; correlation (Time t, const Array &amp;x=Null&lt; Array &gt;()) const =0



virtual Disposable&lt; Matrix &gt; pseudoSqrt (Time t, const Array &amp;x=Null&lt; Array &gt;()) const



virtual Real correlation (Size i, Size j, Time t, const Array &amp;x=Null&lt; Array &gt;()) const



virtual bool isTimeIndependent () const



Protected Member Functions
virtual void generateArguments ()=0



Protected Attributes
const Size size_



std::vector&lt; Parameter &gt; arguments_</code></pre>
<h2>Detailed Description</h2>
<p>libor forward correlation model</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
