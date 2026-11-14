---
title: "quantlib_dirichletbc(3)"
name: "quantlib_dirichletbc"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_dirichletbc/"
description: "QuantLib::DirichletBC – Neumann boundary condition (i.e., constant value)."
---

<p>QuantLib::DirichletBC &#8211; Neumann boundary condition (i.e., constant value). </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/methods/finitedifferences/boundarycondition.hpp&gt; </p>
<p> Inherits <code>BoundaryCondition&lt; TridiagonalOperator &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>DirichletBC</code> (<code>Real</code> value, <code>Side</code> side) </p>
<p> void <code>applyBeforeApplying</code> (<code>TridiagonalOperator</code> &amp;) const </p>
<p> void <code>applyAfterApplying</code> (<code>Array</code> &amp;) const </p>
<p> void <code>applyBeforeSolving</code> (<code>TridiagonalOperator</code> &amp;, <code>Array</code> &amp;rhs) const </p>
<p> void <code>applyAfterSolving</code> (<code>Array</code> &amp;) const </p>
<p> void <code>setTime</code> (Time) </p>
<h2>Detailed Description</h2>
<p>Neumann boundary condition (i.e., constant value). </p>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>generalize to time-dependent conditions.</dl>
<h2>Member Function Documentation</h2>
<h3>void applyBeforeApplying (<code>TridiagonalOperator</code> &amp;) const [virtual]</h3>
<p>This method modifies an operator $ L $ before it is applied to an array $ u $ so that $ v = Lu $ will satisfy the given condition. </p>
<p> Implements <code>BoundaryCondition&lt; TridiagonalOperator &gt;</code>.</p>
<h3>void applyAfterApplying (<code>Array</code> &amp;) const [virtual]</h3>
<p>This method modifies an array $ u $ so that it satisfies the given condition. </p>
<p> Implements <code>BoundaryCondition&lt; TridiagonalOperator &gt;</code>.</p>
<h3>void applyBeforeSolving (<code>TridiagonalOperator</code> &amp;, <code>Array</code> &amp; rhs) const [virtual]</h3>
<p>This method modifies an operator $ L $ before the linear system $ Lu&#8217; = u $ is solved so that $ u&#8217; $ will satisfy the given condition. </p>
<p> Implements <code>BoundaryCondition&lt; TridiagonalOperator &gt;</code>.</p>
<h3>void applyAfterSolving (<code>Array</code> &amp;) const [virtual]</h3>
<p>This method modifies an array $ u $ so that it satisfies the given condition. </p>
<p> Implements <code>BoundaryCondition&lt; TridiagonalOperator &gt;</code>.</p>
<h3>void setTime (Time t) [virtual]</h3>
<p>This method sets the current time for time-dependent boundary conditions. </p>
<p> Implements <code>BoundaryCondition&lt; TridiagonalOperator &gt;</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
