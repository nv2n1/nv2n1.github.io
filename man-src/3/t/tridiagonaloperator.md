---
title: "tridiagonaloperator(3)"
name: "tridiagonaloperator"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tridiagonaloperator/"
description: "ql/methods/finitedifferences/tridiagonaloperator.hpp – tridiagonal operator"
---

<p>ql/methods/finitedifferences/tridiagonaloperator.hpp &#8211; tridiagonal operator </p>
<h2>Synopsis</h2>
<pre><code>void swap (TridiagonalOperator &amp;, TridiagonalOperator &amp;)



Disposable&lt; TridiagonalOperator &gt; operator+ (const TridiagonalOperator &amp;D)



Disposable&lt; TridiagonalOperator &gt; operator- (const TridiagonalOperator &amp;D)



Disposable&lt; TridiagonalOperator &gt; operator+ (const TridiagonalOperator &amp;D1, const TridiagonalOperator &amp;D2)



Disposable&lt; TridiagonalOperator &gt; operator- (const TridiagonalOperator &amp;D1, const TridiagonalOperator &amp;D2)



Disposable&lt; TridiagonalOperator &gt; operator* (Real a, const TridiagonalOperator &amp;D)



Disposable&lt; TridiagonalOperator &gt; operator* (const TridiagonalOperator &amp;D, Real a)



Disposable&lt; TridiagonalOperator &gt; operator/ (const TridiagonalOperator &amp;D, Real a)</code></pre>
<h3>Classes</h3>
<p>class <code>TridiagonalOperator</code><br />
 <i>Base implementation for tridiagonal operator. </i><br />
 class <code>TimeSetter</code><br />
 <i>encapsulation of time-setting logic </i></p>
<h3>Functions</h3>
<pre><code>void swap (TridiagonalOperator &amp;, TridiagonalOperator &amp;)



Disposable&lt; TridiagonalOperator &gt; operator+ (const TridiagonalOperator &amp;D)



Disposable&lt; TridiagonalOperator &gt; operator- (const TridiagonalOperator &amp;D)



Disposable&lt; TridiagonalOperator &gt; operator+ (const TridiagonalOperator &amp;D1, const TridiagonalOperator &amp;D2)



Disposable&lt; TridiagonalOperator &gt; operator- (const TridiagonalOperator &amp;D1, const TridiagonalOperator &amp;D2)



Disposable&lt; TridiagonalOperator &gt; operator* (Real a, const TridiagonalOperator &amp;D)



Disposable&lt; TridiagonalOperator &gt; operator* (const TridiagonalOperator &amp;D, Real a)



Disposable&lt; TridiagonalOperator &gt; operator/ (const TridiagonalOperator &amp;D, Real a)</code></pre>
<h2>Detailed Description</h2>
<p>tridiagonal operator</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
