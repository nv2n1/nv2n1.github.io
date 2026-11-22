---

title: "setfirstrow(3)"
name: "setfirstrow"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setfirstrow/"
description: "QuantLib::TridiagonalOperator – Base implementation for tridiagonal operator."
---

<p>QuantLib::TridiagonalOperator &#8211; Base implementation for tridiagonal operator. </p>

<p> <br/>
 </p>
<p>#include &lt;ql/methods/finitedifferences/tridiagonaloperator.hpp&gt; </p>
<p>Inherited by <code>BSMOperator</code>, <code>DMinus</code>, <code>DPlus</code>, <code>DPlusDMinus</code>, <code>DZero</code>, and PdeOperator&lt; PdeClass &gt;. </p>
<h3>Classes</h3>
<p> <br/>
 class <code>TimeSetter</code> <br/>
 <i>encapsulation of time-setting logic </i>  </p>
<h3>Public Types</h3>
<p> <br/>
 typedef <code>Array</code> <code>array_type</code> <br/>
  </p>
<h3>Public Member Functions</h3>
<p> <br/>
 <code>TridiagonalOperator</code> (Size size=0) <br/>
 <br/>
 <code>TridiagonalOperator</code> (const <code>Array</code> &amp;low, const <code>Array</code> &amp;mid, const <code>Array</code> &amp;high) <br/>
 <br/>
 <code>TridiagonalOperator</code> (const <code>Disposable</code>&lt; <code>TridiagonalOperator</code> &gt; &amp;) <br/>
 <br/>
 <code>TridiagonalOperator</code> &amp; <code>operator=</code> (const <code>Disposable</code>&lt; <code>TridiagonalOperator</code> &gt; &amp;) <br/>
 </p>
<p> <code>Inspectors</code> <br/>
 </p>
<p> <br/>
 Size <code>size</code> () const <br/>
 <br/>
 bool <code>isTimeDependent</code> () <br/>
 <br/>
 const <code>Array</code> &amp; <code>lowerDiagonal</code> () const <br/>
 <br/>
 const <code>Array</code> &amp; <code>diagonal</code> () const <br/>
 <br/>
 const <code>Array</code> &amp; <code>upperDiagonal</code> () const <br/>
 </p>
<p> <code>Modifiers</code> <br/>
 </p>
<p> <br/>
 void <code>setFirstRow</code> (Real, Real) <br/>
 <br/>
 void <code>setMidRow</code> (Size, Real, Real, Real) <br/>
 <br/>
 void <code>setMidRows</code> (Real, Real, Real) <br/>
 <br/>
 void <code>setLastRow</code> (Real, Real) <br/>
 <br/>
 void <code>setTime</code> (Time t) <br/>
 </p>
<p> <code>Utilities</code> <br/>
 </p>
<p> <br/>
 void <code>swap</code> (<code>TridiagonalOperator</code> &amp;) <br/>
  </p>
<h3>Protected Attributes</h3>
<p> <br/>
 <code>Array</code> <code>diagonal_</code> <br/>
 <br/>
 <code>Array</code> <code>lowerDiagonal_</code> <br/>
 <br/>
 <code>Array</code> <code>upperDiagonal_</code> <br/>
 <br/>
 boost::shared_ptr&lt; <code>TimeSetter</code> &gt; <code>timeSetter_</code> <br/>
  </p>
<h3>Friends</h3>
<p> <br/>
 <code>Disposable</code>&lt; <code>TridiagonalOperator</code> &gt; <code>operator+</code> (const <code>TridiagonalOperator</code> &amp;) <br/>
 <br/>
 <code>Disposable</code>&lt; <code>TridiagonalOperator</code> &gt; <code>operator-</code> (const <code>TridiagonalOperator</code> &amp;) <br/>
 <br/>
 <code>Disposable</code>&lt; <code>TridiagonalOperator</code> &gt; <code>operator+</code> (const <code>TridiagonalOperator</code> &amp;, const <code>TridiagonalOperator</code> &amp;) <br/>
 <br/>
 <code>Disposable</code>&lt; <code>TridiagonalOperator</code> &gt; <code>operator-</code> (const <code>TridiagonalOperator</code> &amp;, const <code>TridiagonalOperator</code> &amp;) <br/>
 <br/>
 <code>Disposable</code>&lt; <code>TridiagonalOperator</code> &gt; <code>operator*</code> (Real, const <code>TridiagonalOperator</code> &amp;) <br/>
 <br/>
 <code>Disposable</code>&lt; <code>TridiagonalOperator</code> &gt; <code>operator*</code> (const <code>TridiagonalOperator</code> &amp;, Real) <br/>
 <br/>
 <code>Disposable</code>&lt; <code>TridiagonalOperator</code> &gt; <code>operator/</code> (const <code>TridiagonalOperator</code> &amp;, Real) <br/>
  </p>
<h3>Operator interface</h3>
<p> <br/>
 <code>Disposable</code>&lt; <code>Array</code> &gt; <code>applyTo</code> (const <code>Array</code> &amp;v) const <br/>
 <i>apply operator to a given array </i> <br/>
 <code>Disposable</code>&lt; <code>Array</code> &gt; <code>solveFor</code> (const <code>Array</code> &amp;rhs) const <br/>
 <i>solve linear system for a given right-hand side </i> <br/>
 <code>Disposable</code>&lt; <code>Array</code> &gt; <code>SOR</code> (const <code>Array</code> &amp;rhs, Real tol) const <br/>
 <i>solve linear system with SOR approach </i> <br/>
 static <code>Disposable</code>&lt; <code>TridiagonalOperator</code> &gt; <code>identity</code> (Size size) <br/>
 <i>identity instance </i>  </p>
<h2>Detailed Description</h2>
<p>Base implementation for tridiagonal operator. </p>
<p> <code>Warning</code> </p>
<dl>
<dd> <p> to use real time-dependant algebra, you must overload the corresponding operators in the inheriting time-dependent class. </p>
 </dd></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code. </p>
