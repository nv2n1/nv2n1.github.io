---
title: "sc_lebedevlaikovintegrator(3)"
name: "sc_lebedevlaikovintegrator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_lebedevlaikovintegrator/"
description: "sc::LebedevLaikovIntegrator –"
---

<p>sc::LebedevLaikovIntegrator &#8211; </p>
<p> An implementation of a Lebedev angular integrator.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;integrator.h&gt;</code></pre>
<p> Inherits <code>sc::AngularIntegrator</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>LebedevLaikovIntegrator (const Ref&lt; KeyVal &gt; &amp;)


Construct a LebedevLaikovIntegrator using the given KeyVal input.


LebedevLaikovIntegrator (StateIn &amp;)



LebedevLaikovIntegrator (int)



void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


int nw (void) const



int num_angular_points (double r_value, int ir)



double angular_point_cartesian (int iangular, double r, SCVector3 &amp;integration_point) const



void print (std::ostream &amp;=ExEnv::out0()) const


Print the object.



Protected Member Functions
void init (int n)



Protected Attributes
int npoint_



double * x_



double * y_



double * z_



double * w_</code></pre>
<h2>Detailed Description</h2>
<p>An implementation of a Lebedev angular integrator. </p>
<p> It uses code written by Dr. Dmitri N. Laikov. </p>
<p> This can generate grids with the following numbers of points: 6, 14, 26, 38, 50, 74, 86, 110, 146, 170, 194, 230, 266, 302, 350, 386, 434, 482, 530, 590, 650, 698, 770, 830, 890, 974, 1046, 1118, 1202, 1274, 1358, 1454, 1538, 1622, 1730, 1814, 1910, 2030, 2126, 2222, 2354, 2450, 2558, 2702, 2810, 2930, 3074, 3182, 3314, 3470, 3590, 3722, 3890, 4010, 4154, 4334, 4466, 4610, 4802, 4934, 5090, 5294, 5438, 5606, and 5810. </p>
<p> V.I. Lebedev, and D.N. Laikov &#8216;A quadrature formula for the sphere of the 131st<br />
&nbsp;<wbr>&nbsp;<wbr>algebraic order of accuracy&#8217;&nbsp;<wbr>Doklady Mathematics, Vol. 59, No. 3, 1999, pp. 477-481. </p>
<p> V.I. Lebedev &#8216;A quadrature formula for the sphere of 59th algebraic<br />
&nbsp;<wbr>&nbsp;<wbr>order of accuracy&#8217;&nbsp;<wbr>Russian Acad. Sci. Dokl. Math., Vol. 50, 1995, pp. 283-286. </p>
<p> V.I. Lebedev, and A.L. Skorokhodov &#8216;Quadrature formulas of orders 41, 47, and 53 for the sphere&#8217; Russian Acad. Sci. Dokl. Math., Vol. 45, 1992, pp. 587-592. </p>
<p> V.I. Lebedev &#8216;Spherical quadrature formulas exact to orders 25-29&#8217; Siberian Mathematical Journal, Vol. 18, 1977, pp. 99-107. </p>
<p> V.I. Lebedev &#8216;Quadratures on a sphere&#8217; Computational Mathematics and Mathematical Physics, Vol. 16, 1976, pp. 10-24. </p>
<p> V.I. Lebedev Values of the nodes and weights of ninth to seventeenth order Gauss-Markov quadrature formulae invariant under the octahedron group with inversion Computational Mathematics and Mathematical Physics, Vol. 15, 1975, pp. 44-51.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::LebedevLaikovIntegrator::LebedevLaikovIntegrator (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>Construct a <code>LebedevLaikovIntegrator</code> using the given <code>KeyVal</code> input. The n keyword gives the number of angular points. The default is 302.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::LebedevLaikovIntegrator::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::AngularIntegrator</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
