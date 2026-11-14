---
title: "sc_convergence(3)"
name: "sc_convergence"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_convergence/"
description: "sc::Convergence –"
---

<p>sc::Convergence &#8211; </p>
<p> The <code>Convergence</code> class is used by the optimizer to determine when an optimization is converged.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;conv.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>. Inherited by <code>sc::MolEnergyConvergence</code>.</p>
<h3>Public Member Functions</h3>
<p><code>Convergence</code> (double tolerance) </p>
<p> <code>Convergence</code> (<code>StateIn</code> &amp;) </p>
<p> <code>Convergence</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>The </i><code>KeyVal</code> constructor reads the following keywords:.<br />
 void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 virtual void <code>get_grad</code> (const <code>Ref</code>&lt; <code>Function</code> &gt; &amp;)<br />
 <i>Set the current gradient and displacement. </i><br />
 virtual void <code>get_x</code> (const <code>Ref</code>&lt; <code>Function</code> &gt; &amp;) </p>
<p> virtual void <code>set_nextx</code> (const <code>RefSCVector</code> &amp;) </p>
<p> virtual void <code>reset</code> ()<br />
 <i>Set the current gradient and displacement to null. </i><br />
 virtual int <code>converged</code> ()<br />
 <i>Return nonzero if the optimization has converged. </i></p>
<h3>Protected Member Functions</h3>
<pre><code>void check_conv (const char *heading, double val, double bound, int &amp;pass, int &amp;fail)



void set_defaults ()



Protected Attributes</code></pre>
<p> <code>RefSCVector</code> <code>grad_</code> </p>
<p> <code>RefSCVector</code> <code>x_</code> </p>
<p> <code>RefSCVector</code> <code>nextx_</code> </p>
<p> int <code>use_max_disp_</code> </p>
<p> double <code>max_disp_</code> </p>
<p> int <code>use_max_grad_</code> </p>
<p> double <code>max_grad_</code> </p>
<p> int <code>use_rms_disp_</code> </p>
<p> double <code>rms_disp_</code> </p>
<p> int <code>use_rms_grad_</code> </p>
<p> double <code>rms_grad_</code> </p>
<p> int <code>use_graddisp_</code> </p>
<p> double <code>graddisp_</code></p>
<h2>Detailed Description</h2>
<p>The <code>Convergence</code> class is used by the optimizer to determine when an optimization is converged. </p>
<p> The <code>KeyVal</code> input for <code>Convergence</code> is given below. Giving none of these keywords is the same as giving the following input: </p>
<pre> conv&lt;Convergence&gt;: (
 max_disp = 1.0e-6
 max_grad = 1.0e-6
 graddisp = 1.0e-6
 )</pre>
<p>&nbsp;<wbr></p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::Convergence::Convergence (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>KeyVal</code> constructor reads the following keywords:. .IP &quot;max_disp&quot; 1c The value of the maximum displacement must be less then the value of this keyword for the calculation to be converged. The default is to not check this parameter. However, if no other keyword are given, default convergence parameters are chosen as described above. </p>
<dl>
<dt>max_grad</p>
<dd>The value of the maximum gradient must be less then the value of this keyword for the calculation to be converged. The default is to not check this parameter. However, if no other keyword are given, default convergence parameters are chosen as described above.</dl>
<dl>
<dt>rms_disp</p>
<dd>The value of the RMS of the displacements must be less then the value of this keyword for the calculation to be converged. The default is to not check this parameter. However, if no other keyword are given, default convergence parameters are chosen as described above.</dl>
<dl>
<dt>rms_grad</p>
<dd>The value of the RMS of the gradients must be less then the value of this keyword for the calculation to be converged. The default is to not check this parameter. However, if no other keyword are given, default convergence parameters are chosen as described above.</dl>
<dl>
<dt>graddisp</p>
<dd>The value of the scalar product of the gradient vector with the displacement vector must be less then the value of this keyword for the calculation to be converged. The default is to not check this parameter. However, if no other keyword are given, default convergence parameters are chosen as described above.</dl>
<h2>Member Function Documentation</h2>
<h3>void sc::Convergence::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>. </p>
<p> Reimplemented in <code>sc::MolEnergyConvergence</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
