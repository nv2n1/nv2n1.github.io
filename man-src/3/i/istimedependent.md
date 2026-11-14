---
title: "istimedependent(3)"
name: "istimedependent"
section: "3"
letter: "i"
url: "/docs/linux/man/3-istimedependent/"
description: "QuantLib::TridiagonalOperator – Base implementation for tridiagonal operator."
---

<p>QuantLib::TridiagonalOperator &#8211; Base implementation for tridiagonal operator. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/methods/finitedifferences/tridiagonaloperator.hpp&gt; </p>
<p> Inherited by <code>BSMOperator</code>, <code>DMinus</code>, <code>DPlus</code>, <code>DPlusDMinus</code>, <code>DZero</code>, and PdeOperator&lt; PdeClass &gt;. </p>
<h3>Classes</h3>
<p>class <code>TimeSetter</code><br />
 <i>encapsulation of time-setting logic </i></p>
<h3>Public Types</h3>
<p>typedef <code>Array</code> <code>array_type</code> </p>
<h3>Public Member Functions</h3>
<p><code>TridiagonalOperator</code> (Size size=0) </p>
<p> <code>TridiagonalOperator</code> (const <code>Array</code> &amp;low, const <code>Array</code> &amp;mid, const <code>Array</code> &amp;high) </p>
<p> <code>TridiagonalOperator</code> (const <code>Disposable</code>&lt; <code>TridiagonalOperator</code> &gt; &amp;) </p>
<p> <code>TridiagonalOperator</code> &amp; <code>operator=</code> (const <code>Disposable</code>&lt; <code>TridiagonalOperator</code> &gt; &amp;) </p>
<p> <code>Inspectors</code> </p>
<p> Size <code>size</code> () const </p>
<p> bool <code>isTimeDependent</code> () </p>
<p> const <code>Array</code> &amp; <code>lowerDiagonal</code> () const </p>
<p> const <code>Array</code> &amp; <code>diagonal</code> () const </p>
<p> const <code>Array</code> &amp; <code>upperDiagonal</code> () const </p>
<p> <code>Modifiers</code> </p>
<p> void <code>setFirstRow</code> (Real, Real) </p>
<p> void <code>setMidRow</code> (Size, Real, Real, Real) </p>
<p> void <code>setMidRows</code> (Real, Real, Real) </p>
<p> void <code>setLastRow</code> (Real, Real) </p>
<p> void <code>setTime</code> (Time t) </p>
<p> <code>Utilities</code> </p>
<p> void <code>swap</code> (<code>TridiagonalOperator</code> &amp;) </p>
<h3>Protected Attributes</h3>
<p><code>Array</code> <code>diagonal_</code> </p>
<p> <code>Array</code> <code>lowerDiagonal_</code> </p>
<p> <code>Array</code> <code>upperDiagonal_</code> </p>
<p> boost::shared_ptr&lt; <code>TimeSetter</code> &gt; <code>timeSetter_</code> </p>
<h3>Friends</h3>
<p><code>Disposable</code>&lt; <code>TridiagonalOperator</code> &gt; <code>operator+</code> (const <code>TridiagonalOperator</code> &amp;) </p>
<p> <code>Disposable</code>&lt; <code>TridiagonalOperator</code> &gt; <code>operator-</code> (const <code>TridiagonalOperator</code> &amp;) </p>
<p> <code>Disposable</code>&lt; <code>TridiagonalOperator</code> &gt; <code>operator+</code> (const <code>TridiagonalOperator</code> &amp;, const <code>TridiagonalOperator</code> &amp;) </p>
<p> <code>Disposable</code>&lt; <code>TridiagonalOperator</code> &gt; <code>operator-</code> (const <code>TridiagonalOperator</code> &amp;, const <code>TridiagonalOperator</code> &amp;) </p>
<p> <code>Disposable</code>&lt; <code>TridiagonalOperator</code> &gt; <code>operator*</code> (Real, const <code>TridiagonalOperator</code> &amp;) </p>
<p> <code>Disposable</code>&lt; <code>TridiagonalOperator</code> &gt; <code>operator*</code> (const <code>TridiagonalOperator</code> &amp;, Real) </p>
<p> <code>Disposable</code>&lt; <code>TridiagonalOperator</code> &gt; <code>operator/</code> (const <code>TridiagonalOperator</code> &amp;, Real) </p>
<h3>Operator interface</h3>
<p><code>Disposable</code>&lt; <code>Array</code> &gt; <code>applyTo</code> (const <code>Array</code> &amp;v) const<br />
 <i>apply operator to a given array </i><br />
 <code>Disposable</code>&lt; <code>Array</code> &gt; <code>solveFor</code> (const <code>Array</code> &amp;rhs) const<br />
 <i>solve linear system for a given right-hand side </i><br />
 <code>Disposable</code>&lt; <code>Array</code> &gt; <code>SOR</code> (const <code>Array</code> &amp;rhs, Real tol) const<br />
 <i>solve linear system with SOR approach </i><br />
 static <code>Disposable</code>&lt; <code>TridiagonalOperator</code> &gt; <code>identity</code> (Size size)<br />
 <i>identity instance </i></p>
<h2>Detailed Description</h2>
<p>Base implementation for tridiagonal operator. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>to use real time-dependant algebra, you must overload the corresponding operators in the inheriting time-dependent class.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
