---
title: "sc_clks(3)"
name: "sc_clks"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_clks/"
description: "sc::CLKS –"
---

<p>sc::CLKS &#8211; </p>
<p> This provides a Kohn-Sham implementation for closed-shell systems.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;clks.h&gt;</code></pre>
<p> Inherits <code>sc::CLSCF</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>CLKS (StateIn &amp;)



CLKS (const Ref&lt; KeyVal &gt; &amp;)


This KeyVal constructor reads the following keywords:.


void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


void print (std::ostream &amp;o=ExEnv::out0()) const


Print information about the object.


void two_body_energy (double &amp;ec, double &amp;ex)



int value_implemented () const


Information about the availability of values, gradients, and hessians.


int gradient_implemented () const



RefSymmSCMatrix density ()


Returns the SO density.



Protected Member Functions
void ao_fock (double accuracy)



double scf_energy ()



Ref&lt; SCExtrapData &gt; extrap_data ()



RefSymmSCMatrix effective_fock ()


Returns closed-shell Fock matrix in MO basis (including XC contribution for KS DFT).


void init_vector ()



void done_vector ()



void two_body_deriv (double *)



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>DenIntegrator</code> &gt; <code>integrator_</code> </p>
<p> <code>Ref</code>&lt; <code>DenFunctional</code> &gt; <code>functional_</code> </p>
<p> <code>RefSymmSCMatrix</code> <code>vxc_</code> </p>
<p> double <code>exc_</code></p>
<h2>Detailed Description</h2>
<p>This provides a Kohn-Sham implementation for closed-shell systems.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::CLKS::CLKS (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>This <code>KeyVal</code> constructor reads the following keywords:. .IP &quot;integrator&quot; 1c Specifies the <code>DenIntegrator</code> that will be used to integrate the density functional. The default is <code>RadialAngularIntegrator</code>. </p>
<dl>
<dt>functional</p>
<dd>Specifies the <code>DenFunctional</code> that will be used to compute the exchange/correlation <code>contribution</code>. This is no default.</dl>
<h2>Member Function Documentation</h2>
<h3><code>RefSymmSCMatrix</code> sc::CLKS::effective_fock () [protected, virtual]</h3>
<p>Returns closed-shell Fock matrix in MO basis (including XC <code>contribution</code> for KS DFT). </p>
<p> Reimplemented from <code>sc::CLSCF</code>.</p>
<h3>void sc::CLKS::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::CLSCF</code>.</p>
<h3>int sc::CLKS::value_implemented () const [virtual]</h3>
<p>Information about the availability of values, gradients, and hessians. </p>
<p> Reimplemented from <code>sc::Function</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
