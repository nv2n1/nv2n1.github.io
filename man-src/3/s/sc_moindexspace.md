---
title: "sc_moindexspace(3)"
name: "sc_moindexspace"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_moindexspace/"
description: "sc::MOIndexSpace –"
---

<p>sc::MOIndexSpace &#8211; </p>
<p> Class <code>MOIndexSpace</code> describes a range of molecular orbitals or similar objects that are linear combinations of basis functions (e.g.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;moindexspace.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>.</p>
<h3>Public Types</h3>
<pre><code>enum IndexOrder { symmetry =  0, energy =  1, undefined =  2 }


Describes the ordering of indices.



Public Member Functions</code></pre>
<p> <code>MOIndexSpace</code> (<code>StateIn</code> &amp;) </p>
<p> <code>MOIndexSpace</code> (std::string name, const <code>RefSCMatrix</code> &amp;full_coefs, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; basis, const <code>Ref</code>&lt; <code>Integral</code> &gt; &amp;integral, const vector&lt; int &gt; &amp;offsets, const vector&lt; int &gt; &amp;nmopi, <code>IndexOrder</code> moorder=symmetry, const <code>RefDiagSCMatrix</code> &amp;evals=0)<br />
 <i>This function constructs an </i><code>MOIndexSpace</code> from (blocked) space full_coefs.<br />
 <code>MOIndexSpace</code> (std::string name, const <code>RefSCMatrix</code> &amp;full_coefs, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; basis, const <code>Ref</code>&lt; <code>Integral</code> &gt; &amp;integral, const <code>RefDiagSCMatrix</code> &amp;evals, int nfzc, int nfzv, <code>IndexOrder</code> moorder=energy)<br />
 <i>This constructor should be used when the </i><code>MOIndexSpace</code> object is a subspace of a full orbital space.<br />
 <code>MOIndexSpace</code> (std::string name, const <code>RefSCMatrix</code> &amp;full_coefs, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; basis, const <code>Ref</code>&lt; <code>Integral</code> &gt; &amp;integral)<br />
 <i>This constructor should be used when the </i><code>MOIndexSpace</code> object is the full orbital space.<br />
 <code>MOIndexSpace</code> (std::string name, const <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; &amp;orig_space, const <code>RefSCMatrix</code> &amp;new_coefs, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;new_basis)<br />
 <i>This constructor is a true hack introduced because I have no idea how to construct what I need. </i><br />
 void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 const std::string <code>name</code> () const<br />
 <i>Returns the name of this </i><code>MOIndexSpace</code>.<br />
 const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>basis</code> () const<br />
 <i>Returns the AO basis set. </i><br />
 <code>Ref</code>&lt; <code>Integral</code> &gt; <code>integral</code> () const<br />
 <i>Returns the integral factory used to instantiate the coefficient matrix. </i><br />
 const <code>RefSCMatrix</code> <code>coefs</code> () const<br />
 <i>Returns the coefficient matrix. </i><br />
 const <code>RefDiagSCMatrix</code> <code>evals</code> () const<br />
 <i>Returns the &#8216;eigenvalues&#8217; matrix. </i><br />
 vector&lt; int &gt; <code>mosym</code> () const<br />
 <i>Returns the orbital symmetry array. </i><br />
 <code>IndexOrder</code> <code>moorder</code> () const<br />
 <i>Returns the order of the orbitals. </i><br />
 int <code>rank</code> () const<br />
 <i>Returns the rank of the space. </i><br />
 int <code>full_rank</code> () const<br />
 <i>Returns the rank of the full space. </i><br />
 int <code>nblocks</code> () const<br />
 <i>Returns the number of blocks. </i><br />
 vector&lt; int &gt; <code>nmo</code> () const<br />
 <i>Returns the number of orbitals in each block. </i><br />
 vector&lt; int &gt; <code>offsets</code> () const<br />
 <i>Returns the full-space index of the first orbital in each block. </i><br />
 int <code>to_full_space</code> (const int i) const<br />
 <i>Returns the full-space index. </i><br />
 size_t <code>memory_in_use</code> () const<br />
 <i>Returns how much &#8216;significant&#8217; (i.e. O^2) memory this object uses. </i><br />
 void <code>print</code> (std::ostream &amp;o=ExEnv::out0()) const<br />
 <i>Prints out this. </i><br />
 void <code>print_summary</code> (std::ostream &amp;os) const<br />
 <i>Produces a short summary. </i></p>
<h2>Detailed Description</h2>
<p>Class <code>MOIndexSpace</code> describes a range of molecular orbitals or similar objects that are linear combinations of basis functions (e.g. </p>
<p> atomic orbitals). In general, such sets are subspaces of a full space of orbitals supported by the given basis. Orbitals can be symmetry-blocked, ordered by energy, etc. Examples of sets that can be described using <code>MOIndexSpace</code> are occupied MOs and virtual MOs.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::MOIndexSpace::MOIndexSpace (std::string name, const <code>RefSCMatrix</code> &amp; full_coefs, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; basis, const <code>Ref</code>&lt; <code>Integral</code> &gt; &amp; integral, const vector&lt; int &gt; &amp; offsets, const vector&lt; int &gt; &amp; nmopi, <code>IndexOrder</code> moorder = symmetry, const <code>RefDiagSCMatrix</code> &amp; evals = 0)</h3>
<p>This function constructs an <code>MOIndexSpace</code> from (blocked) space full_coefs. Block i will contain vectors [ offsets[i], offsets[i]+nmopi[i]-1 ] . By default, the space maintains the same blocked structure and the same order within blocks as the original space (moorder=symmetry). If moorder=energy and eigenvalues evals are provided, then all vectors will be put in one block and sorted according to ascending evals. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>name</i> &#8212; the name of this <code>MOIndexSpace</code><br />
 <i>full_coefs</i> &#8212; symmetry-blocked transformation coefficient matrix (AO by MO) for the full space<br />
 <i>basis</i> &#8212; basis set<br />
 <i>integral</i> &#8212; integral factory<br />
 <i>offsets</i> &#8212; block offsets<br />
 <i>nmopi</i> &#8212; new block sizes<br />
 <i>moorder</i> &#8212; specifies new ordering of vectors<br />
 <i>evals</i> &#8212; used to sort the vectors</dl>
<h3>sc::MOIndexSpace::MOIndexSpace (std::string name, const <code>RefSCMatrix</code> &amp; full_coefs, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; basis, const <code>Ref</code>&lt; <code>Integral</code> &gt; &amp; integral, const <code>RefDiagSCMatrix</code> &amp; evals, int nfzc, int nfzv, <code>IndexOrder</code> moorder = energy)</h3>
<p>This constructor should be used when the <code>MOIndexSpace</code> object is a subspace of a full orbital space. Similarly to the previous constructor, it constructs an <code>MOIndexSpace</code> object using a symmetry-blocked transformation coefficient matrix (AO by MO) for the full space, basis set, &#8216;eigenvalues&#8217; and the number of orbitals with lowest (nfzc) and highest (nfzv) eigenvalues to be dropped. The orbitals in the constructed space are ordered by energy.</p>
<h3>sc::MOIndexSpace::MOIndexSpace (std::string name, const <code>RefSCMatrix</code> &amp; full_coefs, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; basis, const <code>Ref</code>&lt; <code>Integral</code> &gt; &amp; integral)</h3>
<p>This constructor should be used when the <code>MOIndexSpace</code> object is the full orbital space. The orbitals will be symmetry-blocked.</p>
<h3>sc::MOIndexSpace::MOIndexSpace (std::string name, const <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; &amp; orig_space, const <code>RefSCMatrix</code> &amp; new_coefs, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp; new_basis)</h3>
<p>This constructor is a true hack introduced because I have no idea how to construct what I need. It will copy orig_space but replace it&#8217;s coefs with new_coefs, and its basis with new_basis.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::MOIndexSpace::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
