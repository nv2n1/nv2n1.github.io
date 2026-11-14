---
title: "sc_redundantcartesiansubiter(3)"
name: "sc_redundantcartesiansubiter"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_redundantcartesiansubiter/"
description: "sc::RedundantCartesianSubIter –"
---

<p>sc::RedundantCartesianSubIter &#8211; </p>
<p> Like <code>RedundantCartesianIter</code>, except a, b, and c are fixed to a given value.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;cartiter.h&gt;</code></pre>
<p> Inherited by <code>sc::RedundantCartesianSubIterCCA</code>, <code>sc::RedundantCartesianSubIterCints</code>, and <code>sc::RedundantCartesianSubIterV3</code>.</p>
<h3>Public Member Functions</h3>
<p><code>RedundantCartesianSubIter</code> (int l)<br />
 <i>Create a object for the given angular momentum. </i><br />
 virtual int <code>bfn</code> ()=0<br />
 <i>Return the current Cartesian basis function number. </i><br />
 void <code>start</code> (int a, int b, int c)<br />
 <i>Initialize the iterator. </i><br />
 void <code>next</code> ()<br />
 <i>Move to the next combination of axes. </i><br />
 <code>operator int</code> () const<br />
 <i>Returns nonzero if the iterator currently hold valid data. </i><br />
 int <code>a</code> () const<br />
 <i>The current exponent of x. </i><br />
 int <code>b</code> () const<br />
 <i>The current exponent of y. </i><br />
 int <code>c</code> () const<br />
 <i>The current exponent of z. </i><br />
 int <code>l</code> () const<br />
 <i>The angular momentum. </i><br />
 int <code>l</code> (int i)<br />
 <i>Returns </i><code>a()</code> if i==0, <code>b()</code> if i==1, and <code>c()</code> if i==2.<br />
 int <code>axis</code> (int i)<br />
 <i>Return the i&#8217;th axis. </i></p>
<h2>Detailed Description</h2>
<p>Like <code>RedundantCartesianIter</code>, except a, b, and c are fixed to a given value.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::RedundantCartesianSubIter::start (int a, int b, int c)</h3>
<p>Initialize the iterator. The constraints on a, b, and c are given as arguments.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
