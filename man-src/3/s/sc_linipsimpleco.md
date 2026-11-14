---
title: "sc_linipsimpleco(3)"
name: "sc_linipsimpleco"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_linipsimpleco/"
description: "sc::LinIPSimpleCo –"
---

<p>sc::LinIPSimpleCo &#8211; </p>
<p> The <code>LinIPSimpleCo</code> class describes an in-plane component of a linear bend internal coordinate of a molecule.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;simple.h&gt;</code></pre>
<p> Inherits <code>sc::SimpleCo</code>.</p>
<h3>Public Member Functions</h3>
<p><code>LinIPSimpleCo</code> (const <code>LinIPSimpleCo</code> &amp;) </p>
<p> <code>LinIPSimpleCo</code> (const char *refr, int, int, int, const <code>SCVector3</code> &amp;u)<br />
 <i>This constructor takes a string containing a label, and three integers a, b, and d which give the indices of the atoms involved in the linear angle abc. </i><br />
 <code>LinIPSimpleCo</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>The </i><code>KeyVal</code> constructor.<br />
 const char * <code>ctype</code> () const<br />
 <i>Always returns the string &#8216;LINIP&#8217;. </i><br />
 double <code>radians</code> () const<br />
 <i>Returns the value of the angle abc in radians. </i><br />
 double <code>degrees</code> () const<br />
 <i>Returns the value of the angle abc in degrees. </i><br />
 double <code>preferred_value</code> () const<br />
 <i>Returns the value of the angle abc in degrees. </i></p>
<h2>Detailed Description</h2>
<p>The <code>LinIPSimpleCo</code> class describes an in-plane component of a linear bend internal coordinate of a molecule. </p>
<p> The input is described in the documentation of its parent class <code>SimpleCo</code>. A vector, $s the keyword u, that is not colinear with either $ &#8211; lly, <code>LinIPSimpleCo</code> is used with a corresponding <code>LinOPSimpleCo</code>, which is given exactly the same u. </p>
<p> Designating the three atoms as $a$, $b$, and $c$ and their cartesian positions as $$, $nd $lue of the coordinate, $ heta_i$, is given by </p>
<p> [ b} = ac{ &#8211; nd three integers a, b, and d which give the indices of the atoms involved in the linear angle abc. The last argument, u, is a unit vector used to defined the direction in which distortion is measured. Atom numbering begins at atom 1, not atom 0.</p>
<h3>sc::LinIPSimpleCo::LinIPSimpleCo (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>KeyVal</code> constructor. This calls the <code>SimpleCo</code> keyval constructor with an integer argument of 3.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
