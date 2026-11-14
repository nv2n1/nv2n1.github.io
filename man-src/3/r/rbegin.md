---
title: "rbegin(3)"
name: "rbegin"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rbegin/"
description: "QuantLib::Array – 1-D array used in linear algebra."
---

<p>QuantLib::Array &#8211; 1-D array used in linear algebra. </p>
<h2>Synopsis</h2>
<pre><code>void swap (Array &amp;)



Related Functions

(Note that these are not member functions.)


Real DotProduct (const Array &amp;, const Array &amp;)



const Disposable&lt; Array &gt; operator+ (const Array &amp;v)



const Disposable&lt; Array &gt; operator- (const Array &amp;v)



const Disposable&lt; Array &gt; operator+ (const Array &amp;, const Array &amp;)



const Disposable&lt; Array &gt; operator+ (const Array &amp;, Real)



const Disposable&lt; Array &gt; operator+ (Real, const Array &amp;)



const Disposable&lt; Array &gt; operator- (const Array &amp;, const Array &amp;)



const Disposable&lt; Array &gt; operator- (const Array &amp;, Real)



const Disposable&lt; Array &gt; operator- (Real, const Array &amp;)



const Disposable&lt; Array &gt; operator* (const Array &amp;, const Array &amp;)



const Disposable&lt; Array &gt; operator* (const Array &amp;, Real)



const Disposable&lt; Array &gt; operator* (Real, const Array &amp;)



const Disposable&lt; Array &gt; operator/ (const Array &amp;, const Array &amp;)



const Disposable&lt; Array &gt; operator/ (const Array &amp;, Real)



const Disposable&lt; Array &gt; operator/ (Real, const Array &amp;)



const Disposable&lt; Array &gt; Abs (const Array &amp;)



const Disposable&lt; Array &gt; Sqrt (const Array &amp;)



const Disposable&lt; Array &gt; Log (const Array &amp;)



const Disposable&lt; Array &gt; Exp (const Array &amp;)



void swap (Array &amp;, Array &amp;)



std::ostream &amp; operator&lt;&lt; (std::ostream &amp;, const Array &amp;)</code></pre>
<h3>Public Types</h3>
<p>typedef Real <code>value_type</code> </p>
<p> typedef Real * <code>iterator</code> </p>
<p> typedef const Real * <code>const_iterator</code> </p>
<p> typedef boost::reverse_iterator&lt; iterator &gt; <code>reverse_iterator</code> </p>
<p> typedef boost::reverse_iterator&lt; const_iterator &gt; <code>const_reverse_iterator</code></p>
<h3>Public Member Functions</h3>
<p><code>Constructors, destructor, and assignment</code><br />
 void swap (Array &amp;)</p>
<p>Related Functions</p>
<p>(Note that these are not member functions.)</p>
<p>Real DotProduct (const Array &amp;, const Array &amp;)</p>
<p>const Disposable&lt; Array &gt; operator+ (const Array &amp;v)</p>
<p>const Disposable&lt; Array &gt; operator- (const Array &amp;v)</p>
<p>const Disposable&lt; Array &gt; operator+ (const Array &amp;, const Array &amp;)</p>
<p>const Disposable&lt; Array &gt; operator+ (const Array &amp;, Real)</p>
<p>const Disposable&lt; Array &gt; operator+ (Real, const Array &amp;)</p>
<p>const Disposable&lt; Array &gt; operator- (const Array &amp;, const Array &amp;)</p>
<p>const Disposable&lt; Array &gt; operator- (const Array &amp;, Real)</p>
<p>const Disposable&lt; Array &gt; operator- (Real, const Array &amp;)</p>
<p>const Disposable&lt; Array &gt; operator* (const Array &amp;, const Array &amp;)</p>
<p>const Disposable&lt; Array &gt; operator* (const Array &amp;, Real)</p>
<p>const Disposable&lt; Array &gt; operator* (Real, const Array &amp;)</p>
<p>const Disposable&lt; Array &gt; operator/ (const Array &amp;, const Array &amp;)</p>
<p>const Disposable&lt; Array &gt; operator/ (const Array &amp;, Real)</p>
<p>const Disposable&lt; Array &gt; operator/ (Real, const Array &amp;)</p>
<p>const Disposable&lt; Array &gt; Abs (const Array &amp;)</p>
<p>const Disposable&lt; Array &gt; Sqrt (const Array &amp;)</p>
<p>const Disposable&lt; Array &gt; Log (const Array &amp;)</p>
<p>const Disposable&lt; Array &gt; Exp (const Array &amp;)</p>
<p>void swap (Array &amp;, Array &amp;)</p>
<p>std::ostream &amp; operator&lt;&lt; (std::ostream &amp;, const Array &amp;) <code>Vector algebra</code><br />
 v += x and similar operation involving a scalar value are shortcuts for $ rall i : v_i = v_i + x $ v *= w and similar operation involving two vectors are shortcuts for $ rall i : v_i = v_i imes w_i $ <code>Precondition:</code></p>
<dl>
<dd>all arrays involved in an algebraic expression must have the same size.</dl>
<p> void swap (Array &amp;)</p>
<p>Related Functions</p>
<p>(Note that these are not member functions.)</p>
<p>Real DotProduct (const Array &amp;, const Array &amp;)</p>
<p>const Disposable&lt; Array &gt; operator+ (const Array &amp;v)</p>
<p>const Disposable&lt; Array &gt; operator- (const Array &amp;v)</p>
<p>const Disposable&lt; Array &gt; operator+ (const Array &amp;, const Array &amp;)</p>
<p>const Disposable&lt; Array &gt; operator+ (const Array &amp;, Real)</p>
<p>const Disposable&lt; Array &gt; operator+ (Real, const Array &amp;)</p>
<p>const Disposable&lt; Array &gt; operator- (const Array &amp;, const Array &amp;)</p>
<p>const Disposable&lt; Array &gt; operator- (const Array &amp;, Real)</p>
<p>const Disposable&lt; Array &gt; operator- (Real, const Array &amp;)</p>
<p>const Disposable&lt; Array &gt; operator* (const Array &amp;, const Array &amp;)</p>
<p>const Disposable&lt; Array &gt; operator* (const Array &amp;, Real)</p>
<p>const Disposable&lt; Array &gt; operator* (Real, const Array &amp;)</p>
<p>const Disposable&lt; Array &gt; operator/ (const Array &amp;, const Array &amp;)</p>
<p>const Disposable&lt; Array &gt; operator/ (const Array &amp;, Real)</p>
<p>const Disposable&lt; Array &gt; operator/ (Real, const Array &amp;)</p>
<p>const Disposable&lt; Array &gt; Abs (const Array &amp;)</p>
<p>const Disposable&lt; Array &gt; Sqrt (const Array &amp;)</p>
<p>const Disposable&lt; Array &gt; Log (const Array &amp;)</p>
<p>const Disposable&lt; Array &gt; Exp (const Array &amp;)</p>
<p>void swap (Array &amp;, Array &amp;)</p>
<p>std::ostream &amp; operator&lt;&lt; (std::ostream &amp;, const Array &amp;) <code>Element access</code> </p>
<p> Real <code>operator[]</code> (Size) const<br />
 <i>read-only </i><br />
 Real <code>at</code> (Size) const </p>
<p> Real <code>front</code> () const </p>
<p> Real <code>back</code> () const </p>
<p> Real &amp; <code>operator[]</code> (Size)<br />
 <i>read-write </i><br />
 Real &amp; <code>at</code> (Size) </p>
<p> Real &amp; <code>front</code> () </p>
<p> Real &amp; <code>back</code> ()<br />
 <code>Inspectors</code> </p>
<p> Size <code>size</code> () const<br />
 <i>dimension of the array </i><br />
 bool <code>empty</code> () const<br />
 <i>whether the array is empty </i> <code>Iterator access</code> </p>
<p> const_iterator <code>begin</code> () const </p>
<p> iterator <code>begin</code> () </p>
<p> const_iterator <code>end</code> () const </p>
<p> iterator <code>end</code> () </p>
<p> const_reverse_iterator <code>rbegin</code> () const </p>
<p> reverse_iterator <code>rbegin</code> () </p>
<p> const_reverse_iterator <code>rend</code> () const </p>
<p> reverse_iterator <code>rend</code> ()<br />
 <code>Utilities</code> </p>
<pre><code>void swap (Array &amp;)



Related Functions

(Note that these are not member functions.)


Real DotProduct (const Array &amp;, const Array &amp;)



const Disposable&lt; Array &gt; operator+ (const Array &amp;v)



const Disposable&lt; Array &gt; operator- (const Array &amp;v)



const Disposable&lt; Array &gt; operator+ (const Array &amp;, const Array &amp;)



const Disposable&lt; Array &gt; operator+ (const Array &amp;, Real)



const Disposable&lt; Array &gt; operator+ (Real, const Array &amp;)



const Disposable&lt; Array &gt; operator- (const Array &amp;, const Array &amp;)



const Disposable&lt; Array &gt; operator- (const Array &amp;, Real)



const Disposable&lt; Array &gt; operator- (Real, const Array &amp;)



const Disposable&lt; Array &gt; operator* (const Array &amp;, const Array &amp;)



const Disposable&lt; Array &gt; operator* (const Array &amp;, Real)



const Disposable&lt; Array &gt; operator* (Real, const Array &amp;)



const Disposable&lt; Array &gt; operator/ (const Array &amp;, const Array &amp;)



const Disposable&lt; Array &gt; operator/ (const Array &amp;, Real)



const Disposable&lt; Array &gt; operator/ (Real, const Array &amp;)



const Disposable&lt; Array &gt; Abs (const Array &amp;)



const Disposable&lt; Array &gt; Sqrt (const Array &amp;)



const Disposable&lt; Array &gt; Log (const Array &amp;)



const Disposable&lt; Array &gt; Exp (const Array &amp;)



void swap (Array &amp;, Array &amp;)



std::ostream &amp; operator&lt;&lt; (std::ostream &amp;, const Array &amp;)</code></pre>
<h2>Detailed Description</h2>
<p>1-D array used in linear algebra. </p>
<p> This class implements the concept of vector as used in linear algebra. As such, it is <code>not</code> meant to be used as a container &#8211; std::vector should be used instead. </p>
<p> <code>Tests</code></p>
<dl>
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
