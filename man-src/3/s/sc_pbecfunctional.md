---
title: "sc_pbecfunctional(3)"
name: "sc_pbecfunctional"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_pbecfunctional/"
description: "sc::PBECFunctional –"
---

<p>sc::PBECFunctional &#8211; </p>
<p> Implements the Perdew-Burke-Ernzerhof (PBE) correlation functional.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;functional.h&gt;</code></pre>
<p> Inherits <code>sc::DenFunctional</code>.</p>
<h3>Public Member Functions</h3>
<p><code>PBECFunctional</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>PBECFunctional</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 int <code>need_density_gradient</code> () </p>
<p> void <code>point</code> (const <code>PointInputData</code> &amp;, <code>PointOutputData</code> &amp;) </p>
<p> void <code>set_spin_polarized</code> (int)</p>
<h3>Protected Member Functions</h3>
<pre><code>void init_constants ()



double rho_deriv (double rho_a, double rho_b, double mdr, double ec_local, double ec_local_dra)



double gab_deriv (double rho, double phi, double mdr, double ec_local)



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>LSDACFunctional</code> &gt; <code>local_</code> </p>
<p> double <code>gamma</code> </p>
<p> double <code>beta</code></p>
<h2>Detailed Description</h2>
<p>Implements the Perdew-Burke-Ernzerhof (PBE) correlation functional. </p>
<p> John P. Perdew, Kieron Burke, and Yue Wang, Phys. Rev. B, 54(23), pp. 16533-16539, 1996. </p>
<p> John P. Perdew, Kieron Burke, and Matthias Ernzerhof, Phys. Rev. Lett., 77(18), pp. 3865-3868, 1996.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::PBECFunctional::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::DenFunctional</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
