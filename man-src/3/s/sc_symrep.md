---
title: "sc_symrep(3)"
name: "sc_symrep"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_symrep/"
description: "sc::SymRep –"
---

<p>sc::SymRep &#8211; </p>
<p> The <code>SymRep</code> class provides an n dimensional matrix representation of a symmetry operation, such as a rotation or reflection.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;pointgrp.h&gt;

Public Member Functions
SymRep (int=0)



SymRep (const SymmetryOperation &amp;)



operator SymmetryOperation () const


Cast to a SymmetryOperation.


double trace () const


returns the trace of the transformation matrix


void set_dim (int i)


set the dimension of d


double * operator[] (int i)


returns the i'th row of the transformation matrix


const double * operator[] (int i) const


const version of the above


double &amp; operator() (int i, int j)


returns a reference to the (i,j)th element of the transformation matrix


double operator() (int i, int j) const


const version of double&amp; operator()(int i, int j)


void zero ()


zero out the symop


SymRep operate (const SymRep &amp;r) const


This operates on this with r (i.e. return r * this).


SymRep transform (const SymRep &amp;r) const


This performs the transform r * this * r~.


void unit ()


Set equal to a unit matrix.


void E ()


Set equal to the identity.


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


void print (std::ostream &amp;=ExEnv::out0()) const


print the matrix</code></pre>
<h2>Detailed Description</h2>
<p>The <code>SymRep</code> class provides an n dimensional matrix representation of a symmetry operation, such as a rotation or reflection. </p>
<p> The trace of a <code>SymRep</code> can be used as the character for that symmetry operation. d is hardwired to 5&#215;5 since the H irrep in Ih is 5 dimensional.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
