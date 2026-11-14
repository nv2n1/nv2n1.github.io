---
title: "quantlib_parameter(3)"
name: "quantlib_parameter"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_parameter/"
description: "QuantLib::Parameter – Base class for model arguments."
---

<p>QuantLib::Parameter &#8211; Base class for model arguments. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/parameter.hpp&gt; </p>
<p> Inherited by <code>ConstantParameter</code>, <code>NullParameter</code>, <code>PiecewiseConstantParameter</code>, and <code>TermStructureFittingParameter</code>. </p>
<h3>Classes</h3>
<p>class <code>Impl</code><br />
 <i>Base class for model parameter implementation. </i></p>
<h3>Public Member Functions</h3>
<p>const <code>Array</code> &amp; <code>params</code> () const </p>
<p> void <code>setParam</code> (Size i, <code>Real</code> x) </p>
<p> bool <code>testParams</code> (const <code>Array</code> &amp;params) const </p>
<p> Size <code>size</code> () const </p>
<p> <code>Real</code> <code>operator()</code> (<code>Time</code> t) const </p>
<p> const boost::shared_ptr&lt; <code>Impl</code> &gt; &amp; <code>implementation</code> () const </p>
<h3>Protected Member Functions</h3>
<p><code>Parameter</code> (Size size, const boost::shared_ptr&lt; <code>Impl</code> &gt; &amp;impl, const <code>Constraint</code> &amp;constraint) </p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; <code>Impl</code> &gt; <code>impl_</code> </p>
<p> <code>Array</code> <code>params_</code> </p>
<p> <code>Constraint</code> <code>constraint_</code> </p>
<h2>Detailed Description</h2>
<p>Base class for model arguments. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
