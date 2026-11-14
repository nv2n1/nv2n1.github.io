---
title: "traits_type(3)"
name: "traits_type"
section: "3"
letter: "t"
url: "/docs/linux/man/3-traits_type/"
description: "QuantLib::PiecewiseDefaultCurve – Piecewise default-probability term structure."
---

<p>QuantLib::PiecewiseDefaultCurve &#8211; Piecewise default-probability term structure. </p>
<h2>Synopsis</h2>
<pre><code>void update ()



Friends</code></pre>
<p> Inherits Traits::template curve::type&lt;Interpolator&gt;, and <code>QuantLib::LazyObject</code>.</p>
<h3>Public Types</h3>
<p>typedef Traits <code>traits_type</code> </p>
<p> typedef Interpolator <code>interpolator_type</code></p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code><br />
 void update ()</p>
<p>Friends <code>DefaultTermStructure interface</code> </p>
<p> <code>Date</code> <code>maxDate</code> () const<br />
 <code>Inspectors</code><br />
 void update ()</p>
<p>Friends <code>Observer interface</code> </p>
<pre><code>void update ()



Friends</code></pre>
<p> class <code>Bootstrap&lt; this_curve &gt;</code> </p>
<p> class <code>BootstrapError&lt; this_curve &gt;</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;class Traits, class Interpolator, template&lt; class &gt; class Bootstrap = IterativeBootstrap&gt; class QuantLib::PiecewiseDefaultCurve&lt; Traits, Interpolator, Bootstrap &gt;</h3>
<p>Piecewise default-probability term structure. </p>
<p> This term structure is bootstrapped on a number of credit instruments which are passed as a vector of handles to DefaultProbabilityHelper instances. Their maturities mark the boundaries of the interpolated segments. </p>
<p> Each segment is determined sequentially starting from the earliest period to the latest and is chosen so that the instrument whose maturity marks the end of such segment is correctly repriced on the curve. </p>
<p> <code>Warning</code></p>
<dl>
<dd>The bootstrapping algorithm will raise an exception if any two instruments have the same maturity date.</dl>
<p> <code>Examples: </code> </p>
<p> <code>CDS.cpp</code>.</p>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Reimplemented from <code>LazyObject</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
