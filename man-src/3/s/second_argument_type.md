---
title: "second_argument_type(3)"
name: "second_argument_type"
section: "3"
letter: "s"
url: "/docs/linux/man/3-second_argument_type/"
description: "QuantLib::Interpolation2D – base class for 2-D interpolations."
---

<p>QuantLib::Interpolation2D &#8211; base class for 2-D interpolations. </p>
<h2>Synopsis</h2>
<pre><code>Real operator() (Real x, Real y, bool allowExtrapolation=false) const



Real xMin () const



Real xMax () const



std::vector&lt; Real &gt; xValues () const



Size locateX (Real x) const



Real yMin () const



Real yMax () const



std::vector&lt; Real &gt; yValues () const



Size locateY (Real y) const



const Matrix &amp; zData () const



bool isInRange (Real x, Real y) const



void update ()



Protected Member Functions
void checkRange (Real x, Real y, bool extrapolate) const



Protected Attributes</code></pre>
<p> Inherits <code>QuantLib::Extrapolator</code>. Inherited by <code>BicubicSpline</code>, <code>BilinearInterpolation</code>, and FlatExtrapolator2D.</p>
<h3>Classes</h3>
<p>class <code>Impl</code><br />
 <i>abstract base class for 2-D interpolation implementations </i><br />
 class <code>templateImpl</code><br />
 <i>basic template implementation </i></p>
<h3>Public Types</h3>
<p>typedef <code>Real</code> <code>first_argument_type</code> </p>
<p> typedef <code>Real</code> <code>second_argument_type</code> </p>
<p> typedef <code>Real</code> <code>result_type</code></p>
<h3>Public Member Functions</h3>
<pre><code>Real operator() (Real x, Real y, bool allowExtrapolation=false) const



Real xMin () const



Real xMax () const



std::vector&lt; Real &gt; xValues () const



Size locateX (Real x) const



Real yMin () const



Real yMax () const



std::vector&lt; Real &gt; yValues () const



Size locateY (Real y) const



const Matrix &amp; zData () const



bool isInRange (Real x, Real y) const



void update ()



Protected Member Functions
void checkRange (Real x, Real y, bool extrapolate) const



Protected Attributes</code></pre>
<p> boost::shared_ptr&lt; <code>Impl</code> &gt; <code>impl_</code></p>
<h2>Detailed Description</h2>
<p>base class for 2-D interpolations. </p>
<p> Classes derived from this class will provide interpolated values from two sequences of length $ N $ and $ M $, representing the discretized values of the $ x $ and $ y $ variables, and a $ N imes M $ matrix representing the tabulated function values.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
