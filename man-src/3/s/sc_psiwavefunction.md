---
title: "sc_psiwavefunction(3)"
name: "sc_psiwavefunction"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_psiwavefunction/"
description: "sc::PsiWavefunction –"
---

<p>sc::PsiWavefunction &#8211; </p>
<p> <code>PsiWavefunction</code> is an abstract base for all Psi wave functions.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;psiwfn.h&gt;</code></pre>
<p> Inherits <code>sc::Wavefunction</code>. Inherited by <code>sc::PsiCCSD</code>, <code>sc::PsiCCSD_T</code>, and <code>sc::PsiSCF</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>PsiWavefunction (const Ref&lt; KeyVal &gt; &amp;)


The KeyVal constructor.


PsiWavefunction (StateIn &amp;)



void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


virtual void write_basic_input (int conv)


Writes out Psi input file entries specific to this PsiWavefunction.


void compute ()


Recompute at least the results that have compute true and are not already computed.


void print (std::ostream &amp;o=ExEnv::out0()) const


Print information about the object.


RefSymmSCMatrix density ()


Returns the SO density.


int nelectron ()


Returns the number of electrons.


Ref&lt; PsiExEnv &gt; get_psi_exenv () const


Return an associated PsiExEnv object.


Ref&lt; PsiInput &gt; get_psi_input () const


Return an associated PsiInput object.



Protected Member Functions
virtual void write_input (int conv)=0


Prepares a complete Psi input file. The input file is assumed to have been opened.



Protected Attributes
int nirrep_



int * docc_



int * socc_



int * frozen_docc_



int * frozen_uocc_



int multp_



int charge_



char * memory_</code></pre>
<h2>Detailed Description</h2>
<p><code>PsiWavefunction</code> is an abstract base for all Psi wave functions. </p>
<p> Its <code>KeyVal</code> constructor is invoked by all <code>KeyVal</code> constructors of concrete implementations of <code>PsiWavefunction</code>.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::PsiWavefunction::PsiWavefunction (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>KeyVal</code> constructor. .IP &quot;psienv&quot; 1c Specifies a <code>PsiExEnv</code> object. There is no default. </p>
<dl>
<dt>memory</p>
<dd>This integer specifies the amount of memory (in bytes) for Psi to use. The default is 2000000.</dl>
<dl>
<dt>debug</p>
<dd>This integer can be used to produce output for debugging. The default is 0.</dl>
<h2>Member Function Documentation</h2>
<h3>void sc::PsiWavefunction::compute () [virtual]</h3>
<p>Recompute at least the results that have compute true and are not already computed. This should only be called by Result&#8217;s members. </p>
<p> Implements <code>sc::Compute</code>.</p>
<h3>void sc::PsiWavefunction::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::Wavefunction</code>. </p>
<p> Reimplemented in <code>sc::PsiSCF</code>, <code>sc::PsiCCSD</code>, and <code>sc::PsiCCSD_T</code>.</p>
<h3>virtual void sc::PsiWavefunction::write_basic_input (int conv) [virtual]</h3>
<p>Writes out Psi input file entries specific to this <code>PsiWavefunction</code>. The input file is assumed to have been opened. </p>
<p> Reimplemented in <code>sc::PsiCLHF</code>, <code>sc::PsiHSOSHF</code>, and <code>sc::PsiUHF</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
