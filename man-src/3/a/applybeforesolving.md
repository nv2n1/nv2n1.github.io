---
title: "applybeforesolving(3)"
name: "applybeforesolving"
section: "3"
letter: "a"
url: "/docs/linux/man/3-applybeforesolving/"
description: "QuantLib::BoundaryCondition – Abstract boundary condition class for finite difference problems."
---

<p>QuantLib::BoundaryCondition &#8211; Abstract boundary condition class for finite difference problems. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/methods/finitedifferences/boundarycondition.hpp&gt; </p>
<h3>Public Types</h3>
<p>enum <code>Side</code> { <code>None</code>, <code>Upper</code>, <code>Lower</code> } </p>
<p> typedef Operator <code>operator_type</code> </p>
<p> typedef Operator::array_type <code>array_type</code> </p>
<h3>Public Member Functions</h3>
<p>virtual void <code>applyBeforeApplying</code> (operator_type &amp;) const =0 </p>
<p> virtual void <code>applyAfterApplying</code> (array_type &amp;) const =0 </p>
<p> virtual void <code>applyBeforeSolving</code> (operator_type &amp;, array_type &amp;rhs) const =0 </p>
<p> virtual void <code>applyAfterSolving</code> (array_type &amp;) const =0 </p>
<p> virtual void <code>setTime</code> (<code>Time</code> t)=0 </p>
<h2>Detailed Description</h2>
<h3>template&lt;class Operator&gt; class QuantLib::BoundaryCondition&lt; Operator &gt;</h3>
<p>Abstract boundary condition class for finite difference problems. </p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>Side</code></h3>
<p><code>Possible enhancements</code></p>
<dl COMPACT>
<dd>Generalize for n-dimensional conditions</dl>
<h2>Member Function Documentation</h2>
<h3>virtual void applyBeforeApplying (operator_type &amp;) const [pure virtual]</h3>
<p>This method modifies an operator $ L $ before it is applied to an array $ u $ so that $ v = Lu $ will satisfy the given condition. </p>
<p> Implemented in <code>NeumannBC</code>, and <code>DirichletBC</code>.</p>
<h3>virtual void applyAfterApplying (array_type &amp;) const [pure virtual]</h3>
<p>This method modifies an array $ u $ so that it satisfies the given condition. </p>
<p> Implemented in <code>NeumannBC</code>, and <code>DirichletBC</code>.</p>
<h3>virtual void applyBeforeSolving (operator_type &amp;, array_type &amp; rhs) const [pure virtual]</h3>
<p>This method modifies an operator $ L $ before the linear system $ Lu&#8217; = u $ is solved so that $ u&#8217; $ will satisfy the given condition. </p>
<p> Implemented in <code>NeumannBC</code>, and <code>DirichletBC</code>.</p>
<h3>virtual void applyAfterSolving (array_type &amp;) const [pure virtual]</h3>
<p>This method modifies an array $ u $ so that it satisfies the given condition. </p>
<p> Implemented in <code>NeumannBC</code>, and <code>DirichletBC</code>.</p>
<h3>virtual void setTime (<code>Time</code> t) [pure virtual]</h3>
<p>This method sets the current time for time-dependent boundary conditions. </p>
<p> Implemented in <code>NeumannBC</code>, and <code>DirichletBC</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
