---
title: "quantlib_constraint(3)"
name: "quantlib_constraint"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_constraint/"
description: "QuantLib::Constraint – Base constraint class."
---

<p>QuantLib::Constraint &#8211; Base constraint class. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/optimization/constraint.hpp&gt; </p>
<p> Inherited by <code>BoundaryConstraint</code>, PrivateConstraint, <code>CompositeConstraint</code>, FellerConstraint, <code>NoConstraint</code>, and <code>PositiveConstraint</code>. </p>
<h3>Classes</h3>
<p>class <code>Impl</code><br />
 <i>Base class for constraint implementations. </i></p>
<h3>Public Member Functions</h3>
<p>bool <code>empty</code> () const </p>
<p> bool <code>test</code> (const <code>Array</code> &amp;p) const </p>
<p> <code>Real</code> <code>update</code> (<code>Array</code> &amp;p, const <code>Array</code> &amp;direction, <code>Real</code> beta) </p>
<p> <code>Constraint</code> (const boost::shared_ptr&lt; <code>Impl</code> &gt; &amp;impl=boost::shared_ptr&lt; <code>Impl</code> &gt;()) </p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; <code>Impl</code> &gt; <code>impl_</code> </p>
<h2>Detailed Description</h2>
<p>Base constraint class. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
