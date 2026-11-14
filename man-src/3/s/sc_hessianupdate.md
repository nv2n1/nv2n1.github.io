---
title: "sc_hessianupdate(3)"
name: "sc_hessianupdate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_hessianupdate/"
description: "sc::HessianUpdate –"
---

<p>sc::HessianUpdate &#8211; </p>
<p> The <code>HessianUpdate</code> abstract class is used to specify a hessian update scheme.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;update.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>. Inherited by <code>sc::DFPUpdate</code>, and <code>sc::PowellUpdate</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>HessianUpdate (StateIn &amp;)



HessianUpdate (const Ref&lt; KeyVal &gt; &amp;)



void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


virtual void update (const RefSymmSCMatrix &amp;hessian, const Ref&lt; Function &gt; &amp;, const RefSCVector &amp;xnew, const RefSCVector &amp;gnew)=0



virtual void set_inverse ()



virtual void apply_transform (const Ref&lt; NonlinearTransform &gt; &amp;)



Protected Attributes
int inverse_hessian_</code></pre>
<h2>Detailed Description</h2>
<p>The <code>HessianUpdate</code> abstract class is used to specify a hessian update scheme. </p>
<p> It is used, for example, by <code>QNewtonOpt</code> objects. Based on the value of inverse_hessian_ x and g may be reversed (see Schlegel, Ab initio Methods in Quantum Chemistry I, 1987, p 10).</p>
<h2>Member Function Documentation</h2>
<h3>void sc::HessianUpdate::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>. </p>
<p> Reimplemented in <code>sc::DFPUpdate</code>, <code>sc::BFGSUpdate</code>, and <code>sc::PowellUpdate</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
