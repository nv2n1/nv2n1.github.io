---
title: "sc_sobasis(3)"
name: "sc_sobasis"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_sobasis/"
description: "sc::SOBasis –"
---

<p>sc::SOBasis &#8211; </p>
<p> A <code>SOBasis</code> object describes the transformation from an atomic orbital basis to a symmetry orbital basis.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;sobasis.h&gt;</code></pre>
<p> Inherits <code>sc::RefCount</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>SOBasis (const Ref&lt; GaussianBasisSet &gt; &amp;, const Ref&lt; Integral &gt; &amp;)


Create an SOBasis object given a GaussianBasisSet and Integral objects.


int nshell () const


Return the number of shells.


int nirrep () const


Return the number of irreps.


int ncomponent (int iirrep) const



int nfunction_in_irrep (int irrep) const


Return the number of functions in the given irrep.


int function_offset_for_irrep (int irrep) const


Return the offset for the first function of the given irrep.


int nfunction (int ishell) const


Return the number of functions in the given shell.


int naofunction (int ishell) const


Return the number of functions in the AO shell that make up the given SO shell.


int nfunction (int ishell, int iirrep) const


Returns the number of functions in the shell in a given irrep.


int max_nfunction_in_shell () const


Returns the maximum number of functions in a shell (summed over all irreps).


int function_offset_within_shell (int ishell, int iirrep) const


Normally, SO shell numbering starts at zero within each irrep.


int function (int ishell)


Convert the SO shell number to the overall number of the first function within that shell.


int irrep (int ishell, int ifunc) const


Convert SO shell and function number within shell to irrep.


int function_within_irrep (int ishell, int ifunc) const


Convert SO shell and function number to number within irrep.


const SOTransform &amp; trans (int i) const


Return the SOTransform object for the given shell.


void print (std::ostream &amp;o=ExEnv::out0()) const



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>basis_</code> </p>
<p> int <code>nshell_</code> </p>
<p> int <code>nirrep_</code> </p>
<p> int * <code>ncomp_</code> </p>
<p> int ** <code>nfunc_</code> </p>
<p> int * <code>naofunc_</code> </p>
<p> int ** <code>funcoff_</code> </p>
<p> int * <code>nfunc_in_irrep_</code> </p>
<p> int * <code>func_</code> </p>
<p> int * <code>irrep_</code> </p>
<p> int * <code>func_within_irrep_</code> </p>
<p> <code>SOTransform</code> * <code>trans_</code></p>
<h2>Detailed Description</h2>
<p>A <code>SOBasis</code> object describes the transformation from an atomic orbital basis to a symmetry orbital basis.</p>
<h2>Member Function Documentation</h2>
<h3>int sc::SOBasis::function (int ishell) [inline]</h3>
<p>Convert the <code>SO</code> shell number to the overall number of the first function within that shell.</p>
<h3>int sc::SOBasis::function_offset_within_shell (int ishell, int iirrep) const [inline]</h3>
<p>Normally, <code>SO</code> shell numbering starts at zero within each irrep. This returns an offset to make <code>SO</code> shell numbers unique within the shell.</p>
<h3>int sc::SOBasis::naofunction (int ishell) const [inline]</h3>
<p>Return the number of functions in the AO shell that make up the given <code>SO</code> shell.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
