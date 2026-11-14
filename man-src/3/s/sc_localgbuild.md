---
title: "sc_localgbuild(3)"
name: "sc_localgbuild"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_localgbuild/"
description: "sc::LocalGBuild –"
---

<p>sc::LocalGBuild &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::GBuild&lt; T &gt;</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>LocalGBuild (T &amp;t, const Ref&lt; TwoBodyInt &gt; &amp;tbi, const Ref&lt; PetiteList &gt; &amp;rpl, const Ref&lt; GaussianBasisSet &gt; &amp;bs, const Ref&lt; MessageGrp &gt; &amp;g, signed char *pm, double acc, int nt=1, int tn=0)



void run ()


This is called with the Thread is run from a ThreadGrp.



Public Attributes
double tnint



Protected Attributes</code></pre>
<p> <code>MessageGrp</code> * <code>grp_</code> </p>
<p> <code>TwoBodyInt</code> * <code>tbi_</code> </p>
<p> <code>GaussianBasisSet</code> * <code>gbs_</code> </p>
<p> <code>PetiteList</code> * <code>rpl_</code> </p>
<p> signed char *restrictxx <code>pmax</code> </p>
<p> int <code>threadno_</code> </p>
<p> int <code>nthread_</code> </p>
<p> double <code>accuracy_</code></p>
<h3>template&lt;class T&gt; class sc::LocalGBuild&lt; T &gt;</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
