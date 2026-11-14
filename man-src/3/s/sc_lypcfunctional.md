---
title: "sc_lypcfunctional(3)"
name: "sc_lypcfunctional"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_lypcfunctional/"
description: "sc::LYPCFunctional –"
---

<p>sc::LYPCFunctional &#8211; </p>
<p> Implements the Lee, Yang, and Parr functional.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;functional.h&gt;</code></pre>
<p> Inherits <code>sc::DenFunctional</code>.</p>
<h3>Public Member Functions</h3>
<p><code>LYPCFunctional</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>LYPCFunctional</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 int <code>need_density_gradient</code> () </p>
<p> void <code>point</code> (const <code>PointInputData</code> &amp;, <code>PointOutputData</code> &amp;)</p>
<h3>Protected Member Functions</h3>
<pre><code>void init_constants ()



Protected Attributes
double a_



double b_



double c_



double d_</code></pre>
<h2>Detailed Description</h2>
<p>Implements the Lee, Yang, and Parr functional. </p>
<p> B. Miehlich, A. Savin, H. Stoll and H. Preuss, Chem. Phys. Lett., <a href="/docs/linux/man/3-157/">157</a>(3), pp. 200-206, 1989. </p>
<p> C. Lee, W. Yang, and R. G. Parr, Phys. Rev. B, <a href="/docs/linux/man/2-37/">37</a>(2), pp 785-789, 1988.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::LYPCFunctional::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::DenFunctional</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
