---
title: "sc_shellrotation(3)"
name: "sc_shellrotation"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_shellrotation/"
description: "sc::ShellRotation –"
---

<p>sc::ShellRotation &#8211; </p>
<p> <code>Compute</code> the transformation matrices that maps a set of Cartesian functions to another set of Cartesian functions in a rotated coordinate system.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;shellrot.h&gt;

Public Member Functions
void init (int a, SymmetryOperation &amp;, const Ref&lt; Integral &gt; &amp;)


Initialize the ShellRotation for Cartesian functions, given the angular momentum, a symmetry operation, and an Integral object.


void init_pure (int a, SymmetryOperation &amp;, const Ref&lt; Integral &gt; &amp;)


Initialize the ShellRotation for solid harmonic functions, given the angular momentum, a symmetry operation, and an Integral object.


ShellRotation (int n)


Initialize this ShellRotation to hold a n by n transformation.


ShellRotation (const ShellRotation &amp;)


Initialize this from another ShellRotation.


ShellRotation (int a, SymmetryOperation &amp;, const Ref&lt; Integral &gt; &amp;, int pure=0)


Initialize using init(...) or, if pure is nonzero, init_pure(...).


ShellRotation &amp; operator= (const ShellRotation &amp;)


Assign this to another shell rotation.


int am () const


Return the angular momentum.


int dim () const


Return the number of functions in a shell.


double &amp; operator() (int i, int j)


Return an element of the transform matrix.


double * operator[] (int i)


Return a row of the transform matrix.


ShellRotation operate (const ShellRotation &amp;rot) const


Returns the result of rot*this.


ShellRotation transform (const ShellRotation &amp;rot) const


Returns the result of rot*this*transpose(rot).


double trace () const


Return the trace of the transformation.


void print () const


Print the object to ExEnv::out0().</code></pre>
<h2>Detailed Description</h2>
<p><code>Compute</code> the transformation matrices that maps a set of Cartesian functions to another set of Cartesian functions in a rotated coordinate system.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::ShellRotation::init (int a, <code>SymmetryOperation</code> &amp;, const <code>Ref</code>&lt; <code>Integral</code> &gt; &amp;)</h3>
<p>Initialize the <code>ShellRotation</code> for Cartesian functions, given the angular momentum, a symmetry operation, and an <code>Integral</code> object.</p>
<h3>void sc::ShellRotation::init_pure (int a, <code>SymmetryOperation</code> &amp;, const <code>Ref</code>&lt; <code>Integral</code> &gt; &amp;)</h3>
<p>Initialize the <code>ShellRotation</code> for solid harmonic functions, given the angular momentum, a symmetry operation, and an <code>Integral</code> object.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
