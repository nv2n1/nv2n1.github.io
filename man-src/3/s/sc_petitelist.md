---
title: "sc_petitelist(3)"
name: "sc_petitelist"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_petitelist/"
description: "sc::PetiteList –"
---

<p>sc::PetiteList &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::RefCount</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>PetiteList (const Ref&lt; GaussianBasisSet &gt; &amp;, const Ref&lt; Integral &gt; &amp;)



Ref&lt; GaussianBasisSet &gt; basis ()



Ref&lt; Integral &gt; integral ()



Ref&lt; PetiteList &gt; clone ()



int nirrep () const



int order () const



int atom_map (int n, int g) const



int shell_map (int n, int g) const



int lambda (int ij) const



int lambda (int i, int j) const



int in_p1 (int n) const



int in_p2 (int ij) const



int in_p2 (int i, int j) const


Same as previous, except for it takes i and j separately.


int in_p4 (int ij, int kl, int i, int j, int k, int l) const



int in_p4 (int i, int j, int k, int l) const


Same as previous, except for doesn't assume ij &gt; kl and recomputes them.


int nfunction (int i) const



int nblocks () const



void print (std::ostream &amp;=ExEnv::out0(), int verbose=1)



RefSCDimension AO_basisdim ()



RefSCDimension SO_basisdim ()



RefSCMatrix r (int g)



SO_block * aotoso_info ()



RefSCMatrix aotoso ()



RefSCMatrix sotoao ()



void symmetrize (const RefSymmSCMatrix &amp;skel, const RefSymmSCMatrix &amp;sym)



RefSymmSCMatrix to_SO_basis (const RefSymmSCMatrix &amp;)



RefSymmSCMatrix to_AO_basis (const RefSymmSCMatrix &amp;)



RefSCMatrix evecs_to_AO_basis (const RefSCMatrix &amp;)



RefSCMatrix evecs_to_SO_basis (const RefSCMatrix &amp;)
</code></pre>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
