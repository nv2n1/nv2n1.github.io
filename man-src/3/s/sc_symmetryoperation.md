---
title: "sc_symmetryoperation(3)"
name: "sc_symmetryoperation"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_symmetryoperation/"
description: "sc::SymmetryOperation –"
---

<p>sc::SymmetryOperation &#8211; </p>
<p> The <code>SymmetryOperation</code> class provides a 3 by 3 matrix representation of a symmetry operation, such as a rotation or reflection.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;pointgrp.h&gt;

Public Member Functions
SymmetryOperation (const SymmetryOperation &amp;)



double trace () const


returns the trace of the transformation matrix


double * operator[] (int i)


returns the i'th row of the transformation matrix


const double * operator[] (int i) const


const version of the above


double &amp; operator() (int i, int j)


returns a reference to the (i,j)th element of the transformation matrix


double operator() (int i, int j) const


const version of the above


void zero ()


zero out the symop


SymmetryOperation operate (const SymmetryOperation &amp;r) const


This operates on this with r (i.e. return r * this).


SymmetryOperation transform (const SymmetryOperation &amp;r) const


This performs the transform r * this * r~.


void unit ()


Set equal to a unit matrix.


void E ()


Set equal to E.


void i ()


Set equal to an inversion.


void sigma_h ()


Set equal to reflection in xy plane.


void sigma_xz ()


Set equal to reflection in xz plane.


void sigma_yz ()


Set equal to reflection in yz plane.


void rotation (int n)


Set equal to a clockwise rotation by 2pi/n.


void rotation (double theta)



void c2_x ()


Set equal to C2 about the x axis.


void c2_y ()


Set equal to C2 about the x axis.


void transpose ()



void print (std::ostream &amp;=ExEnv::out0()) const


print the matrix</code></pre>
<h2>Detailed Description</h2>
<p>The <code>SymmetryOperation</code> class provides a 3 by 3 matrix representation of a symmetry operation, such as a rotation or reflection.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
