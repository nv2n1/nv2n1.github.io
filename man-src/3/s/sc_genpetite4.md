---
title: "sc_genpetite4(3)"
name: "sc_genpetite4"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_genpetite4/"
description: "sc::GenPetite4 –"
---

<p>sc::GenPetite4 &#8211; </p>
<p> This class is an abstract base to a generalized four index petite list.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;gpetite.h&gt;</code></pre>
<p> Inherits <code>sc::RefCount</code>. Inherited by <code>sc::GPetite4&lt; C4 &gt;</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>GenPetite4 (const Ref&lt; GaussianBasisSet &gt; &amp;b1, const Ref&lt; GaussianBasisSet &gt; &amp;b2, const Ref&lt; GaussianBasisSet &gt; &amp;b3, const Ref&lt; GaussianBasisSet &gt; &amp;b4)



virtual int in_p4 (int i, int j, int k, int l)=0



Protected Attributes</code></pre>
<p> bool <code>c1_</code> </p>
<p> int <code>ng_</code> </p>
<p> int ** <code>shell_map_i_</code> </p>
<p> int ** <code>shell_map_j_</code> </p>
<p> int ** <code>shell_map_k_</code> </p>
<p> int ** <code>shell_map_l_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>b1_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>b2_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>b3_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>b4_</code></p>
<h2>Detailed Description</h2>
<p>This class is an abstract base to a generalized four index petite list.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
