---
title: "sc_r12inteval(3)"
name: "sc_r12inteval"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_r12inteval/"
description: "sc::R12IntEval –"
---

<p>sc::R12IntEval &#8211; </p>
<p> <code>R12IntEval</code> is the top-level class which computes intermediates occuring in linear R12 theories.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;r12int_eval.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>R12IntEval (StateIn &amp;)



R12IntEval (const Ref&lt; R12IntEvalInfo &gt; &amp;info, bool gbc=true, bool ebc=true, LinearR12::ABSMethod abs_method=LinearR12::ABS_CABSPlus, LinearR12::StandardApproximation stdapprox=LinearR12::StdApprox_Ap, bool follow_ks_ebcfree=false)


Constructs R12IntEval.


void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


virtual void obsolete ()



void include_mp1 (bool include_mp1)



void set_debug (int debug)



void set_dynamic (bool dynamic)



void set_print_percent (double print_percent)



void set_memory (size_t nbytes)



const bool gbc () const



const bool ebc () const



const LinearR12::StandardApproximation stdapprox () const



bool follow_ks_ebcfree () const



Ref&lt; R12IntEvalInfo &gt; r12info () const



RefSCDimension dim_oo_aa () const



RefSCDimension dim_oo_ab () const



RefSCDimension dim_oo_s () const



RefSCDimension dim_oo_t () const



RefSCDimension dim_vv_aa () const



RefSCDimension dim_vv_ab () const



virtual void compute ()


This function causes the intermediate matrices to be computed.


RefSCMatrix V_aa ()


Returns alpha-alpha block of the V intermediate matrix.


RefSCMatrix X_aa ()


Returns alpha-alpha block of the X intermediate matrix.


RefSymmSCMatrix B_aa ()


Returns alpha-alpha block of the B intermediate matrix.


RefSCMatrix A_aa ()


Returns alpha-alpha block of the A intermediate matrix. Returns 0 if EBC is assumed.


RefSCMatrix Ac_aa ()


Returns alpha-alpha block of the A intermediate matrix. Returns 0 if EBC is assumed.


RefSCMatrix T2_aa ()


Returns alpha-alpha block of the MP2 T2 matrix. Returns 0 if EBC is assumed.


RefSCMatrix V_ab ()


Returns alpha-beta block of the V intermediate matrix.


RefSCMatrix X_ab ()


Returns alpha-beta block of the X intermediate matrix.


RefSymmSCMatrix B_ab ()


Returns alpha-beta block of the B intermediate matrix.


RefSCMatrix A_ab ()


Returns alpha-beta block of the A intermediate matrix. Returns 0 if EBC is assumed.


RefSCMatrix Ac_ab ()


Returns alpha-beta block of the A intermediate matrix. Returns 0 if EBC is assumed.


RefSCMatrix T2_ab ()


Returns alpha-beta block of the MP2 T2 matrix. Returns 0 if EBC is assumed.


RefSCVector emp2_aa ()


Returns alpha-alpha MP2 pair energies.


RefSCVector emp2_ab ()


Returns alpha-beta MP2 pair energies.


Ref&lt; R12Amplitudes &gt; amps ()


Returns amplitudes of pair correlation functions.


RefDiagSCMatrix evals () const</code></pre>
<h2>Detailed Description</h2>
<p><code>R12IntEval</code> is the top-level class which computes intermediates occuring in linear R12 theories. </p>
<p> This class is used by all <code>Wavefunction</code> classes that implement linear R12 methods.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::R12IntEval::R12IntEval (const <code>Ref</code>&lt; <code>R12IntEvalInfo</code> &gt; &amp; info, bool gbc = true, bool ebc = true, LinearR12::ABSMethod abs_method = LinearR12::ABS_CABSPlus, LinearR12::StandardApproximation stdapprox = LinearR12::StdApprox_Ap, bool follow_ks_ebcfree = false)</h3>
<p>Constructs <code>R12IntEval</code>. If follow_ks_ebcfree is true then follow formalism of Klopper and Samson to compute EBC-free MP2-R12 energy.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::R12IntEval::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
