---
title: "sc_p86cfunctional(3)"
name: "sc_p86cfunctional"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_p86cfunctional/"
description: "sc::P86CFunctional –"
---

<p>sc::P86CFunctional &#8211; </p>
<p> Implements the Perdew 1986 (P86) correlation functional.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;functional.h&gt;</code></pre>
<p> Inherits <code>sc::DenFunctional</code>.</p>
<h3>Public Member Functions</h3>
<p><code>P86CFunctional</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>P86CFunctional</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 int <code>need_density_gradient</code> () </p>
<p> void <code>point</code> (const <code>PointInputData</code> &amp;, <code>PointOutputData</code> &amp;)</p>
<h3>Protected Member Functions</h3>
<pre><code>void init_constants ()



Protected Attributes
double a_



double C1_



double C2_



double C3_



double C4_



double C5_



double C6_



double C7_</code></pre>
<h2>Detailed Description</h2>
<p>Implements the Perdew 1986 (P86) correlation functional. </p>
<p> J. P. Perdew, Phys. Rev. B, 33(12), pp. 8822-8824. </p>
<p> J. P. Perdew, Phys. Rev. B. 34(10), pp. 7406.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::P86CFunctional::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::DenFunctional</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
