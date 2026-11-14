---
title: "testparams(3)"
name: "testparams"
section: "3"
letter: "t"
url: "/docs/linux/man/3-testparams/"
description: "QuantLib::Parameter – Base class for model arguments."
---

<p>QuantLib::Parameter &#8211; Base class for model arguments. </p>
<h2>Synopsis</h2>
<pre><code>const Array &amp; params () const



void setParam (Size i, Real x)



bool testParams (const Array &amp;params) const



Size size () const



Real operator() (Time t) const



const boost::shared_ptr&lt; Impl &gt; &amp; implementation () const



Protected Member Functions</code></pre>
<p> Inherited by <code>ConstantParameter</code>, <code>NullParameter</code>, <code>PiecewiseConstantParameter</code>, and <code>TermStructureFittingParameter</code>.</p>
<h3>Classes</h3>
<p>class <code>Impl</code><br />
 <i>Base class for model parameter implementation. </i></p>
<h3>Public Member Functions</h3>
<pre><code>const Array &amp; params () const



void setParam (Size i, Real x)



bool testParams (const Array &amp;params) const



Size size () const



Real operator() (Time t) const



const boost::shared_ptr&lt; Impl &gt; &amp; implementation () const



Protected Member Functions</code></pre>
<p> <code>Parameter</code> (Size size, const boost::shared_ptr&lt; <code>Impl</code> &gt; &amp;impl, const <code>Constraint</code> &amp;constraint)</p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; <code>Impl</code> &gt; <code>impl_</code> </p>
<p> <code>Array</code> <code>params_</code> </p>
<p> <code>Constraint</code> <code>constraint_</code></p>
<h2>Detailed Description</h2>
<p>Base class for model arguments.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
