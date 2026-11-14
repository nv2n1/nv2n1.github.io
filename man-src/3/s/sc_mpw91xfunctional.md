---
title: "sc_mpw91xfunctional(3)"
name: "sc_mpw91xfunctional"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_mpw91xfunctional/"
description: "sc::mPW91XFunctional –"
---

<p>sc::mPW91XFunctional &#8211; </p>
<p> Implements a modified 1991 Perdew-Wang exchange functional.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;functional.h&gt;</code></pre>
<p> Inherits <code>sc::DenFunctional</code>.</p>
<h3>Public Types</h3>
<p>enum <code>Func</code> { <code>B88</code>, <code>PW91</code>, <code>mPW91</code> }</p>
<h3>Public Member Functions</h3>
<p><code>mPW91XFunctional</code> ()<br />
 <i>Construct an mPW exchange functional. </i><br />
 <code>mPW91XFunctional</code> (Func variant)<br />
 <i>Construct an mPW form exchange functional using the given functional variant. </i><br />
 <code>mPW91XFunctional</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>Construct an mPW form exchange functional. </i><br />
 <code>mPW91XFunctional</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 int <code>need_density_gradient</code> () </p>
<p> void <code>point</code> (const <code>PointInputData</code> &amp;, <code>PointOutputData</code> &amp;) </p>
<p> void <code>init_constants</code> (Func)</p>
<h3>Protected Member Functions</h3>
<pre><code>void spin_contrib (const PointInputData::SpinData &amp;, double &amp;mpw, double &amp;dmpw_dr, double &amp;dmpw_dg)



Protected Attributes
double b



double beta



double c



double d



double a_x



double x_d_coef</code></pre>
<h2>Detailed Description</h2>
<p>Implements a modified 1991 Perdew-Wang exchange functional. </p>
<p> C. Adamo and V. Barone, J. Chem. Phys., <a href="/docs/linux/man/2-108/">108</a>(2), pp. 664-674, 1998.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::mPW91XFunctional::mPW91XFunctional (Func variant)</h3>
<p>Construct an mPW form exchange functional using the given functional variant. The variant can be B88, PW91, or mPW91.</p>
<h3>sc::mPW91XFunctional::mPW91XFunctional (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>Construct an mPW form exchange functional. The following keywords are recognized:</p>
<dl>
<dt>constants</p>
<dd>This can be B88 to give the Becke88 exchange functional; PW91, to give results similar to the PW91 exchange functional; or mPW91, to give the new functional developed by Adamo and Barone.</dl>
<dl>
<dt>b</p>
<dd>
<dt>beta</p>
<dd>
<dt>c</p>
<dd>
<dt>d</p>
<dd>
<dt>x_d_coef</p>
<dd>The coefficient of $x^d$, where $x$ is the reduced gradient.</dl>
<h2>Member Function Documentation</h2>
<h3>void sc::mPW91XFunctional::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::DenFunctional</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
