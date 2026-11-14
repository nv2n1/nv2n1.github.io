---
title: "yvalues(3)"
name: "yvalues"
section: "3"
letter: "y"
url: "/docs/linux/man/3-yvalues/"
description: "QuantLib::Interpolation::Impl – abstract base class for interpolation implementations"
---

<p>QuantLib::Interpolation::Impl &#8211; abstract base class for interpolation implementations </p>
<h2>Synopsis</h2>
<pre><code>virtual void update ()=0



virtual Real xMin () const =0



virtual Real xMax () const =0



virtual std::vector&lt; Real &gt; xValues () const =0



virtual std::vector&lt; Real &gt; yValues () const =0



virtual bool isInRange (Real) const =0



virtual Real value (Real) const =0



virtual Real primitive (Real) const =0



virtual Real derivative (Real) const =0



virtual Real secondDerivative (Real) const =0</code></pre>
<p> Inherited by <code>templateImpl&lt; I1, I2 &gt;</code>, and <code>templateImpl&lt; I1, I2 &gt;</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>virtual void update ()=0



virtual Real xMin () const =0



virtual Real xMax () const =0



virtual std::vector&lt; Real &gt; xValues () const =0



virtual std::vector&lt; Real &gt; yValues () const =0



virtual bool isInRange (Real) const =0



virtual Real value (Real) const =0



virtual Real primitive (Real) const =0



virtual Real derivative (Real) const =0



virtual Real secondDerivative (Real) const =0</code></pre>
<h2>Detailed Description</h2>
<p>abstract base class for interpolation implementations</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
