---
title: "ql-constraint(3)"
name: "ql-constraint"
section: "3"
letter: "q"
url: "/docs/linux/man/3-ql-constraint/"
description: "QuantLib::Constraint – Base constraint class."
---

<p>QuantLib::Constraint &#8211; Base constraint class. </p>
<h2>Synopsis</h2>
<pre><code>bool empty () const



bool test (const Array &amp;p) const



Real update (Array &amp;p, const Array &amp;direction, Real beta)



Constraint (const boost::shared_ptr&lt; Impl &gt; &amp;impl=boost::shared_ptr&lt; Impl &gt;())



Protected Attributes</code></pre>
<p> Inherited by <code>BoundaryConstraint</code>, PrivateConstraint, <code>CompositeConstraint</code>, FellerConstraint, <code>NoConstraint</code>, and <code>PositiveConstraint</code>.</p>
<h3>Classes</h3>
<p>class <code>Impl</code><br />
 <i>Base class for constraint implementations. </i></p>
<h3>Public Member Functions</h3>
<pre><code>bool empty () const



bool test (const Array &amp;p) const



Real update (Array &amp;p, const Array &amp;direction, Real beta)



Constraint (const boost::shared_ptr&lt; Impl &gt; &amp;impl=boost::shared_ptr&lt; Impl &gt;())



Protected Attributes</code></pre>
<p> boost::shared_ptr&lt; <code>Impl</code> &gt; <code>impl_</code></p>
<h2>Detailed Description</h2>
<p>Base constraint class.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
