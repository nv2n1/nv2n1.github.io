---
title: "front(3)"
name: "front"
section: "3"
letter: "f"
url: "/docs/linux/man/3-front/"
---

<h2 class="name">NAME</h2>
 

 QuantLib::Array - 1-D array used in linear algebra. 

<h2>SYNOPSIS</h2>

 
 

 #include &lt;ql/math/array.hpp&gt; 

<h3>Public Types</h3>

 

 
 typedef Real <b>value_type</b> 
 
 typedef Real * <b>iterator</b> 
 
 typedef const Real * <b>const_iterator</b> 
 
 typedef boost::reverse_iterator&lt; iterator &gt; <b>reverse_iterator</b> 
 
 typedef boost::reverse_iterator&lt; const_iterator &gt; <b>const_reverse_iterator</b> 

<h3>Public Member Functions</h3>

 

 

 <b>Constructors, destructor, and assignment</b> 
 

 
 <b>Array</b> (Size size=0) 
 <i>creates the array with the given dimension </i> 
 <b>Array</b> (Size size, Real value) 
 <i>creates the array and fills it with </i>value 
 <b>Array</b> (Size size, Real value, Real increment) 
 <i>creates the array and fills it according to $ a_{0} = value, a_{i}=a_{i-1}+increment $ </i> 
 <b>Array</b> (const <b>Array</b> &amp;) 
 
 <b>Array</b> (const <b>Disposable</b>&lt; <b>Array</b> &gt; &amp;) 
 
 <b>Array</b> (const std::vector&lt; Real &gt; &amp;) 
 <i>creates the array as a copy of a given stl vector </i> 
 <b>Array</b> &amp; <b>operator=</b> (const <b>Array</b> &amp;) 
 
 <b>Array</b> &amp; <b>operator=</b> (const <b>Disposable</b>&lt; <b>Array</b> &gt; &amp;) 
 
 bool <b>operator==</b> (const <b>Array</b> &amp;) const 
 
 bool <b>operator!=</b> (const <b>Array</b> &amp;) const 
 

 <b>Vector algebra</b> 
 v += x and similar operation involving a scalar value are shortcuts for $ rall i : v_i = v_i + x $ 

 v *= w and similar operation involving two vectors are shortcuts for $ rall i : v_i = v_i imes w_i $ 

 <b>Precondition:</b>
<dl>
<dt>
<dd> all arrays involved in an algebraic expression must have the same size.</dl>
 

 

 

 
 const <b>Array</b> &amp; <b>operator+=</b> (const <b>Array</b> &amp;) 
 
 const <b>Array</b> &amp; <b>operator+=</b> (Real) 
 
 const <b>Array</b> &amp; <b>operator-=</b> (const <b>Array</b> &amp;) 
 
 const <b>Array</b> &amp; <b>operator-=</b> (Real) 
 
 const <b>Array</b> &amp; <b>operator*=</b> (const <b>Array</b> &amp;) 
 
 const <b>Array</b> &amp; <b>operator*=</b> (Real) 
 
 const <b>Array</b> &amp; <b>operator/=</b> (const <b>Array</b> &amp;) 
 
 const <b>Array</b> &amp; <b>operator/=</b> (Real) 
 

 <b>Element access</b> 
 

 
 Real <b>operator[]</b> (Size) const 
 <i>read-only </i> 
 Real <b>at</b> (Size) const 
 
 Real <b>front</b> () const 
 
 Real <b>back</b> () const 
 
 Real &amp; <b>operator[]</b> (Size) 
 <i>read-write </i> 
 Real &amp; <b>at</b> (Size) 
 
 Real &amp; <b>front</b> () 
 
 Real &amp; <b>back</b> () 
 

 <b>Inspectors</b> 
 

 
 Size <b>size</b> () const 
 <i>dimension of the array </i> 
 bool <b>empty</b> () const 
 <i>whether the array is empty </i> 

 <b>Iterator access</b> 
 

 
 const_iterator <b>begin</b> () const 
 
 iterator <b>begin</b> () 
 
 const_iterator <b>end</b> () const 
 
 iterator <b>end</b> () 
 
 const_reverse_iterator <b>rbegin</b> () const 
 
 reverse_iterator <b>rbegin</b> () 
 
 const_reverse_iterator <b>rend</b> () const 
 
 reverse_iterator <b>rend</b> () 
 

 <b>Utilities</b> 
 

 
 void <b>swap</b> (<b>Array</b> &amp;) 

<h3>Related Functions</h3>

 (Note that these are not member functions.) 
 Real <b>DotProduct</b> (const <b>Array</b> &amp;, const <b>Array</b> &amp;) 
 
 const <b>Disposable</b>&lt; <b>Array</b> &gt; <b>operator+</b> (const <b>Array</b> &amp;v) 
 
 const <b>Disposable</b>&lt; <b>Array</b> &gt; <b>operator-</b> (const <b>Array</b> &amp;v) 
 
 const <b>Disposable</b>&lt; <b>Array</b> &gt; <b>operator+</b> (const <b>Array</b> &amp;, const <b>Array</b> &amp;) 
 
 const <b>Disposable</b>&lt; <b>Array</b> &gt; <b>operator+</b> (const <b>Array</b> &amp;, Real) 
 
 const <b>Disposable</b>&lt; <b>Array</b> &gt; <b>operator+</b> (Real, const <b>Array</b> &amp;) 
 
 const <b>Disposable</b>&lt; <b>Array</b> &gt; <b>operator-</b> (const <b>Array</b> &amp;, const <b>Array</b> &amp;) 
 
 const <b>Disposable</b>&lt; <b>Array</b> &gt; <b>operator-</b> (const <b>Array</b> &amp;, Real) 
 
 const <b>Disposable</b>&lt; <b>Array</b> &gt; <b>operator-</b> (Real, const <b>Array</b> &amp;) 
 
 const <b>Disposable</b>&lt; <b>Array</b> &gt; <b>operator*</b> (const <b>Array</b> &amp;, const <b>Array</b> &amp;) 
 
 const <b>Disposable</b>&lt; <b>Array</b> &gt; <b>operator*</b> (const <b>Array</b> &amp;, Real) 
 
 const <b>Disposable</b>&lt; <b>Array</b> &gt; <b>operator*</b> (Real, const <b>Array</b> &amp;) 
 
 const <b>Disposable</b>&lt; <b>Array</b> &gt; <b>operator/</b> (const <b>Array</b> &amp;, const <b>Array</b> &amp;) 
 
 const <b>Disposable</b>&lt; <b>Array</b> &gt; <b>operator/</b> (const <b>Array</b> &amp;, Real) 
 
 const <b>Disposable</b>&lt; <b>Array</b> &gt; <b>operator/</b> (Real, const <b>Array</b> &amp;) 
 
 const <b>Disposable</b>&lt; <b>Array</b> &gt; <b>Abs</b> (const <b>Array</b> &amp;) 
 
 const <b>Disposable</b>&lt; <b>Array</b> &gt; <b>Sqrt</b> (const <b>Array</b> &amp;) 
 
 const <b>Disposable</b>&lt; <b>Array</b> &gt; <b>Log</b> (const <b>Array</b> &amp;) 
 
 const <b>Disposable</b>&lt; <b>Array</b> &gt; <b>Exp</b> (const <b>Array</b> &amp;) 
 
 void <b>swap</b> (<b>Array</b> &amp;, <b>Array</b> &amp;) 
 
 std::ostream &amp; <b>operator&lt;&lt;</b> (std::ostream &amp;, const <b>Array</b> &amp;) 

<h2>Detailed Description</h2>

 

 1-D array used in linear algebra. 

 This class implements the concept of vector as used in linear algebra. As such, it is <b>not</b> meant to be used as a container - std::vector should be used instead. 

 <b>Tests</b>
<dl>
<dt>
<dd> construction of arrays is checked in a number of cases</dl>
 

 

<h2>Friends And Related Function Documentation</h2>

 

<h3>Real DotProduct (const <b>Array</b> &amp;, const <b>Array</b> &amp;) [related]</h3>

 

 

<h3>const <b>Disposable</b>&lt; <b>Array</b> &gt; operator+ (const <b>Array</b> &amp; v) [related]</h3>

 

 

<h3>const <b>Disposable</b>&lt; <b>Array</b> &gt; operator- (const <b>Array</b> &amp; v) [related]</h3>

 

 

<h3>const <b>Disposable</b>&lt; <b>Array</b> &gt; operator+ (const <b>Array</b> &amp;, const <b>Array</b> &amp;) [related]</h3>

 

 

<h3>const <b>Disposable</b>&lt; <b>Array</b> &gt; operator+ (const <b>Array</b> &amp;, Real) [related]</h3>

 

 

<h3>const <b>Disposable</b>&lt; <b>Array</b> &gt; operator+ (Real, const <b>Array</b> &amp;) [related]</h3>

 

 

<h3>const <b>Disposable</b>&lt; <b>Array</b> &gt; operator- (const <b>Array</b> &amp;, const <b>Array</b> &amp;) [related]</h3>

 

 

<h3>const <b>Disposable</b>&lt; <b>Array</b> &gt; operator- (const <b>Array</b> &amp;, Real) [related]</h3>

 

 

<h3>const <b>Disposable</b>&lt; <b>Array</b> &gt; operator- (Real, const <b>Array</b> &amp;) [related]</h3>

 

 

<h3>const <b>Disposable</b>&lt; <b>Array</b> &gt; operator* (const <b>Array</b> &amp;, const <b>Array</b> &amp;) [related]</h3>

 

 

<h3>const <b>Disposable</b>&lt; <b>Array</b> &gt; operator* (const <b>Array</b> &amp;, Real) [related]</h3>

 

 

<h3>const <b>Disposable</b>&lt; <b>Array</b> &gt; operator* (Real, const <b>Array</b> &amp;) [related]</h3>

 

 

<h3>const <b>Disposable</b>&lt; <b>Array</b> &gt; operator/ (const <b>Array</b> &amp;, const <b>Array</b> &amp;) [related]</h3>

 

 

<h3>const <b>Disposable</b>&lt; <b>Array</b> &gt; operator/ (const <b>Array</b> &amp;, Real) [related]</h3>

 

 

<h3>const <b>Disposable</b>&lt; <b>Array</b> &gt; operator/ (Real, const <b>Array</b> &amp;) [related]</h3>

 

 

<h3>const <b>Disposable</b>&lt; <b>Array</b> &gt; Abs (const <b>Array</b> &amp;) [related]</h3>

 

 

<h3>const <b>Disposable</b>&lt; <b>Array</b> &gt; Sqrt (const <b>Array</b> &amp;) [related]</h3>

 

 

<h3>const <b>Disposable</b>&lt; <b>Array</b> &gt; Log (const <b>Array</b> &amp;) [related]</h3>

 

 

<h3>const <b>Disposable</b>&lt; <b>Array</b> &gt; Exp (const <b>Array</b> &amp;) [related]</h3>

 

 

<h3>void swap (<b>Array</b> &amp;, <b>Array</b> &amp;) [related]</h3>

 

 

 

 <b>Examples: </b> <b>BermudanSwaption.cpp</b>.

<h3>std::ostream &amp; operator&lt;&lt; (std::ostream &amp;, const <b>Array</b> &amp;) [related]</h3>

 

 

 

<h2>Author</h2>

 

 Generated automatically by Doxygen for QuantLib from the source code. 

<h2>Index</h2>



<dt><a HREF="#lbBD">Author</a>
<dd></dl>
