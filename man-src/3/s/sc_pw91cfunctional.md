---
title: "sc_pw91cfunctional(3)"
name: "sc_pw91cfunctional"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_pw91cfunctional/"
description: "sc::PW91CFunctional –"
---

<p>sc::PW91CFunctional &#8211; </p>
<p> The Perdew-Wang 1991 correlation functional computes energies and densities using the designated local correlation functional.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;functional.h&gt;</code></pre>
<p> Inherits <code>sc::DenFunctional</code>.</p>
<h3>Public Member Functions</h3>
<p><code>PW91CFunctional</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>PW91CFunctional</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 int <code>need_density_gradient</code> () </p>
<p> void <code>point</code> (const <code>PointInputData</code> &amp;, <code>PointOutputData</code> &amp;) </p>
<p> void <code>set_spin_polarized</code> (int)</p>
<h3>Protected Member Functions</h3>
<pre><code>void init_constants ()



double limit_df_drhoa (double rhoa, double gamma, double ec, double decdrhoa)



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>LSDACFunctional</code> &gt; <code>local_</code> </p>
<p> double <code>a</code> </p>
<p> double <code>b</code> </p>
<p> double <code>c</code> </p>
<p> double <code>d</code> </p>
<p> double <code>alpha</code> </p>
<p> double <code>c_c0</code> </p>
<p> double <code>c_x</code> </p>
<p> double <code>nu</code></p>
<h2>Detailed Description</h2>
<p>The Perdew-Wang 1991 correlation functional computes energies and densities using the designated local correlation functional. </p>
<p> J. P. Perdew, Proceedings of the 75. WE-Heraeus-Seminar and 21st Annual International Symposium on Electronic Structure of Solids held in Gaussig (Germany), March 11-15, 1991, P. Ziesche and H. Eschrig, eds., pp. 11-20. </p>
<p> J. P. Perdew, J. A. Chevary, S. H. Vosko, K. A. Jackson, M. R. Pederson, and D. J. Singh, Phys. Rev. B, 46, 6671, 1992.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::PW91CFunctional::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::DenFunctional</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
