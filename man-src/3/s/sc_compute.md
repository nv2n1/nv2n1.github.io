---
title: "sc_compute(3)"
name: "sc_compute"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_compute/"
description: "sc::Compute –"
---

<p>sc::Compute &#8211; </p>
<p> The <code>Compute</code> class provides a means of keeping results up to date.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;compute.h&gt;</code></pre>
<p> Inherited by <code>sc::Function</code>.</p>
<h3>Public Member Functions</h3>
<p>virtual void <code>obsolete</code> ()<br />
 <i>Marks all results as being out of date. </i></p>
<h3>Protected Member Functions</h3>
<pre><code>virtual void compute ()=0


Recompute at least the results that have compute true and are not already computed.



Friends</code></pre>
<p> class <code>ResultInfo</code> </p>
<p> class <code>AccResultInfo</code></p>
<h2>Detailed Description</h2>
<p>The <code>Compute</code> class provides a means of keeping results up to date. </p>
<p> Derived classes can have member data which is registered with the compute class. When this member data is accessed and it is not available, the compute member function is called. The compute member must be implemented in derived classes and is responsible for computed the requested result.</p>
<h2>Member Function Documentation</h2>
<h3>virtual void sc::Compute::compute () [protected, pure virtual]</h3>
<p>Recompute at least the results that have compute true and are not already computed. This should only be called by Result&#8217;s members. </p>
<p> Implemented in <code>sc::SumMolecularEnergy</code>, <code>sc::TaylorMolecularEnergy</code>, <code>sc::MBPT2</code>, <code>sc::MP2BasisExtrap</code>, <code>sc::MBPT2_R12</code>, <code>sc::PsiWavefunction</code>, <code>sc::SCF</code>, <code>sc::ElectronDensity</code>, <code>sc::BatchElectronDensity</code>, <code>sc::Orbital</code>, <code>sc::Shape</code>, and <code>sc::Volume</code>.</p>
<h3>virtual void sc::Compute::obsolete () [virtual]</h3>
<p>Marks all results as being out of date. Any subsequent access to results will cause <code>Compute::compute()</code> to be called. </p>
<p> Reimplemented in <code>sc::MBPT2</code>, <code>sc::MBPT2_R12</code>, <code>sc::SCF</code>, and <code>sc::Wavefunction</code>. </p>
<p> Referenced by sc::Function::get_x_reference().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
