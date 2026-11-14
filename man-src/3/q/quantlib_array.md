---
title: "quantlib_array(3)"
name: "quantlib_array"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_array/"
description: "QuantLib::Array – 1-D array used in linear algebra."
---

<p>QuantLib::Array &#8211; 1-D array used in linear algebra. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/array.hpp&gt; </p>
<h3>Public Types</h3>
<p>typedef Real <code>value_type</code> </p>
<p> typedef Real * <code>iterator</code> </p>
<p> typedef const Real * <code>const_iterator</code> </p>
<p> typedef boost::reverse_iterator&lt; iterator &gt; <code>reverse_iterator</code> </p>
<p> typedef boost::reverse_iterator&lt; const_iterator &gt; <code>const_reverse_iterator</code> </p>
<h3>Public Member Functions</h3>
<p><code>Constructors, destructor, and assignment</code> </p>
<p> <code>Array</code> (Size size=0)<br />
 <i>creates the array with the given dimension </i><br />
 <code>Array</code> (Size size, Real value)<br />
 <i>creates the array and fills it with </i>value<br />
 <code>Array</code> (Size size, Real value, Real increment)<br />
 <i>creates the array and fills it according to $ a_{0} = value, a_{i}=a_{i-1}+increment $ </i><br />
 <code>Array</code> (const <code>Array</code> &amp;) </p>
<p> <code>Array</code> (const <code>Disposable</code>&lt; <code>Array</code> &gt; &amp;) </p>
<p> <code>Array</code> (const std::vector&lt; Real &gt; &amp;)<br />
 <i>creates the array as a copy of a given stl vector </i><br />
 <code>Array</code> &amp; <code>operator=</code> (const <code>Array</code> &amp;) </p>
<p> <code>Array</code> &amp; <code>operator=</code> (const <code>Disposable</code>&lt; <code>Array</code> &gt; &amp;) </p>
<p> bool <code>operator==</code> (const <code>Array</code> &amp;) const </p>
<p> bool <code>operator!=</code> (const <code>Array</code> &amp;) const </p>
<p> <code>Vector algebra</code><br />
 v += x and similar operation involving a scalar value are shortcuts for $ rall i : v_i = v_i + x $ </p>
<p> v *= w and similar operation involving two vectors are shortcuts for $ rall i : v_i = v_i imes w_i $ </p>
<p> <code>Precondition:</code></p>
<dl COMPACT>
<dd>all arrays involved in an algebraic expression must have the same size.</dl>
<p> const <code>Array</code> &amp; <code>operator+=</code> (const <code>Array</code> &amp;) </p>
<p> const <code>Array</code> &amp; <code>operator+=</code> (Real) </p>
<p> const <code>Array</code> &amp; <code>operator-=</code> (const <code>Array</code> &amp;) </p>
<p> const <code>Array</code> &amp; <code>operator-=</code> (Real) </p>
<p> const <code>Array</code> &amp; <code>operator*=</code> (const <code>Array</code> &amp;) </p>
<p> const <code>Array</code> &amp; <code>operator*=</code> (Real) </p>
<p> const <code>Array</code> &amp; <code>operator/=</code> (const <code>Array</code> &amp;) </p>
<p> const <code>Array</code> &amp; <code>operator/=</code> (Real) </p>
<p> <code>Element access</code> </p>
<p> Real <code>operator[]</code> (Size) const<br />
 <i>read-only </i><br />
 Real <code>at</code> (Size) const </p>
<p> Real <code>front</code> () const </p>
<p> Real <code>back</code> () const </p>
<p> Real &amp; <code>operator[]</code> (Size)<br />
 <i>read-write </i><br />
 Real &amp; <code>at</code> (Size) </p>
<p> Real &amp; <code>front</code> () </p>
<p> Real &amp; <code>back</code> () </p>
<p> <code>Inspectors</code> </p>
<p> Size <code>size</code> () const<br />
 <i>dimension of the array </i><br />
 bool <code>empty</code> () const<br />
 <i>whether the array is empty </i> </p>
<p> <code>Iterator access</code> </p>
<p> const_iterator <code>begin</code> () const </p>
<p> iterator <code>begin</code> () </p>
<p> const_iterator <code>end</code> () const </p>
<p> iterator <code>end</code> () </p>
<p> const_reverse_iterator <code>rbegin</code> () const </p>
<p> reverse_iterator <code>rbegin</code> () </p>
<p> const_reverse_iterator <code>rend</code> () const </p>
<p> reverse_iterator <code>rend</code> () </p>
<p> <code>Utilities</code> </p>
<p> void <code>swap</code> (<code>Array</code> &amp;) </p>
<h3>Related Functions</h3>
<p>(Note that these are not member functions.)<br />
 Real <code>DotProduct</code> (const <code>Array</code> &amp;, const <code>Array</code> &amp;) </p>
<p> const <code>Disposable</code>&lt; <code>Array</code> &gt; <code>operator+</code> (const <code>Array</code> &amp;v) </p>
<p> const <code>Disposable</code>&lt; <code>Array</code> &gt; <code>operator-</code> (const <code>Array</code> &amp;v) </p>
<p> const <code>Disposable</code>&lt; <code>Array</code> &gt; <code>operator+</code> (const <code>Array</code> &amp;, const <code>Array</code> &amp;) </p>
<p> const <code>Disposable</code>&lt; <code>Array</code> &gt; <code>operator+</code> (const <code>Array</code> &amp;, Real) </p>
<p> const <code>Disposable</code>&lt; <code>Array</code> &gt; <code>operator+</code> (Real, const <code>Array</code> &amp;) </p>
<p> const <code>Disposable</code>&lt; <code>Array</code> &gt; <code>operator-</code> (const <code>Array</code> &amp;, const <code>Array</code> &amp;) </p>
<p> const <code>Disposable</code>&lt; <code>Array</code> &gt; <code>operator-</code> (const <code>Array</code> &amp;, Real) </p>
<p> const <code>Disposable</code>&lt; <code>Array</code> &gt; <code>operator-</code> (Real, const <code>Array</code> &amp;) </p>
<p> const <code>Disposable</code>&lt; <code>Array</code> &gt; <code>operator*</code> (const <code>Array</code> &amp;, const <code>Array</code> &amp;) </p>
<p> const <code>Disposable</code>&lt; <code>Array</code> &gt; <code>operator*</code> (const <code>Array</code> &amp;, Real) </p>
<p> const <code>Disposable</code>&lt; <code>Array</code> &gt; <code>operator*</code> (Real, const <code>Array</code> &amp;) </p>
<p> const <code>Disposable</code>&lt; <code>Array</code> &gt; <code>operator/</code> (const <code>Array</code> &amp;, const <code>Array</code> &amp;) </p>
<p> const <code>Disposable</code>&lt; <code>Array</code> &gt; <code>operator/</code> (const <code>Array</code> &amp;, Real) </p>
<p> const <code>Disposable</code>&lt; <code>Array</code> &gt; <code>operator/</code> (Real, const <code>Array</code> &amp;) </p>
<p> const <code>Disposable</code>&lt; <code>Array</code> &gt; <code>Abs</code> (const <code>Array</code> &amp;) </p>
<p> const <code>Disposable</code>&lt; <code>Array</code> &gt; <code>Sqrt</code> (const <code>Array</code> &amp;) </p>
<p> const <code>Disposable</code>&lt; <code>Array</code> &gt; <code>Log</code> (const <code>Array</code> &amp;) </p>
<p> const <code>Disposable</code>&lt; <code>Array</code> &gt; <code>Exp</code> (const <code>Array</code> &amp;) </p>
<p> void <code>swap</code> (<code>Array</code> &amp;, <code>Array</code> &amp;) </p>
<p> std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, const <code>Array</code> &amp;) </p>
<h2>Detailed Description</h2>
<p>1-D array used in linear algebra. </p>
<p> This class implements the concept of vector as used in linear algebra. As such, it is <code>not</code> meant to be used as a container &#8211; std::vector should be used instead. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>construction of arrays is checked in a number of cases</dl>
<h2>Friends And Related Function Documentation</h2>
<h3>Real DotProduct (const <code>Array</code> &amp;, const <code>Array</code> &amp;) [related]</h3>
<h3>const <code>Disposable</code>&lt; <code>Array</code> &gt; operator+ (const <code>Array</code> &amp; v) [related]</h3>
<h3>const <code>Disposable</code>&lt; <code>Array</code> &gt; operator- (const <code>Array</code> &amp; v) [related]</h3>
<h3>const <code>Disposable</code>&lt; <code>Array</code> &gt; operator+ (const <code>Array</code> &amp;, const <code>Array</code> &amp;) [related]</h3>
<h3>const <code>Disposable</code>&lt; <code>Array</code> &gt; operator+ (const <code>Array</code> &amp;, Real) [related]</h3>
<h3>const <code>Disposable</code>&lt; <code>Array</code> &gt; operator+ (Real, const <code>Array</code> &amp;) [related]</h3>
<h3>const <code>Disposable</code>&lt; <code>Array</code> &gt; operator- (const <code>Array</code> &amp;, const <code>Array</code> &amp;) [related]</h3>
<h3>const <code>Disposable</code>&lt; <code>Array</code> &gt; operator- (const <code>Array</code> &amp;, Real) [related]</h3>
<h3>const <code>Disposable</code>&lt; <code>Array</code> &gt; operator- (Real, const <code>Array</code> &amp;) [related]</h3>
<h3>const <code>Disposable</code>&lt; <code>Array</code> &gt; operator* (const <code>Array</code> &amp;, const <code>Array</code> &amp;) [related]</h3>
<h3>const <code>Disposable</code>&lt; <code>Array</code> &gt; operator* (const <code>Array</code> &amp;, Real) [related]</h3>
<h3>const <code>Disposable</code>&lt; <code>Array</code> &gt; operator* (Real, const <code>Array</code> &amp;) [related]</h3>
<h3>const <code>Disposable</code>&lt; <code>Array</code> &gt; operator/ (const <code>Array</code> &amp;, const <code>Array</code> &amp;) [related]</h3>
<h3>const <code>Disposable</code>&lt; <code>Array</code> &gt; operator/ (const <code>Array</code> &amp;, Real) [related]</h3>
<h3>const <code>Disposable</code>&lt; <code>Array</code> &gt; operator/ (Real, const <code>Array</code> &amp;) [related]</h3>
<h3>const <code>Disposable</code>&lt; <code>Array</code> &gt; Abs (const <code>Array</code> &amp;) [related]</h3>
<h3>const <code>Disposable</code>&lt; <code>Array</code> &gt; Sqrt (const <code>Array</code> &amp;) [related]</h3>
<h3>const <code>Disposable</code>&lt; <code>Array</code> &gt; Log (const <code>Array</code> &amp;) [related]</h3>
<h3>const <code>Disposable</code>&lt; <code>Array</code> &gt; Exp (const <code>Array</code> &amp;) [related]</h3>
<h3>void swap (<code>Array</code> &amp;, <code>Array</code> &amp;) [related]</h3>
<p><code>Examples: </code> <code>BermudanSwaption.cpp</code>.</p>
<h3>std::ostream &amp; operator&lt;&lt; (std::ostream &amp;, const <code>Array</code> &amp;) [related]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
