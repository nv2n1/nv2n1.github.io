---
title: "sc_pw91xfunctional(3)"
name: "sc_pw91xfunctional"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_pw91xfunctional/"
description: "sc::PW91XFunctional –"
---

<p>sc::PW91XFunctional &#8211; </p>
<p> The Perdew-Wang 1991 exchange functional computes energies and densities using the designated local correlation functional.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;functional.h&gt;</code></pre>
<p> Inherits <code>sc::DenFunctional</code>.</p>
<h3>Public Member Functions</h3>
<p><code>PW91XFunctional</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>PW91XFunctional</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 int <code>need_density_gradient</code> () </p>
<p> void <code>point</code> (const <code>PointInputData</code> &amp;, <code>PointOutputData</code> &amp;)</p>
<h3>Protected Member Functions</h3>
<pre><code>void spin_contrib (const PointInputData::SpinData &amp;, double &amp;mpw, double &amp;dmpw_dr, double &amp;dmpw_dg)



void init_constants ()



Protected Attributes
double a



double b



double c



double d



double a_x</code></pre>
<h2>Detailed Description</h2>
<p>The Perdew-Wang 1991 exchange functional computes energies and densities using the designated local correlation functional. </p>
<p> J. P. Perdew, Proceedings of the 75. WE-Heraeus-Seminar and 21st Annual International Symposium on Electronic Structure of Solids held in Gaussig (Germany), March 11-15, 1991, P. Ziesche and H. Eschrig, eds., pp. 11-20. </p>
<p> J. P. Perdew, J. A. Chevary, S. H. Vosko, K. A. Jackson, M. R. Pederson, and D. J. Singh, Phys. Rev. B, 46, 6671, 1992.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::PW91XFunctional::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::DenFunctional</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
